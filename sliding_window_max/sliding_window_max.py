'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

Given an array of integers, there is a sliding window of size k which is moving from the left side of the array to the right, one element at a time. 
You can only interact with the k numbers in the window. Return an array consisting of the maximum value of each window of elements.


UNDERSTAND
- k is the number of elements in the array i can interact with at any given iteration
- k - 1 would give me the last index in the window i can interact with
- i need pointers pointing at the first element i can interact with in the window as well as the last
- what if k is bigger than the length of the arr?
    -- i will assume in that case that i interact with every item in the arr
- what if k is 0?
    -- 


PLAN
- create an empty array where i can store the maximum values of the window elements
- create pointer variables for the first index nums in the range of k that i can interact with
    -- k_end  remember k - 1 will give me the end index that i need
    -- k_start  zero would be where you start intitially for the first index
- do a while loop that checks if k_end != len(arr)
    - do a for loop that loops in the range of k
    - in that loop create a max value variable and assign it the the initial index value
    - check the value at the current index in the loop
    - if value is greater than the max value - reassign the max value to the value at the index
    - after the loop has completed the max value variable should have the largest value
    - append the max value variable to the empty array created at the beginning

    - outside but under the for loop i can increment the k_end and k_start variables and then let the while loop repeat

'''

# EXECUTE
# def sliding_window_max(nums, k):
#     max_values = []
#     k_start = 0
#     k_end = k-1

#     while k_end != len(nums):

#         max_value = nums[k_start]
#         for i in range(k_start, k_end+1):
#             if nums[i] > max_value:
#                 max_value = nums[i]
#             # print(nums[i])

#         max_values.append(max_value)

#         k_end += 1
#         k_start += 1

#     return max_values

# SECOND PASS
def sliding_window_max(nums, k):
    max_values = []
    k_start = 0
    k_end = k-1

    k_counter = k

    


    # while k_end != len(nums):

    #     max_value = nums[k_start]
    #     for i in range(k_start, k_end+1):
    #         if nums[i] > max_value:
    #             max_value = nums[i]
    #         # print(nums[i])

    #     max_values.append(max_value)

    #     k_end += 1
    #     k_start += 1

    return max_values

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")


'''
REFLECT
looks like the time complexity for this is O(n^2) - there is probably a way this could be optimized - i should try and see if i can do it in 1 loop instead of 2

'''