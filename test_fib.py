#!/usr/bin/env python3

import unittest


class TestFibonacciSequence(unittest.TestCase):
    def setUp(self):
        with open("fibb.txt") as f:
            self.values = [int(line) for line in f.readlines()]

    def test_increasing(self):
        pairs = list(zip(self.values[:-1], self.values[1:]))
        self.assertEqual(len(pairs), len(self.values) - 1)
        for smaller, larger in pairs:
            self.assertLessEqual(smaller, larger)

    def test_values(self):
        triples = list(zip(self.values[:-2], self.values[1:-1], self.values[2:]))
        self.assertEqual(len(triples), len(self.values) - 2)
        for first, second, third in triples:
            self.assertEqual(first + second, third)


if __name__ == "__main__":
    unittest.main()
