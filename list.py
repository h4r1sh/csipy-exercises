# Basic list exercises
# Fill in the definitions for the required functions. The main functions and the testing 
# has been handled, so when you run a program, you will get an output of how many testcases
# passed and how many didn't.

# A. alphanum Score
def alphanum_score(words):
	"""
	The function takes a list of words as its argument.
	Returns a score generated as follows,
		> Start with a net score of 0
		> If the element is a alpha-string, +1
		> If the element is a number, -1
	"""
        #Our score variable.
	score = 0

        #Iterating over the list
        for i in words:
                if i.isalpha(): #A method to check if the word contains only alphabets.
                        score += 1
                elif i.isdigit():#A method to check if the word contains only numbers.
                        score -= 1 
        
	return score


# B. Occurences
def occurences(words, letter):
	"""
	The function takes a list of words and a letter as its arguments.
	Returns a list sorted by the number of times the given letter occurs.
	"""

	# Add your code here
        
        #An empty list that holds the number of occurences for each word.
        times = []
        
        #Iterating over the list
        for i in words:
                times.append(i.count(letter)) #str.count(substr) is a method to find the occurences of a substring 'substr' in the string.
        
        times.sort()

	return times #Return a -sorted inplace- list.


# C. Tuple Merge
def function(tuples1, tuples2):
	"""
	The functions takes two lists of 2-tuples as its arguments.
	Returns a list of the form - 
		[tuples1 sorted by first element, tuples2 sorted by second element]
	"""
        # Add your code here
        
        #Main idea is to sort the tuples separately and concatenate them later.
        tuples1.sort() #Default argument is always the first element in a tuple.
        tuples2.sort(key = lambda x: x[1])
	
	return tuples1 + tuples2
        """ Alternate method:
            return sorted(tuples1, key = lambda x: x[0]) +  sorted(tuples2, key = lambda x: x[1])
        """

