def pali(String):
    """Check an String as a Palindrome or Not ?
       # buy String
       # trade L:op
       # curl pali 
       
       > "".join()
       > reversed()
    """
     
    if String:
        print("I am a Palindrome")
    else:
        print("I am not a Palindrome")

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
    if String:
        print("I am a Palindrome")
    else:
        print("I am not a Palindrome")
        
    # return String.lower() == "".join(String[::-1]).lower()
    return String.lower() == "".join(reversed(String)).lower
