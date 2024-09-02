""""
Description: A class to manage LibraryItem objects.
Author: Carlos Boquia
Date: August 28 2024
"""
from genre.genre import Genre

class LibraryItem():
    """
    Represents the items within libary

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        genre (Genre): The genre of the book.
        item_id(int): An id number to uniquely identify the library item.
        is_borrowed(bool): Identifies whether the library item is
            borrowed (True) or available (False). 
    
    """

    def __init__(self, title:str, author:str, genre: Genre, item_id:int, is_borrowed:bool):

        """
        Grabs the title, author and genre of a book from the library
        and updatess the inventory. 

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (Genre): The genre of the book.
            item_id(int): An id number to uniquely identify the library item.
            is_borrowed(bool): Identifies whether the library item is
                borrowed (True) or available (False). 
        Returns:
            self.__title (str): Returns private title attribute.
            self.__author(str): Returns private author attribute.
            self.__genre (Genre): Returns private genre attribute.
            self.__item_id (int) Returns the item_id private attribute
            self.__is_borrowed(bool): Returns the private is_borrowed attribute
        Raises:
            ValueError: Title cannot be blank
            ValueError: Author cannot be blank
            ValueError: Invalid Genre
            ValueError: Item ID must be numeric
            ValueError: Is Borrowed must be boolean value
        """
        # Part 1
        if len(title.strip()) == 0:
            raise ValueError ("Title cannot be blank")
        else:
            self.__title = title
        
        if len(author.strip()) == 0:
            raise ValueError ("Author cannot be blank")
        else:
            self.__author = author
        
        if isinstance(genre, Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre")
        
        # Part 2
        if isinstance(item_id,int):
            self.__item_id = item_id
        else:
            raise ValueError("Item ID must be numeric")
        
        if isinstance(is_borrowed, bool):
            self.__is_borrowed = is_borrowed
        else:
            raise ValueError ("Is Borrowed must be boolean value")
        

    # Accessors
    # Part 1
    @property
    def title(self) -> str:
        return self.__title
        
    @property
    def author(self) -> str:
        return self.__author

    @property
    def genre(self) -> Genre:
        return self.__genre
    
    def __str__(self) -> str:
        return (f"Title: {self.__title}"
            + f"\nAuthor: {self.__author}"
            + f"\nGenre: {self.__genre.name.replace('_',' ').title()}"
            + f"\nItem ID: {self.__item_id}"
            + f"\nIs Borrowed? {self.__is_borrowed}") 
    
    # Part 2
    @property
    def item_id(self) -> int:
        return self.__item_id
    
    @property
    def is_borrowed(self) -> bool:
        return self.__is_borrowed
    


name = "ronald"
print(name)