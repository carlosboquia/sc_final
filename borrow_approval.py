from borrower_status.borrower_status import BorrowerStatus


def borrow_item_approval(user, library_item) -> str:

        """
        Checks to see if item is available and can be borrowed by user

        """    
        if user.borrower_status != BorrowerStatus.DELINQUENT:
            if library_item.is_borrowed == False:
                return "The item is available to be borrowed."
        if user.borrower_status == BorrowerStatus.DELINQUENT:
            if library_item.is_borrowed == False:
                raise Exception("Item is not available due your status: DELINQUENT")
        if user.borrower_status != BorrowerStatus.DELINQUENT:
            if library_item.is_borrowed == True:
                raise Exception("The Item is not available to be borrowed.")
        if user.borrower_status == BorrowerStatus.DELINQUENT:
            if library_item.is_borrowed == True:
                raise Exception("Cannot process request due to item not being available and your status: DELINQUENT")


