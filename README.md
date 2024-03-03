# typed-trie

A pure Python implementation of [trie](https://en.wikipedia.org/wiki/Trie) with typing.

## Usage

```
>>> from typed_trie import Trie
>>>
>>> trie = Trie()
>>> trie.insert("how to cook", 1)
>>> trie.insert("how to swim", 2)
>>> trie.search("how to cook")
1
>>> trie.delete("how to cook")
>>> trie.search("how to cook")
...
    raise KeyError(key)
KeyError: 'how to cook'
```

## License

`repipe` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.