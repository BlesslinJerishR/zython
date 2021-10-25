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


def dupes_alt_0(l1):
    o = ""
    dupe = []
    if len(l1) <= 4:
        for x in l1:
            if(x in o):
                dupe.append(x)
                pass
            else:
                o = x + o + '0'
        print("The Origin : ",o,end="")
        print(o)
        # Bug
        return "The Origin : ",o,o
    else:
        print("[!BUGGU] --> Innu Kannu pudikala  , therinja enaku sollu kudu .")


# @test1
# n1 = list(input("Enter N1 : "))
# dupes_remover(n1)

# @test2
# n1 = list(input("Enter N1 : "))
# dupes_alt_0(n1)


