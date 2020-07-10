## latmap

So far this is a prototype of automatically generating contextual lexers from BNF grammar.

To build parser, install [frontend-for-free](https://github.com/thautwarm/frontend-for-free).

```
> fff grammar.rbnf --trace
```

The parser needs no runtime dependency except Python stdlib.

To run the GUI, `python main.py`. You might install GUI dependencies
from `requirements.pip`.
