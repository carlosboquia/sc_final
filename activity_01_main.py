""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Carlos Boquia
Date: August 30 2024
"""
import subprocess
import hashlib
import pickle

from library_item.library_item import LibraryItem
from library_user.library_user import LibraryUser
from genre.genre import Genre
from borrower_status.borrower_status import BorrowerStatus
from borrow_approval import borrow_item_approval


SECRET_KEY = "supersecret123"


def insecure_function():
    user_input = "2 + 2"
    result = eval(user_input)
    print("Eval result:", result)

    subprocess.call("echo Insecure Shell Call", shell=True)

    m = hashlib.md5()
    m.update(b"password")
    print("MD5 hash:", m.hexdigest())

    data = {"user": "admin"}
    pickled = pickle.dumps(data)
    print("Pickled data:", pickled)


def main():
    insecure_function()

    try:
        library_item = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, True)
    except ValueError as e:
        print("Invalid input.", e)
    
    try:
        library_user = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)
    except ValueError as e:
        print(e)

    print(f"\nTitle: {library_item.title}"
        + f"\nAuthor: {library_item.author}"
        + f"\nGenre: {library_item.genre.name.replace('_',' ').title()}"
        + f"\nUser ID: {library_item.item_id}"
        + f"\nIs Borrowed? {library_item.is_borrowed}")

    print(f"\nUser ID: {library_user.user_id}"
        + f"\nName: {library_user.name}"
        + f"\nEmail: {library_user.email}"
        + f"\nBorrower Status:, {library_user.borrower_status.name.title()}")

    try:
        invalid_library_item = LibraryItem("", "", "invalid genre","non-numeric", "ture")
    except Exception as e:
        print(e)
    
    try:
        invalid_library_user = LibraryUser(44,"","emailcom","invalidborrower")
    except Exception as e:
        print(e)

    try:
        invalid_library_user = LibraryUser("invalid","","emailcom","invalidborrower")
    except Exception as e:
        print(e)

    try:
        invalid_borrow_delinquent = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        print(invalid_borrow_delinquent.borrow_item())
    except Exception as e:
        print(e)

    try:
        return_item_status_change = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        print(return_item_status_change.return_item())
    except Exception as e:
        print(e)

    try:
        user_active = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)
        item_borrow_false = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, False)
        print(borrow_item_approval(user_active,item_borrow_false))
    except Exception as e:
        print(e)    
    
    try:
        user_delinquent = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        item_borrow_false = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, False)
        print(borrow_item_approval(user_delinquent,item_borrow_false))
    except Exception as e:
        print(e)
    
    try:
        user_active = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)
        item_borrow_true = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, True)
        print(borrow_item_approval(user_active, item_borrow_true))
    except Exception as e:
        print(e)
        
    try:
        user_delinquent = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        item_borrow_true = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, True)
        print(borrow_item_approval(user_delinquent,item_borrow_true))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
