import sys
from textwrap import wrap


def cowsay(text):
    bubble = "\n".join(
        [" " + "_" * (len(line) + 2) for line in wrap(text, 40)]
        + ["/"]
        + [f"< {line} >" for line in wrap(text, 40)]
        + ["\\"]
        + [" " + "-" * (len(line) + 2) for line in wrap(text, 40)]
    )
    cow = "\n        \\   ^__^\n         \\  (oo)\\_______\n            (__)\\       )\\/\\\n                ||----w |\n                ||     ||"
    print(bubble + cow)


cowsay(" ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Moo!")
