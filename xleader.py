def leader(times):
    gang = []
    print(f"Enter the {times} team members names : ")
    # Gang
    ids = 1
    for i in range(times):
        thug = int(input(f"Enter the power of Thug ids {ids} : "))
        ids += 1
        gang.append(thug)   
    leaders = []
    gangx = gang[1:]
    for i in gang:
        for j in gangx:
            if i > j:
                leaders.append(i)
            else:
                break
    leaders.append(gang.pop())
    print(list(set(leaders)))
    
# Diver Class
leader(5)