# typed-trie

A pure Python implementation of [trie](https://en.wikipedia.org/wiki/Trie) with typing.

## Install

`pip install typed-trie` or `poetry add typed-trie`.

## Usage

```
>>> from typed_trie import Trie
>>>
>>> trie = Trie()
>>> trie["how to cook"] = 1
>>> trie["how to swim"] = 2
>>> trie["who is john doe"] = 3
>>> list(trie.items_by_prefix("how to"))
[('how to cook', 1), ('how to swim', 2)]
>>> del trie["how to cook"]
```

## License

`typed-trie` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.