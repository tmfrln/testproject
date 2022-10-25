# -*- coding: utf-8 -*-

import unittest

from testproject.teststuff import answer

class TestAnswer(unittest.TestCase):
    def test_value(self):
        assert answer() == 42
