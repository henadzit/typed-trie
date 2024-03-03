from typing import cast, TypeVar, Generic

T = TypeVar("T")


class _Unset:
    pass


UNSET = _Unset()


class TrieNode(Generic[T]):
    def __init__(self, key: str, value: T | _Unset):
        self.key = key
        self.value = value
        self.children: dict[str, TrieNode[T | _Unset]] = {}

    def __str__(self):
        return f"TrieNode({self.key}, {self.value})"


class Trie(Generic[T]):
    def __init__(self):
        self.root = TrieNode[T | _Unset]("", UNSET)

    def insert(self, key: str, value: T):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode[T | _Unset](char, UNSET)
            node = node.children[char]
        node.value = value

    def search(self, key: str) -> T:
        return cast(T, self._find_node(key).value)

    def delete(self, key: str):
        node = self._find_node(key)
        node.value = UNSET

    def _find_node(self, key: str) -> TrieNode[T | _Unset]:
        node = self.root
        for char in key:
            if char not in node.children:
                raise KeyError(key)
            node = node.children[char]

        if node.value is UNSET:
            raise KeyError(key)

        return node
