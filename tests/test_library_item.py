"""
Description: Unit tests for the Book class.
Author: Carlos Boquia
Date: August 28 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_item.py
"""

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class TestClient(unittest.TestCase):
    def test_init_valid(self):
        library_item = LibraryItem ("Book", "Bruce Willis", Genre.TRUE_CRIME)

    def test_init_invalid_title(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(" ", "Bruce Willis", Genre.TRUE_CRIME)

    def test_init_invalid_author(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem ("Book", " ", Genre.TRUE_CRIME)

    def test_init_invalid_genre(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem ("Book", "Bruce Willis", "invalid")