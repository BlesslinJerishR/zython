def pali(String):
    """Check an String as a Palindrome or Not ?
       # buy String
       # trade L:op
       # curl pali 
       
       > "".join()
       > reversed()
    """
    # return String.lower() == "".join(String[::-1]).lower()
    return String.lower() == "".join(reversed(String)).lower
    

def shell_pali(String):
    """Check an Input String as a Palindrome or Not ?
       # get String
       # trade L:op
       # curl pali 
       
       > "".join()
       > reversed() 
    """
    String = str(input("Enter an Sting to check Palindorme Syndrome"))
    # return String.lower() == "".join(String[::-1]).lower()
    return String.lower() == "".join(reversed(String)).lower
