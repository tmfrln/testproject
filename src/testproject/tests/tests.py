# -*- coding: utf-8 -*-

import unittest

from testproject.teststuff import answer

class TestAnswer(unittest.TestCase):
    def test_value(self):
        assert answer() == 42

    def test_failing(self):
        assert False
