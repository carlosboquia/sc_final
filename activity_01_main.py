""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Carlos Boquia
Date: August 30 2024
"""
from library_item.library_item import LibraryItem
from library_user.library_user import LibraryUser
from genre.genre import Genre
from borrower_status.borrower_status import BorrowerStatus
from borrow_approval import borrow_item_approval

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    
    # Library Item
    try:
        library_item = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, True)

    except ValueError as e:
        print("Invalid input.", e)
    
    # Library User
    try:
        library_user = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)

    except ValueError as e:
        print(e)

    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.
    
    # Library Item
    print(f"\nTitle: {library_item.title}"
        + f"\nAuthor: {library_item.author}"
        + f"\nGenre: {library_item.genre.name.replace('_',' ').title()}"
        + f"\nUser ID: {library_item.item_id}"
        + f"\nIs Borrowed? {library_item.is_borrowed}")
    # Library User
    print(f"\nUser ID: {library_user.user_id}"
        + f"\nName: {library_user.name}"
        + f"\nEmail: {library_user.email}"
        + f"\nBorrower Status:, {library_user.borrower_status.name.title()}")

        ## 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    # Library Item - Invalid
    try:
        invalid_library_item = LibraryItem("", "", "invalid genre","non-numeric", "ture")
    except Exception as e:
        print(e)
    
    # Library User - Invalid
    try:
        invalid_library_user = LibraryUser(44,"","emailcom","invalidborrower")
    except Exception as e:
        print(e)
    # Library User - Invalid 2
    try:
        invalid_library_user = LibraryUser("invalid","","emailcom","invalidborrower")
    except Exception as e:
        print(e)

    # borrow_item
    try:
        invalid_borrow_delinquent = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        print(invalid_borrow_delinquent.borrow_item())
    except Exception as e:
        print(e)
    
    # return_item
    try:
        return_item_status_change = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        print(return_item_status_change.return_item())
    except Exception as e:
        print(e)

    
    
    # Bonus
    
    # Active and False
    try:
        user_active = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)
        item_borrow_false = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, False)
        print(borrow_item_approval(user_active,item_borrow_false))
    except Exception as e:
        print(e)    
    
    
    # Delinquent and False    
    try:
        user_delinquent = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        item_borrow_false = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, False)
        print(borrow_item_approval(user_delinquent,item_borrow_false))
    except Exception as e:
        print(e)
    
    
    # Active and True
    try:
        user_active = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)
        item_borrow_true = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, True)
        print(borrow_item_approval(user_active, item_borrow_true))
    except Exception as e:
        print(e)
        
    
    # Delinquent and True
    try:
        user_delinquent = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.DELINQUENT)
        item_borrow_true = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, True)
        print(borrow_item_approval(user_delinquent,item_borrow_true))
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()



