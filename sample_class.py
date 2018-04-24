#!/usr/bin/env python
import fire


class Sample():
    def hello(count=1, name='world'):
        """Simple method that greets NAME for a total of COUNT times."""
        for _ in range(count):
            print("Hello, {name}!".format(name=name))


def main():
    fire.Fire(Sample)


if __name__ == '__main__':
    main()
