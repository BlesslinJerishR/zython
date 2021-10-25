def dupes_remover(l1):
    """To Remove Duplicates in the List

    Args:
        L1 (List): Pass the List who should be burned .
    """
    o = ""
    for x in l1:
        if(x in o):
            pass
        else:
            o = o+x
    print("The Origin : ",o)
    return "The Origin : ",o


# @test1
n1 = list(input("Enter N1 : "))
dupes_remover(n1)