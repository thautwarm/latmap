## latmap

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">It works.. repo here <a href="https://t.co/MxI5Hr4sKe">https://t.co/MxI5Hr4sKe</a><br><br>It&#39;s about generating fast and flexible highlighting implementations from BNF grammars, which I expect for long.<br><br>P.S: It works for editors that don&#39;t manage texts as trees. <a href="https://t.co/wDYgVm6EJO">pic.twitter.com/wDYgVm6EJO</a></p>&mdash; redyred (@thautwarm) <a href="https://twitter.com/thautwarm/status/1281657073650941952?ref_src=twsrc%5Etfw">July 10, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

So far this is a prototype of automatically generating contextual lexers from BNF grammar.

To build parser, install [frontend-for-free](https://github.com/thautwarm/frontend-for-free).

```
> fff grammar.rbnf --trace
```

The parser needs no runtime dependency except Python stdlib.

To run the GUI, `python main.py`. You might install GUI dependencies
from `requirements.pip`.
