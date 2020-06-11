import math
'''
Input: a List of integers
Returns: a List of integers
Write a function that receives an array of integers and returns an array 
consisting of the product of all numbers in the array except the number at that index.

UNDERSTAND
- when doing the calculation i need to exclude the currend index number from the calculation
- i will assume that arr will not be empty

PLAN
- loop over the array
- do a double loop and multiply all the items in the list together
- after multiplying all items together divide it by the number at the current index
- assign that new number to the index in the arr
- 
-return the arr

UPDATE
- loop through the array twice and assign the value of all the numbers multiplied together to a new array
- then you loop through the new array and divide each value in the array by its corresponding value in the first array
- assign the new value to the position at that index

UPDATE UPDATE
- can use math.prod to multiply all the items in the list together
after that i can loop over the array and divide the values by their counterpart
'''
def product_of_all_other_numbers(arr):
    no_zeroes = [num for num in arr if num != 0]
    no_zero_num = math.prod(no_zeroes)
    num = math.prod(arr)
    prod_arr = [num] * len(arr)

    for i in range(len(arr)):
        
        if arr[i] == 0:
            arr[i] = no_zero_num
        else:
            arr[i] = prod_arr[i] // arr[i]

    return arr
                


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [0, 2, 3, 0, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


'''
REFLECT
- this implementation does not work if there is more than 1 zero in the array
- i was able to get the time complexity to O(n) but space complexity is also O(n)
- could try to find a way to get the time complexity to O(1)
'''