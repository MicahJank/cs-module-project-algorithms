'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
'''
UNDERSTAND
- need to find the number in the arr that shows up only once
- must do it in one pass
- must have space complexity of O(1)

PLAN
--BRUTE FORCE--
- double for loop the arr twice comparing each number to see if they match
- if they match that means the number is not single
- if i get through the entire array without finding a matching number that means it is single
- return that number
------------------------
- UPDATE
- if i sort the array first then i can just compare the first index to the second index
- have 2 pointers 1 pointing at the first index and the second pointing at the second index
- compare the numbers if they are the same then that number is not unique so i can then increase both pointers by 2
- for loop can increment by 2 each time since i know there are only going to be at most 2 of each number

'''
# EXECUTE
def single_number(arr):
    arr.sort()
    for i in range(0, len(arr), 2):
        pointerA = arr[i]
        pointerB = arr[i+1]

        if pointerA != pointerB:
            return pointerA


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


'''
REFLECT
I believe the time complexity for the current version is O(n/2) since i am incrementing by 2 and not 1
The space complexity is at O(1) in the current implementation i believe because the variables i have declared will take up the same
amount of space regardless of how big arr is

I could try to do this recursively and see how to make it work

since i am using a sort first i am not doing it in 1 pass i dont think? - how could i accomplish this without doing the sort first then?
'''