""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""
from library_item.library_item import LibraryItem
from genre.genre import Genre

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
        library_item = LibraryItem("Die Hard", "Bruce Willis", Genre.TRUE_CRIME)

    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.

        print("Title:", library_item.title)
        print("Author:", library_item.author)
        print("Genre:", library_item.genre.name.replace('_',' ').title())

    except ValueError as e:
        print("Invalid input.", e)


    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
        invalid_lib_item = LibraryItem("", "", " ")
        print("One or more invalid input created.")

if __name__ == "__main__":
    main()