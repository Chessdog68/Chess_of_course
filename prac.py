
# Write a Python function called `is_even` that takes an integer as an argument
# and returns True if the number is even, and False if the number is odd.

# Write a Python function called `factorial` that takes a non-negative integer as an argument
# and returns the factorial of that number.
# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# The factorial of 0 is 1 by definition.


# The first two numbers in the sequence are 0 and 1.
# The next number in the sequence is the sum of the previous two numbers.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
         return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))  # Should return 8 (0, 1, 1, 2, 3, 5, 8)



def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            n = n*i
        return n

# Test cases
print(factorial(6))  # Should return 120 (5 * 4 * 3 * 2 * 1)



s = "hello"

def reverse_string(s):
    # Your code here
    return s[::-1]

# Test cases
print(reverse_string("hello"))  # Should return "olleh"





number = 27
 

def is_even(number):

    if number % 2 == 0:
        return True
    # Your code here
   

# Test cases
print(is_even(4))  # Should return True
print(is_even(7))  # Should return False


#print(longest_unique_substring("abcabcbb"))  # Output: "abc"
#print(longest_unique_substring("bbbbb"))    # Output: "b"
#print(longest_unique_substring("pwwkew"))   # Output: "wke"
#print(longest_unique_substring("abcd"))     # Output: "abcd"
#print(longest_unique_substring(""))         # Output: ""

s = ("abcabcbbl")
print(s)
l = sorted(s)
print(l)
print(enumerate(l))


def longest_unique_substring(s: str) -> str:

    if not s:
        return ""
    start = 0
    max_len = 0
    max_start = 0   
    used_char = {}

    for i, c in enumerate(s):
        print(i, c)
        if c in used_char and start <= used_char[c]:
            start = used_char[c] + 1
        else:
            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_start = start
        used_char[c] = i

    return s[max_start:max_start + max_len]

print(longest_unique_substring(s))