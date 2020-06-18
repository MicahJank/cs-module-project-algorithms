'''
Input: a List of integers
Returns: a List of integers
Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, 
then returns the altered array. 
The order of the non-zero integers does not matter in the mutated array.
'''

'''
UNDERSTAND


PLAN
- i could make two new empty arrays where i can store the values
- then i could loop over the array
- if the current number in the array is not a zero i could then append the number to the new array
- if the number is a zero i would append it to the other array
- after i have looped through the array i can merge to two arrays using the extends method
- then return the merged arr
'''

# EXECUTE
# def moving_zeroes(arr):
#     mutated_array = []
#     zeros = []

#     for num in arr:
#         if num != 0:
#             mutated_array.append(num)
#         else:
#             zeros.append(num)

#     mutated_array.extend(zeros)

#     return mutated_array

# SECOND PASS
# time complexity i think is now O(n) at the worse case - generally it should be lower, the only time it would be O(n) is 
#  when there are no zeroes in the array
# space complexity is O(1)
def moving_zeroes(arr):
    end_pointer = len(arr)-1
    start_pointer = 0
    while start_pointer < end_pointer:
        if arr[end_pointer] == 0:
            end_pointer -= 1

        if arr[start_pointer] == 0:
            arr[start_pointer], arr[end_pointer] = arr[end_pointer], arr[start_pointer]
            end_pointer -= 1

        start_pointer += 1
        # print("array status: ", arr)

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


'''
REFLECT
i believe the time complexity for this is O(n) since we are doing a for loop
since mutated_array is essentially a mutated copy of the original array then that must mean my space complexity is O(n) as well
- could try to find a way to get the space complexity down to O(1)
- how would i do this recursively?
'''