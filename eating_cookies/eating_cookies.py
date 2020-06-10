'''
Input: an integer
Returns: an integer

Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with n cookies inside of it, 
how many ways could he eat all n cookies in the cookie jar? Implement a function eating_cookies that counts the number of 
possible ways Cookie Monster can eat all of the cookies in the jar.

UNDERSTAND
- n is a number that represents how many cookies are in the jar

- 

PLAN
- if n represents the length of the list essentially that means i will need to recurse n times
- which means the base case would be when my counter reaches below 0 - ie there are no more cookies to eat
- 
'''
def eating_cookies(n):
    iterations = 0
    # what happens if there is only 1 item
    if n == 0:
        # i can return 1 because once n becomes 0 that means we have iterated through the cookies one time
        # 1 then will get added to the iterations at the next level up of the recursion tree
        return 1
    
    if n >= 1:
        cookies_left = n - 1
        iterations += eating_cookies(cookies_left)

    if n >= 2:
        cookies_left = n - 2
        iterations += eating_cookies(cookies_left)

    # if there are more than 3 cookies he has the ability to eat 3 cookies
    if n >= 3:
        # subtract the cookies he has eaten from the jar and then use recursion to check the cookie jar again
        cookies_left = n - 3
        iterations += eating_cookies(cookies_left)

    # the number of possible combinations
    return iterations


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
