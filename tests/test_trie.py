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
        trie[key] = value

    for key, value in searches:
        assert trie[key] == value


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
        trie[key] = value

    with pytest.raises(KeyError):
        trie[search]


@pytest.mark.parametrize(
    "inserts, delete",
    [
        ([("a", "1")], "a"),
        ([("ab", "1")], "ab"),
        ([("abc", "1")], "abc"),
        ([("a", "1"), ("ab", "2")], "ab"),
        ([("a", "1"), ("ab", "2")], "a"),
        ([("a", "1"), ("ab", "2"), ("ac", "3")], "ab"),
    ],
)
def test_delete(inserts: list[tuple[str, str]], delete: str):
    trie = Trie()

    for key, value in inserts:
        trie[key] = value

    del trie[delete]

    with pytest.raises(KeyError):
        trie[delete]


def test_delete_not_found():
    trie = Trie()
    trie["b"] = "1"

    with pytest.raises(KeyError):
        del trie["a"]


def test_setitem():
    trie = Trie()
    trie["a"] = "1"
    assert trie["a"] == "1"
    trie["a"] = "2"
    assert trie["a"] == "2"


def test_items_by_prefix():
    trie = Trie()
    trie["ab"] = "2"
    trie["abc"] = "3"
    trie["ac"] = "4"
    trie["b"] = "5"

    assert list(trie.items_by_prefix()) == [
        ("ab", "2"),
        ("abc", "3"),
        ("ac", "4"),
        ("b", "5"),
    ]
    assert list(trie.items_by_prefix("a")) == [("ab", "2"), ("abc", "3"), ("ac", "4")]
    assert list(trie.items_by_prefix("ab")) == [("ab", "2"), ("abc", "3")]
    assert list(trie.items_by_prefix("abc")) == [("abc", "3")]
    assert list(trie.items_by_prefix("abcd")) == []
    assert list(trie.items_by_prefix("b")) == [("b", "5")]
    assert list(trie.items_by_prefix("c")) == []


def test_keys_by_prefix():
    trie = Trie()
    trie["ab"] = "1"
    trie["ac"] = "2"
    trie["ad"] = "3"

    assert list(trie.keys_by_prefix()) == ["ab", "ac", "ad"]
    assert list(trie.keys_by_prefix("a")) == ["ab", "ac", "ad"]
    assert list(trie.keys_by_prefix("ab")) == ["ab"]


def test_len():
    trie = Trie()
    assert len(trie) == 0

    trie["a"] = "1"
    assert len(trie) == 1

    trie["abbbbbc"] = "2"
    assert len(trie) == 2

    del trie["a"]
    assert len(trie) == 1
