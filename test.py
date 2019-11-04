import unittest
from LongestSuffix import longest_suffix


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(longest_suffix("a", "a"), 1)

    def test2(self):
        self.assertEqual(longest_suffix("ab+", "c"), 0)

    def test3(self):
        self.assertEqual(longest_suffix("ab+", "a"), 1)

    def test4(self):
        self.assertEqual(longest_suffix("ab+ca+.", "ac"), 2)

    def test5(self):
        self.assertEqual(longest_suffix("ca+*a.a.bc+*.", "acaccccaacaabbcccbcb"), 20)

    def test6(self):
        self.assertEqual(longest_suffix("ac+b+*c.b.c.c*.", "acbabaccbac"), 1)

    def test7(self):
        self.assertEqual(longest_suffix("1a+b.", "cb"), 1)

    def test8(self):
        self.assertEqual(longest_suffix("ca.a.ab.+*", "cacababcaa"), 7)

    def test9(self):
        self.assertEqual(longest_suffix("ab+c.aba.*.bac.+.+*", "babc"), 2)

    def test10(self):
        self.assertEqual(longest_suffix("acb..bab.c.*.ab.ba.+.+*a.", "cbaa"), 4)

    def test11(self):
        with self.assertRaises(Exception) as context:
            longest_suffix("zsertsehtsgh14sdrg2313", "cacababcaa")
        self.assertEqual("Haven't got this letter", str(context.exception))

    def test12(self):
        with self.assertRaises(Exception) as context:
            longest_suffix("..", "cacababcaa")
        self.assertEqual("Wrong polish entry", str(context.exception))

    def test13(self):
        with self.assertRaises(Exception) as context:
            longest_suffix("aab", "cacababcaa")
        self.assertEqual("Wrong polish entry", str(context.exception))

    def test14(self):
        with self.assertRaises(Exception) as context:
            longest_suffix("a", "qwewt232")
        self.assertEqual("u haven't got this letter", str(context.exception))


if __name__ == '__main__':
    unittest.main()
