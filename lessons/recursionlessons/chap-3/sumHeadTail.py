#!/usr/bin/python3

def sum(numbers):
    
    if len(numbers) == 0:   # 0 is the base case
        return 0

    else:   # the recursive case
        head = numbers[0]
        tail = numbers[1:]

        return head + sum(tail)


#   =====================================

if __name__ == '__main__':

    nums = [1, 2, 3, 4, 5]
    print("Sum of {}: {}".format(nums, sum(nums)))

    nums1 = [5, 2, 4, 8]
    print("Sum of {}: {}".format(nums1, sum(nums1)))

    nums2 = [1, 10, 100, 1000]
    print("Sum of {}: {}".format(nums2, sum(nums2)))
