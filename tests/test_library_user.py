"""
Description: Unit tests for the LibraryUser class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_user.py
"""

import unittest
from borrower_status.borrower_status import BorrowerStatus
from library_user.library_user import LibraryUser


class TestClient(unittest.TestCase):

    def test_init_valid(self):
        library_user = LibraryUser (1244, "Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)