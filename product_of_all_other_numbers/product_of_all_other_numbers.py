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
-return the arr
'''
def product_of_all_other_numbers(arr):
    for i in range(len(arr)):
        for num in arr:
            if arr[i] != num:
                
                


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
