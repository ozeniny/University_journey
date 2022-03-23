# This proggram check if two lists of numbers are similar or not similar.
# Whithout built_in function.
def similar():
    user_list1 = input("Enter element of list separated with (,): ")
    user_list2 = input("Enter element of list separated with (,): ")
    list1 = user_list1.split(",")
    list2 = user_list2.split(",")
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    for i in range(len(list2)):
        list2[i] = int(list2[i])
    for element in list1:
        if element in list2:
            continue
        else:
            print("Lists are = False")
            quit()
    print("Lists are = True")


similar()