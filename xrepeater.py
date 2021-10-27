def repeater(word):
    """Repeater - Find the first repeated word .

    Args:
        word (str): [ Enter the word that you want to generate
                      The first repeated word]

    Returns:
        [str]: [unix]
    """
    garage_0 = []

    for char in word:
        garage_0.append(char)

    garage_1 = set()
    unix = []

    for z in garage_0:
        if z not in unix:
            unix.append(z)
            garage_1.add(z)

    print("I am first repeater in my family ", unix[0])
    print(unix)
    return unix[0]

def repeater2(word):
    garage_0 = [x for x in word]
    garage_1 = set()
    unix = []
    l_uniq = [x for x in garage_0 if x not in unix or garage_1.add(x) ]
    print("I am first repeater in my family : ",l_uniq[0])
    
# Driver Class
repeater("apple")



