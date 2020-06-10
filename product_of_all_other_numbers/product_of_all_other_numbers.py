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

TODO - cant figure this out will need to come back to it
'''
def product_of_all_other_numbers(arr):
    new_arr = arr.copy()
    for i in range(len(arr)):
        for j in range(len(new_arr)):
            if i != j:
                new_arr[i] *= arr[j]

    print(new_arr)
    for i in range(len(arr)):
        if new_arr[i] == 0:
            arr[i] = 0
        else:
            arr[i] = new_arr[i] // arr[i]

    return arr
                


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
