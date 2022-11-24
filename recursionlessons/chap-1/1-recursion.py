def count_down_and_up(number):
    print(number)

    if number == 0:
        # base case reached
        print("Reached base case.")
        return
    else:
        # recursive case
        count_down_and_up(number - 1)
        print(number, " returning")
        return

def diamond_shape(number):
    print('#' * number)

    if number == 0:
        print('reversed')
        return
    else:
        diamond_shape(number - 1)
        print('#' * number)
        return
#   ===============================

if __name__ == '__main__':

    num = int(input("Enter a number: "))
    count_down_and_up(num)
