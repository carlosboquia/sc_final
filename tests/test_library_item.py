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

    def setUp(self):
        self.library_item = LibraryItem("Book", "Bruce Willis", Genre.TRUE_CRIME)
    
    def test_title_accessor(self):
        self.assertEqual("Book", self.library_item.title)

    def test_author_accessor(self):
        self.assertEqual("Bruce Willis", self.library_item.author)

    def test_genre_accessor(self):
        self.assertEqual(Genre.TRUE_CRIME, self.library_item.genre)

    def test_str(self):
        expected = ("Title: Book\n"
                    + "Author: Bruce Willis\n"
                    + "Genre: True Crime")
        self.assertEqual(expected, str(self.library_item))