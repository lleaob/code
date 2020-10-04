'''print("big">"small")

print(11%5)

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

print(((10 >= 5*2) and (10 <= 5*2)))

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n+=1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
'''
#Question 2 Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.
'''
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
'''

#Question 3 The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers. Note: Try running your function with the number 0 as the input, and see what you get!
'''
def is_power_of_two(n):
	# Check if the number can be divided by two without a remainder
	while n % 2 == 0 and n !=0:
		n = n / 2
	# If after dividing by two the number is 1, it's a power of two
	if n == 1:
		return True
	elif n  == 0:
		return False
  
	return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
'''
'''
#Question 4 Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.
def sum_divisors(n):
  sum = 0
  denominator = 1
  # Return the sum of all divisors of n, not including n
  for denominator in range(1,n):
	  if n % denominator == 0:
		  sum += denominator

  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
'''

#Question 5 The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. An additional requirement is that the result is not to exceed 25, which is done with the break statement. Fill in the blanks to complete the function to satisfy these conditions.
'''
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24
'''

#The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:
'''
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return ( n + sum_positive_numbers(n-1))

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
'''

'''
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
'''
#Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
'''
def first_and_last(message):
    if message != "":
        if message[0] == message[-1]:
            return True
    else: return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
'''
#Try using the index method yourself now! Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".
'''
word = "supercalifragilisticexpialidocious"
print(word.index('x'))
'''
#Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
'''
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
'''
#Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
'''
def student_grade(name, grade):
	return "{} received {} on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
'''
#Question 1 The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
'''
def is_palindrome(input_string):
  # We'll create two strings, to compare them
  new_string = ""
  reverse_string = ""
  # Traverse through each letter of the input string
  for letter in input_string.lower():
    # Add any non-blank letters to the 
    # end of one string, and to the front
    # of the other string. 
    if letter != " ":
      new_string = new_string + letter
      reverse_string = letter + reverse_string
  # Compare the strings
  #print(new_string + "\n" + reverse_string)
  if new_string == reverse_string:
    return True
  return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
'''
#Question 2 Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
'''
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
'''
'''
Weather = "Rainfall"
print(Weather[:4])
'''
'''
def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 
'''
#Question 5
#The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).
'''
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.count(old) != 0:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence.rfind(old)
		#print (i)
		new_sentence = sentence[:i] + new + sentence[i+len(old):]
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
'''
'''
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence
	if sentence.split(" ")[-1] == old:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence.rfind(old)
		#print (i)
		new_sentence = sentence[:i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
'''
#The skip_elements function returns a list containing every other element from an input list, starting with the first element. Complete this function to do that, using the for loop to iterate through the input list.
'''
def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for element in range(0,len(elements)):
		# Does this element belong in the resulting list?
		if i <= len(elements):
			# Add this element to the resulting list
			new_list.append(elements[i])
		# Increment i
		i =  i+2
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
'''
#Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
'''
def file_size(file_info):
	name, type, size = file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
'''

#Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.
'''
def skip_elements(elements):
	# code goes here
	new_list = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
'''
'''
#return "name <email>" from a tuple
def full_email(people):
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name, email))
	return result

print(full_email([("lleaob@gmail.com","Leonardo Braga")]))
'''
'''
def odd_numbers(n):
	return [x for x in range(1, n+1, 2)]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
'''
'''
def mdc(a, b):
	list_a = [a]
	list_b = [b]
	list_primes = []
	dc = 1
	for n in range(2,max(a,b)):
		while a%n == 0 and b%n == 0:
			list_a.append(a/n)
			list_b.append(b/n)
			list_primes.append(n)
			a = a/n
			b = b/n
			dc = dc * n
	#for i in n: i = i*n
	return list_primes , dc

print(mdc(2000,200))
'''
