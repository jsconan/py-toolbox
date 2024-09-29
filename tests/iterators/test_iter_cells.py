"""Test the iterator for returning elements from a list."""

import unittest

from cerbernetix.toolbox.iterators import iter_cells
from cerbernetix.toolbox.testing import test_cases


class TestIterCells(unittest.TestCase):
    """Test suite for the iterator for returning elements from a list."""

    @test_cases(
        [
            [
                "Column order, all by 1",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 1},
                [1, "\n", 2, "\n", 3, "\n", 4, "\n", 5, "\n", 6, "\n"],
            ],
            [
                "Row order, all by 1",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 1, "col_dir": False},
                [1, "\n", 2, "\n", 3, "\n", 4, "\n", 5, "\n", 6, "\n"],
            ],
            [
                "Column order, all by 2",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 2},
                [1, 4, "\n", 2, 5, "\n", 3, 6, "\n"],
            ],
            [
                "Row order, all by 2",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 2, "col_dir": False},
                [1, 2, "\n", 3, 4, "\n", 5, 6, "\n"],
            ],
            [
                "Column order, all by 3",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 3},
                [1, 3, 5, "\n", 2, 4, 6, "\n"],
            ],
            [
                "Row order, all by 3",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 3, "col_dir": False},
                [1, 2, 3, "\n", 4, 5, 6, "\n"],
            ],
            [
                "Column order, 3 cells by 2",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 2, "nb_cells": 3},
                [1, 3, "\n", 2, "\n"],
            ],
            [
                "Row order, 3 cells by 2",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 2, "nb_cells": 3, "col_dir": False},
                [1, 2, "\n", 3, "\n"],
            ],
            [
                "Column order, 3 cells by 3",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 3, "nb_cells": 3},
                [1, 2, 3, "\n"],
            ],
            [
                "Row order, 3 cells by 3",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 3, "nb_cells": 3, "col_dir": False},
                [1, 2, 3, "\n"],
            ],
            [
                "Column order, 4 cells by 3",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 3, "nb_cells": 4},
                [1, 3, "\n", 2, 4, "\n"],
            ],
            [
                "Row order, 4 cells by 3",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 3, "nb_cells": 4, "col_dir": False},
                [1, 2, 3, "\n", 4, "\n"],
            ],
            [
                "Column order, 5 cells by 3",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 3, "nb_cells": 5},
                [1, 3, 5, "\n", 2, 4, "\n"],
            ],
            [
                "Row order, 5 cells by 3",
                {"cells": [1, 2, 3, 4, 5, 6], "nb_cols": 3, "nb_cells": 5, "col_dir": False},
                [1, 2, 3, "\n", 4, 5, "\n"],
            ],
        ]
    )
    def test_iter_cells(self, _, kwargs, expected):
        """Test the iterator for returning elements from a list."""
        self.assertEqual(list(iter_cells(**kwargs)), expected)
