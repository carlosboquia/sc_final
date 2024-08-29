""""
Description: A class to manage LibraryItem objects.
Author: Carlos Boquia
Date: August 28 2024
"""
from genre.genre import Genre

class LibraryItem():
    """
    Represents the items within libary

    Attributess:
        title (str): The title of the book.
        author (str): The author of the book.
        genre (Genre): The genre of the book.
    
    """

    def __init__(self, title:str, author:str, genre: Genre):

        """
        Grabs the title, author and genre of a book from the library
        and updatess the inventory. 

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (Genre): The genre of the book.
        Returns:
            self.__title (str): Returns private title attribute.
            self.__author(str): Returns private author attribute.
            self.__genre (Genre): Returns private genre attribute.
        Raises:
            ValueError: "Title cannot be blank"
            ValueError: "Author cannot be blank"
            ValueError: "Invalid Genre"
        """

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
        

    # Accessors

    @property
    def title(self) -> str:
        return self.__title
        
    @property
    def author(self) -> str:
        return self.__author
    
    @property
    def genre(self) -> Genre:
        return self.__genre
        