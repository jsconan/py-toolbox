"""Test the set of helpers for working with concurrent programming."""

import unittest

from cerbernetix.toolbox.system import concurrent_tasks


class TestParallel(unittest.TestCase):
    """Test suite for the set of helpers for working with concurrent programming."""

    def test_concurrent_tasks_with_list_params(self):
        """Test concurrent_tasks using list parameters."""

        def add(a, b):
            return a + b

        task_args = [
            [1, 2],
            [3, 4],
            [5, 6],
        ]

        results = concurrent_tasks(add, task_args)

        self.assertIsInstance(results, type((i for i in range(1))))
        self.assertEqual(list(results), [3, 7, 11])

    def test_concurrent_tasks_with_dict_params(self):
        """Test concurrent_tasks using list parameters."""

        def add(a, b):
            return a + b

        task_args = [
            {"a": 1, "b": 2},
            {"a": 3, "b": 4},
            {"a": 5, "b": 6},
        ]

        results = concurrent_tasks(add, task_args)

        self.assertIsInstance(results, type((i for i in range(1))))
        self.assertEqual(list(results), [3, 7, 11])
