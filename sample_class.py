#!/usr/bin/env python
import fire


class Sample():
    def hello(self, count=1, name='me'):
        """Simple method that greets NAME for a total of COUNT times."""
        for _ in range(count):
            print("Hello, {name}!".format(name=name))


def main():
    sample = Sample()
    fire.Fire(sample)


if __name__ == '__main__':
    main()
