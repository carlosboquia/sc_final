""""
Description: A class to manage User objects.
Edited by: Carlos Boquia
Date: August 30 2024
"""
from borrower_status.borrower_status import BorrowerStatus
from email_validator import validate_email, EmailNotValidError

class LibraryUser():
    """
    Represents the status of library user

    Attributes:

    
    
    """

    def __init__(self, user_id:int, name:str, email:str, borrower_status: BorrowerStatus):

        
        if user_id <= 99:
            raise ValueError("Invalid User ID: must be greater than 99")
        elif not isinstance(user_id, int):
            raise ValueError("User ID must be numeric")
        else:
            self.__user_id = user_id

        if len(name.strip()) == 0:
            self.__name = name
        else:
            raise ValueError("Name cannot be blank")
        
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
        return self.__user_id
    
    def name(self) -> str:
        return self.__name
    
    def email(self) -> str:
        return self.__email
    
    def borrower_status(self) -> BorrowerStatus:
        return self.__borrower_status
    
    def __str__(self) -> str:
        return (f"User ID: {self.__user_id}"
            + f"\nName: {self.__name}"
            + f"\nEmail: {self.__email}"
            + f"\nBorrower Status: {self.__item_id.name.replace('_',' ').title()}")
    
    def borrow_item(borrower_status:BorrowerStatus, name:str) -> str:
        if borrower_status is BorrowerStatus.DELINQUENT:
            raise ValueError("f{name} cannot borrow an item due to their {borrower_status}.")
        else:
            return(f"{name} is eliigble to borrow the item")
        
    def return_item(borrower_status:BorrowerStatus, name:str) -> str:
        if borrower_status is BorrowerStatus.ACTIVE:
            return (f"{name} has returned the item, status now changed to {borrower_status}")
        else:
            return(f"Item successfully returned")
        

