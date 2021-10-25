def lister(l1):
    """To view a List without comma & brackets .

    Args:
        L1 (List): Pass to view the List without comma & brackets
    """
    return print(*l1, sep="")


def listerx(l1):
    """To view a List without bracketx .

    Args:
        L1 (List): Pass to view the List without comma & brackets
    """
    return print(*l1, sep=",")


# @test0
# n1 = ['1','2']
# print(n1)
# @test1
# lister(n1)
# @test2
# listerx(n1)