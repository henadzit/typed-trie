import pytest

from typed_trie import Trie


@pytest.mark.parametrize(
    "inserts, searches",
    [
        ([("a", "1"), ("b", "2"), ("c", "3")], [("a", "1"), ("b", "2"), ("c", "3")]),
        (
            [("a", "1"), ("aa", "2"), ("aaa", "3")],
            [("a", "1"), ("aa", "2"), ("aaa", "3")],
        ),
        ([("ab", "1"), ("ac", "2")], [("ab", "1"), ("ac", "2")]),
    ],
)
def test_search(inserts: list[tuple[str, str]], searches: list[tuple[str, str]]):
    trie = Trie()

    for key, value in inserts:
        trie.insert(key, value)

    for key, value in searches:
        assert trie.search(key) == value


@pytest.mark.parametrize(
    "inserts, search",
    [
        ([], "a"),
        ([("a", "1")], "ab"),
        ([("ab", "1")], "a"),
        ([("a", "1"), ("ab", "2")], "ac"),
    ],
)
def test_search_not_found(inserts: list[tuple[str, str]], search: str):
    trie = Trie()

    for key, value in inserts:
        trie.insert(key, value)

    with pytest.raises(KeyError):
        trie.search(search)


@pytest.mark.parametrize(
    "inserts, delete",
    [
        ([("a", "1")], "a"),
        ([("a", "1"), ("ab", "2")], "ab"),
        ([("a", "1"), ("ab", "2")], "a"),
        ([("a", "1"), ("ab", "2"), ("ac", "3")], "ab"),
    ],
)
def test_delete(inserts: list[tuple[str, str]], delete: str):
    trie = Trie()

    for key, value in inserts:
        trie.insert(key, value)

    trie.delete(delete)

    with pytest.raises(KeyError):
        trie.search(delete)
