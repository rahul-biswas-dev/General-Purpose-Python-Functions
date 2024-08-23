# a function that takes a list and target parameters
# multiple variables : middle,start,end,steps
# recurtion or while loop
# increse steps each time split is done
# conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    try:
        while (start <= end):
            print("step", steps, ":", str(list[start:end + 1]))

            steps = steps + 1
            middle = (start + end) // 2

            if element == list[middle]:
                return middle

            if element < list[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return -1
    except:
        print(f"entered value {target} is not in the list")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = int(input("find:>"))
binary_search(my_list, target)
