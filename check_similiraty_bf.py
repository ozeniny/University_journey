# This proggram check if two lists of numbers are similar or not similar.
# using built_in function.
from difflib import SequenceMatcher
def similar():
    user_list1 = input("Enter element of list separated with (,): ")
    user_list2 = input("Enter element of list separated with (,): ")
    list1 = user_list1.split(",")
    list2 = user_list2.split(",")
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    for i in range(len(list2)):
        list2[i] = int(list2[i])
    match = SequenceMatcher(None, list1, list2).ratio()
    if match == 1.0:
        print("Lists are = True")
    else:
        print("List are = False")
similar()