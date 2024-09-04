""""
Description: A class to manage User objects.
Edited by: Carlos Boquia
Date: August 30 2024
"""
from borrower_status.borrower_status import BorrowerStatus
from email_validator import validate_email, EmailNotValidError
from library_item.library_item import LibraryItem

class LibraryUser():
    """
    Represents the status of library user

    Attributes:
        user_id (int): The unique user id value of the library user.
        name (str): The name of the library user.
        email: The email address of the library user.
        borrower_status: The current status of the library user.
    
    """
    def __init__(self, user_id:int, name:str, email:str, borrower_status: BorrowerStatus):
        """
        Args:
            user_id (int): The unique user id value of the library user.
            name (str): The name of the library user.
            email(str): The email address of the library user.
            borrower_status(BorrowStatus): The current status of the library user.
        
        Returns:
            self.__user_id (int): Returns a private attribute of the unique user id value of the library user.
            self.__name (str): Returns a private attribute of the name of the library user.
            self.__email(str): Returns a private attribute of the email address of the library user.
            self.__borrower_status(BorrowStatus): Returns a private attribute of the current status of the library user.
        Raises:
            ValueError: User ID must be numeric
            ValueError: name cannot be blank
            ValueError: invalid email address
            ValueError: invalid borrower status
        """
        if not isinstance(user_id, int):
            raise ValueError("User ID must be numeric")
        elif user_id <= 99:
            raise ValueError("Invalid User ID: must be greater than 99")
        else:
            self.__user_id = user_id

        if len(name.strip()) == 0:
            raise ValueError("Name cannot be blank")
        else:
            self.__name = name
        
        if isinstance(email,str):
            try:
                validated_email = validate_email(email, check_deliverability = False)  
                self.__email = validated_email.email
            except EmailNotValidError as e:
                raise ValueError(f"Invalid Email Address: {e}") 
        else:
            raise ValueError(f"Invalid Email Address")
        
        if isinstance(borrower_status,BorrowerStatus):
            self.__borrower_status = borrower_status
        else:
            raise ValueError("Invalid borrower status")
        
    # Accessors
    @property
    def user_id(self) -> int:
        """
        Accessor for the user_id attribute
        """      
        return self.__user_id
    
    @property
    def name(self) -> str:
        """
        Accessor for the name attribute
        """               
        return self.__name
    
    @property
    def email(self) -> str:
        """
        Accessor for the email attribute
        """                
        return self.__email
    
    @property
    def borrower_status(self) -> BorrowerStatus:
        """
        Accessor for the borrower_status attribute
        """                
        return self.__borrower_status
    
    def __str__(self) -> str:
        """
        Returns
            str: A string to represent the format for the library user:
              user_id, name, email, borrower_status. 

        Example:
               User ID: 1244
               Name: Jackie Chan
               Email: 44@gmail.com
               Borrower Status: Active
        """
                
        return (f"User ID: {self.__user_id}"
            + f"\nName: {self.__name}"
            + f"\nEmail: {self.__email}"
            + f"\nBorrower Status: {self.__borrower_status.name.title()}")
    
    def borrow_item(self) -> str:
        """
        Accessor for the borrow_item attribute

        Returns
        """
        if self.__borrower_status is BorrowerStatus.DELINQUENT:
            raise ValueError(f"{self.__name} cannot borrow an item due to their {self.__borrower_status.name.title()} status.")
        else:
            return(f"{self.__name} is eligible to borrow the item")
        
    def return_item(self) -> str:
        """
        Accessor for the return_item attribute
        """
        
        if self.__borrower_status is BorrowerStatus.DELINQUENT:
                self.__borrower_status = BorrowerStatus.ACTIVE
                return (f"Item successfully returned. {self.__name} has returned the item, status now changed to: {self.__borrower_status.name.title()}")

        else:
            return(f"Item successfully returned")
        

    def borrow_item_approval(self, library_item:LibraryItem) -> str:

        """
        Checks to see if item is available and can be borrowed by user

        """    
        if self.__borrower_status != BorrowerStatus.DELINQUENT:
            if library_item.is_borrowed == False:
                return "The item is available to be borrowed."
        if self.__borrower_status != BorrowerStatus.DELINQUENT:
            if library_item.is_borrowed != False:
                raise Exception("The Item is not available to be borrowed.")
        if self.__borrower_status == BorrowerStatus.DELINQUENT:
            if library_item.is_borrowed == True:
                raise Exception("Item is not available due your status: DELINQUENT")
        if self.__borrower_status == BorrowerStatus.DELINQUENT:
            if library_item.is_borrowed == True:
                raise Exception("Cannot process request due to item not being available and your status: DELINQUENT")


