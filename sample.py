#!/usr/bin/env python
import fire


def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        print("Hello, {name}!".format(name=name))


def main():
    fire.Fire(hello)


if __name__ == '__main__':
    main()
