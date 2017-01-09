"""
Tests for memopy.py
"""


from memopy.memopy import memoify

import unittest


class Testmemoify(unittest.TestCase):

    def test_memoify_no_arguments(self):
        """ Wrap a function that has no arguments """

        @memoify
        def func1():
            func1.num_calls += 1
            return 5
        func1.num_calls = 0

        # make sure the function returns the same answer each time, and is only
        # executed the first time

        self.assertEqual(func1.num_calls, 0)
        self.assertEqual(func1(), 5)
        self.assertEqual(func1.num_calls, 1)
        self.assertEqual(func1(), 5)
        self.assertEqual(func1.num_calls, 1)

    def test_memoify_functions_dont_interfere(self):
        """ Wrap different functions and make sure they don't interfere """

        @memoify
        def func1():
            func1.num_calls += 1
            return 5
        func1.num_calls = 0

        @memoify
        def func2():
            func2.num_calls += 1
            return 7
        func2.num_calls = 0

        # make sure each function behaves correctly when multiple memoizing
        # functions are created

        self.assertEqual(func1.num_calls, 0)
        self.assertEqual(func1(), 5)
        self.assertEqual(func1.num_calls, 1)
        self.assertEqual(func1(), 5)
        self.assertEqual(func1.num_calls, 1)

        self.assertEqual(func2.num_calls, 0)
        self.assertEqual(func2(), 7)
        self.assertEqual(func2.num_calls, 1)
        self.assertEqual(func2(), 7)
        self.assertEqual(func2.num_calls, 1)

        self.assertEqual(func1(), 5)
        self.assertEqual(func1.num_calls, 1)

    def test_memoify_hashable_args(self):
        """ Wrap a function that is called with hashable arguments """

        @memoify
        def func1(a, b):
            func1.num_calls += 1
            return a + b
        func1.num_calls = 0

        # make sure the function returns the same answer each time it's given
        # the same inputs combo, and is only executed the first time each new
        # input combo is seen

        self.assertEqual(func1.num_calls, 0)
        self.assertEqual(func1(2, 3), 5)
        self.assertEqual(func1.num_calls, 1)
        self.assertEqual(func1(2, 3), 5)
        self.assertEqual(func1.num_calls, 1)

        self.assertEqual(func1(2, 4), 6)
        self.assertEqual(func1.num_calls, 2)
        self.assertEqual(func1(2, 4), 6)
        self.assertEqual(func1.num_calls, 2)

        self.assertEqual(func1(2, 3), 5)
        self.assertEqual(func1.num_calls, 2)

    def test_memoify_unhashable_args(self):
        """ Wrap a function that is called with unhashable args """

        @memoify
        def func1(a, b):
            func1.num_calls += 1
            return a + b
        func1.num_calls = 0

        # make sure the function returns the same answer each time it's given
        # the same inputs combo, and is only executed the first time each new
        # input combo is seen

        self.assertEqual(func1.num_calls, 0)
        self.assertEqual(func1([2], [3]), [2, 3])
        self.assertEqual(func1.num_calls, 1)
        self.assertEqual(func1([2], [3]), [2, 3])
        self.assertEqual(func1.num_calls, 1)

        self.assertEqual(func1([2], [4]), [2, 4])
        self.assertEqual(func1.num_calls, 2)
        self.assertEqual(func1([2], [4]), [2, 4])
        self.assertEqual(func1.num_calls, 2)

        self.assertEqual(func1([2], [3]), [2, 3])
        self.assertEqual(func1.num_calls, 2)

    def test_memoify_hashable_args_and_kwargs(self):
        """ Wrap a function that is called with hashable args and kwargs """

        @memoify
        def func1(tup, index=0):
            func1.num_calls += 1
            return tup[index]
        func1.num_calls = 0

        # make sure the function returns the same answer each time, and is only
        # executed the first time each new input combo is seen

        self.assertEqual(func1.num_calls, 0)
        self.assertEqual(func1((5, 7), index=0), 5)
        self.assertEqual(func1.num_calls, 1)
        self.assertEqual(func1((5, 7), index=0), 5)
        self.assertEqual(func1.num_calls, 1)

        self.assertEqual(func1((6, 8), index=1), 8)
        self.assertEqual(func1.num_calls, 2)
        self.assertEqual(func1((6, 8), index=1), 8)
        self.assertEqual(func1.num_calls, 2)

        self.assertEqual(func1((5, 7), index=0), 5)
        self.assertEqual(func1.num_calls, 2)

    def test_memoify_unhashable_args_and_kwargs(self):
        """ Wrap a function that is called with unhashable args and kwargs """

        @memoify
        def func1(dic, key, choices=None, choice_idx=0):
            func1.num_calls += 1
            choices = choices or [0]
            return dic[key] + choices[choice_idx]
        func1.num_calls = 0

        # make sure the function returns the same answer each time, and is only
        # executed the first time each new input combo is seen

        self.assertEqual(func1.num_calls, 0)
        self.assertEqual(func1({'a': 5}, 'a', choices=[3, 4], choice_idx=1), 9)
        self.assertEqual(func1.num_calls, 1)
        self.assertEqual(func1({'a': 5}, 'a', choices=[3, 4], choice_idx=1), 9)
        self.assertEqual(func1.num_calls, 1)

        self.assertEqual(func1({'b': 6}, 'b', choices=[7, 8], choice_idx=1), 14)
        self.assertEqual(func1.num_calls, 2)
        self.assertEqual(func1({'b': 6}, 'b', choices=[7, 8], choice_idx=1), 14)
        self.assertEqual(func1.num_calls, 2)

        self.assertEqual(func1({'a': 5}, 'a', choices=[3, 4], choice_idx=1), 9)
        self.assertEqual(func1.num_calls, 2)

    ## TODO: test clearing

    ## TODO: test handling exceptions
