"""
Description: Unit tests for the borrow approval function
Author: Carlos Boquia
Date: August 28 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_borrow_approval.py
"""
import unittest
from borrow_approval import borrow_item_approval
from library_user.library_user import LibraryUser
from library_item.library_item import LibraryItem
from genre.genre import Genre
from borrower_status.borrower_status import BorrowerStatus


class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.user_delinquent = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        self.user_active = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)
        self.item_borrow_false = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, False)
        self.item_borrow_true = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, True)

    def test_borrow_user_active_item_false(self):
        expected = borrow_item_approval(self.user_active, self.item_borrow_false)
        actual = "The item is available to be borrowed."
        self.assertEqual(expected, actual)

    def test_borrow_user_delinquent_item_false(self):
        with self.assertRaises(Exception) as context:
            borrow_item_approval(self.user_delinquent, self.item_borrow_false,)
        self.assertEqual(str(context.exception), "Item is not available due your status: DELINQUENT")
  
    def test_borrow_user_active_item_true(self):
        with self.assertRaises(Exception) as context:
            borrow_item_approval(self.user_active, self.item_borrow_true)
        self.assertEqual(str(context.exception), "The Item is not available to be borrowed.")
    
    def test_borrow_user_delinquent_item_true(self):
        with self.assertRaises(Exception) as context:
            borrow_item_approval(self.user_delinquent, self.item_borrow_true)
        self.assertEqual(str(context.exception), "Cannot process request due to item not being available and your status: DELINQUENT")

        
                






    
