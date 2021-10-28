from typing import Any
import string

def binarySearch(array: list, lower: int, upper: int, num: Any) -> int:
    index = -1
    if upper >= lower:
        mid = (lower + upper) // 2
        if array[mid] == num:
            index = mid
        elif array[mid] > num:
            index = binarySearch(array, lower, mid-1, num)
        else:
            index = binarySearch(array, mid + 1, upper, num)
    return index

def test_num_list(array: list, start: int, stop: int, step: int) -> None:
    for i in range(start, stop, step):
        print("Find num: ", i,", Index: ", binarySearch(array, 0, len(array)-1, i))

def test_chars_list(array: list, start: int, step: int) -> None:
    lowercase = string.ascii_lowercase
    for i in range(start, len(lowercase), step):
        print("Find char: ", lowercase[i],", Index: ", binarySearch(array, 0, len(array)-1, lowercase[i]))

def fill_list_nums(array: list, start: int, stop: int, step: int) -> None:
    for i in range(start, stop, step):
        array.append(i)

def fill_list_chars(array: list, start: int, step: int) -> None:
    lowercase = string.ascii_lowercase
    for i in range(start, len(lowercase), step):
        array.append(lowercase[i])

def main():
    l = []
    
    fill_list_nums(l, 0, 20, 4)
    print(l)
    test_num_list(l, -10, 31, 1)
    l.clear()

    fill_list_chars(l,0,3)
    print(l)
    test_chars_list(l,0,1)

if __name__ == "__main__":
    main()