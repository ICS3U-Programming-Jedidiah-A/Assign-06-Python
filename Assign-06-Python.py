# !/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 28, 2021
# This program asks the user to enter 2 lists of different elements.

def merged_list(list_a, list_b):
    merged_list = []
    for i in range(len(list_a)):
        merged_list.append(list_a[i])
        merged_list.append(list_b[i])
    return merged_list


def main():
    first_list = input("Enter the elements you want in the list: ")
    second_list = input("Enter the elements of the second list: ")
    print("List a is:", first_list)
    print("List b is:", second_list)
    joined_list = merged_list(first_list, second_list)
    final_list = ",".join(joined_list)
    print(final_list)


if __name__ == "__main__":
    main()
