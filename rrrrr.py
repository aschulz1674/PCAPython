def remove_sort_reverse(my_list):
    # perform operations on `my_list` to 
    # 1. remove all "eggplant"s
    # 2. sort it
    # 3. reverse it!
    y = len(my_list)
    for i in my_list:
        if i == "eggplant":
            my_list.remove(i)
    my_list.sort(reverse = True)
    return my_list
pe = ["eggplant","poo","pee","tee","eggplant","a","c","b","eggplant"]
remove_sort_reverse(pe)