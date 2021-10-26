import collections

# Bro ... BUGGU Bruh ...

def confusioner(key, k):
    """Confusioner : Ngotha dei enakae ennanu terla daw !

    Args:
        key (str): [ Key .]
        k (int): [ N number of times ]
    """
    
    result = max_count = 0
    count = collections.Counter()
    for item in range(len(key)):
        count[key[item]] += 1
        max_count = max(max_count, count(key[item]))
        if result - max_count >= k:
            count[key[item-result]] -= 1
        else:
            result += 1
    return result

# @test1
# Edhukku ??