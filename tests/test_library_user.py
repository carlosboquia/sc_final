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

    # Setup
    def setUp(self):
        self.library_user = LibraryUser(1244, "Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)
        self.library_user_delinquent = LibraryUser(1244, "Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)

    def test_init_valid(self):
        library_user = LibraryUser(1244, "Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)

    def test_init_invalid_name(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(1244, " ", "44@gmail.com", BorrowerStatus.ACTIVE)
    
    def test_init_invalid_user_id_numeric(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser("invalid", "Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)

    def test_init_invalid_user_id_under_99(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(44, "Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)

    def test_init_invalid_email(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(1244, "Jackie Chan", "invalid email", BorrowerStatus.ACTIVE)

    def test_init_invalid_bowrrower_status(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(1244, "Jackie Chan", "44@gmail.com", "invalid")

    def test_user_id_accessor(self):
        self.assertEqual(1244, self.library_user.user_id)

    def test_name_accessor(self):
        self.assertEqual("Jackie Chan", self.library_user.name)

    def test_email_accessor(self):
        self.assertEqual("44@gmail.com", self.library_user.email)

    def test_borrower_status_accessor(self):
        self.assertEqual(BorrowerStatus.ACTIVE, self.library_user.borrower_status)
    
    def test_str(self):
        expected = ("User ID: 1244\n"
                    + "Name: Jackie Chan\n"
                    + "Email: 44@gmail.com\n"
                    + "Borrower Status: Active")
        self.assertEqual(expected, str(self.library_user))

    def test_borrow_item_eligible(self):
        expected = ("Jackie Chan is eligible to borrow the item")
        self.assertEqual(self.library_user.borrow_item(),expected)

    def test_borrow_item_not_eligible(self):
        library_user = LibraryUser(1244, "Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        with self.assertRaises(ValueError):
            library_user.borrow_item()

    def test_return_item_correct_status(self):
       expected = ("Item successfully returned. Jackie Chan has returned the item, status now changed to: Active")
       self.assertEqual(self.library_user_delinquent.return_item(),expected)
    
    def test_return_item_successful_return(self):
        expected = ("Item successfully returned")
        self.assertEqual(self.library_user.return_item(), expected)



