#!/usr/bin/env python3

import unittest


class TestFibonacciSequence(unittest.TestCase):
    def setUp(self):
        with open("fib.txt") as f:
            self.values = [int(line) for line in f.readlines()]

    def test_increasing(self):
        pairs = list(zip(self.values[:-1], self.values[1:]))
        self.assertEqual(len(pairs), len(self.values) - 1)
        for smaller, larger in pairs:
            self.assertLessEqual(smaller, larger)


if __name__ == "__main__":
    unittest.main()
