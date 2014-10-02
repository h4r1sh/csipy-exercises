# Basic string exercises
# Fill in the definitions for the required functions. The main functions and the testing 
# has been handled, so when you run a program, you will get an output of how many testcases
# passed and how many didn't.


# A. Odd Rotation
def odd_rotation(number, word):
	"""
	The function takes a number and a word as its arguments. 
	If the number is even, return the first three characters of the string.
	If the number is odd, return a word formed by a concatenation of the last 2 letters 
	and the first 2 letters of the word.
	For example,
	odd_rotation(2, 'apple') -> 'app'
	odd_rotation(5, 'cabbage') -> 'geca'
	"""

	# Add your code here
        
        #Simple slicing. Remember, str[:n] gives you all letters from 0 to n-1.
        if number % 2 == 0: #Even
                return word[:3] 
        else:
                #New variable to find the index of the last but second letter.
                st = len(word) - 2
                return word[st:] + word[:2]


# B. Flip Case
def flip_case(word):
	"""
	The function takes a word as its argument.
	Return a word that has all lowercase characters swapped to uppercase and vice versa.
	"""
        
	# Add your code here
	return word.swapcase()


# C. And/Or ?
def and_or(word):
	"""
	The function takes a word as its argument.
	If the word starts with 'a', return the index where the substring 'and' appears.
	Otherwise, if the word ends with 'r', return the index where the substring 'or' appears. 
	"""

        #assumed to return -1 upon an unsuccessful find().
        if word.startswith('a'):
                return word.find('and')
        elif word.endswith('r'):
                return word.find('or')
	return -1


# D. sin + cos
def sincos(number):
	"""
	The function takes a number as its argument.
	Return a string formed by taking the first 5 characters of the result of the expression - 
		sin(number) + cos(number)

	HINT : Look into the math module in more detail
	"""

	# Add your code here
        
	return



