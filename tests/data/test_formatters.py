"""Test the collection of formatting utilities."""

import unittest
from unittest.mock import patch

from cerbernetix.toolbox.data import format_heading, print_heading
from cerbernetix.toolbox.testing import test_cases


class TestDataFormatters(unittest.TestCase):
    """Test suite for the collection of formatting utilities."""

    FORMAT_HEADING_CASES = [
        [
            "Default",
            {"title": "Hello"},
            "\n" + ("-" * 46) + " Hello " + ("-" * 47) + "\n\n",
        ],
        [
            "Centered",
            {"title": "Hello", "justify": 0},
            "\n" + ("-" * 46) + " Hello " + ("-" * 47) + "\n\n",
        ],
        [
            "Left justified",
            {"title": "Hello", "justify": -1},
            "\nHello " + ("-" * 94) + "\n\n",
        ],
        [
            "Right justified",
            {"title": "Hello", "justify": 1},
            "\n" + ("-" * 94) + " Hello\n\n",
        ],
        [
            "No margin",
            {"title": "Hello", "margin": 0},
            ("-" * 46) + " Hello " + ("-" * 47) + "\n",
        ],
        [
            "Different margins",
            {"title": "Hello", "margin": [2, 3]},
            "\n\n" + ("-" * 46) + " Hello " + ("-" * 47) + "\n\n\n\n",
        ],
        [
            "Same margin",
            {"title": "Hello", "margin": 2},
            "\n\n" + ("-" * 46) + " Hello " + ("-" * 47) + "\n\n\n",
        ],
        [
            "Single margin",
            {"title": "Hello", "margin": [2]},
            "\n\n" + ("-" * 46) + " Hello " + ("-" * 47) + "\n\n\n",
        ],
        [
            "Title length",
            {"title": "Hello", "length": None},
            "\nHello\n\n",
        ],
        [
            "Short length",
            {"title": "Hello", "length": 13},
            "\n--- Hello ---\n\n",
        ],
        [
            "Decorator",
            {"title": "Hello", "decorator": "#"},
            "\n" + ("#" * 46) + " Hello " + ("#" * 47) + "\n\n",
        ],
        [
            "No decorator",
            {"title": "Hello", "decorator": ""},
            "\n" + ("-" * 46) + " Hello " + ("-" * 47) + "\n\n",
        ],
        [
            "Double decorator",
            {"title": "Hello", "simple": False},
            "\n"
            + ("-" * 100)
            + "\n"
            + (" " * 46)
            + " Hello "
            + (" " * 47)
            + "\n"
            + ("-" * 100)
            + "\n\n",
        ],
    ]

    @test_cases(FORMAT_HEADING_CASES)
    def test_format_heading(self, _, kwargs, value):
        """Test the title is formatted."""
        self.assertEqual(format_heading(**kwargs), value)

    @test_cases(FORMAT_HEADING_CASES)
    def test_print_heading(self, _, kwargs, value):
        """Test the title is printed."""
        with patch("builtins.print") as mock_print:
            self.assertIsNone(print_heading(**kwargs))
            mock_print.assert_called_once_with(value, end="")
