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

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        library_item = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME, 1244, True)

    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.

        print("Title:", library_item.title)
        print("Author:", library_item.author)
        print("Genre:", library_item.genre.name.replace('_',' ').title())
        print("Item ID:", library_item.item_id)
        print("Is Borrowed?", library_item.is_borrowed)

    except ValueError as e:
        print("Invalid input.", e)
    try:
        library_user = LibraryUser(1244,"Jackie Chan", "44@gmail.com", BorrowerStatus.ACTIVE)
        print("User ID:", library_user.user_id)
        print("Name:", library_user.name)
        print("Email:", library_user.email)
        print("Borrower Status:", library_user.borrower_status.name.title())
    except ValueError as e:
        print("invalid input.", e)

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
        invalid_lib_item = LibraryItem("", "", " ")
        print("One or more invalid input created.")

if __name__ == "__main__":
    main()