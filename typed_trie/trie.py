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

    def __repr__(self):
        return f"TrieNode({self.key}, {self.value})"

    def __str__(self):
        return f"TrieNode({self.key}, {self.value})"


class Trie(Generic[T]):
    def __init__(self):
        self.root = TrieNode[T | _Unset]("", UNSET)

    def __repr__(self):
        return f"Trie({self.root})"

    def __str__(self):
        return f"Trie({self.root})"

    def insert(self, key: str, value: T):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode[T | _Unset](char, UNSET)
            node = node.children[char]
        node.value = value

    def search(self, key: str) -> T:
        node = self.root
        for char in key:
            if char not in node.children:
                raise KeyError(key)
            node = node.children[char]

        if node.value is UNSET:
            raise KeyError(key)

        return cast(T, node.value)

    def delete(self, key: str):
        node = self.root
        for char in key:
            if char not in node.children:
                return
            node = node.children[char]
        node.value = UNSET
