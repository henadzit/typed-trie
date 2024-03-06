from collections.abc import MutableMapping
from typing import cast, TypeVar, Generic

T = TypeVar("T")


class _Unset:
    pass


UNSET = _Unset()


class TrieNode(Generic[T]):

    def __init__(self, value: T | _Unset):
        self.value = value
        self.children: dict[str, TrieNode[T]] = {}

    def iterate(self, prefix: str):
        stack: list[tuple[str, TrieNode[T]]] = [(prefix, self)]

        while stack:
            current_prefix, node = stack.pop()

            if node.value is not UNSET:
                yield current_prefix, node.value

            # reverse to preserve the insert order
            for char, child in reversed(node.children.items()):
                stack.append((current_prefix + char, child))


class Trie(MutableMapping[str, T]):
    def __init__(self):
        self.root = TrieNode[T | _Unset](UNSET)

    def __setitem__(self, key: str, value: T):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode[T | _Unset](UNSET)
            node = node.children[char]
        node.value = value

    def __getitem__(self, key: str) -> T:
        return cast(T, self._find_node(key).value)

    def __delitem__(self, key: str):
        node = self.root
        stack: list[tuple[str, TrieNode[T | _Unset]]] = [("", node)]
        for char in key:
            if char not in node.children:
                raise KeyError(key)
            node = node.children[char]
            stack.append((char, node))

        if node.value is UNSET:
            raise KeyError(key)

        node.value = UNSET

        self._cleanup(stack)

    def items_by_prefix(self, prefix: str = ""):
        node = self._try_finding_node(prefix)

        if node is None:
            return

        yield from node.iterate(prefix)

    def keys_by_prefix(self, prefix: str = ""):
        for key, _ in self.items_by_prefix(prefix):
            yield key

    def values_by_prefix(self, prefix: str = ""):
        for _, value in self.items_by_prefix(prefix):
            yield value

    def _find_node(self, key: str) -> TrieNode[T | _Unset]:
        node = self.root
        for char in key:
            if char not in node.children:
                raise KeyError(key)
            node = node.children[char]

        if node.value is UNSET:
            raise KeyError(key)

        return node

    def _try_finding_node(self, key: str) -> TrieNode[T | _Unset] | None:
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]

        return node

    def __iter__(self):
        yield from self.keys_by_prefix()

    def __len__(self):
        return sum(1 for _ in self)

    def _cleanup(self, stack: list[tuple[str, TrieNode[T | _Unset]]]):
        child_char = None
        while stack:
            char, node = stack.pop()

            if child_char is not None:
                del node.children[child_char]

            if node.children or node.value is not UNSET:
                break

            child_char = char
