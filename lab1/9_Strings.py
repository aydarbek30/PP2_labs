#STRINGS
print("Sup")
print('Sup')

#QUOTES INSIDE QUOTES
print("Vse norm")
print("Ego zovut 'Aida'")
print('Ego zovut "Aibek"')

#ASSIGN STRING TO A VARIABLES
a = "Chao"
print(a)

#MULTILINE STRINGS
a = """ Chao sdasfdsfs fsdfsadf  sdf asf  """
print(a)

a = ''' Chao sdasfdsfs fsdfsadf  sdf asf '''
print(a)

#STRINGS ARE ARRAYS
a = "PRIVET"
print(a[1])

#LOOPING
for x in "apple":
  print(x)

#STRING LENGTH
a = "PRIVET VSEM"
print(len(a))

#CHECK STRING
txt = "che tam rebyata"
print("che" in txt)

txt = "che tam rebyata"
if "che" in txt:
  print("Da, 'che' est.")

#CHECK IF NOT
txt = "che tam rebyata"
print("che" in txt)

txt = "che tam rebyata"
if "ches" not in txt:
  print("Net, 'ches' est.")




#SLICING
a = "Hello, Pacani!"
print(a[2:5])

a = "Hello, Pacani!"
print(a[:5])

a = "Hello, Pacani!"
print(a[2:])

b = "Hello, Pacani!"
print(b[-6:-2])




#UPPER CASE
a = "Hello, Pacani!"
print(a.upper())

#LOWER CASE
a = "Hello, Pacani!"
print(a.lower())

#UBIRAET PROBELI
a = " Hello, Pacani! "
print(a.strip()) # vidast "Hello, Pacani!"

#REPLACE STRING
a = "Hello, Pacani!"
print(a.replace("P", "H"))

#SPLIT STRING
a = "Hello, Pacani!"
print(a.split(",")) # vidast ['Hello', ' Pacani!']




#STRING CONCATENATION
a = "Hello"
b = "Pacani"
c = a + " " + b
print(c)




#STRING FORMAT F-STRINGS
age = 22
txt = f"My name is Aida, I am {age}"
print(txt)

#PLACEHOLDERS AND MODIFIERS
price = 69
txt = f"The price is {price:.2f} tenge"
print(txt)

txt = f"The price is {11 * 11} tenge"
print(txt)




#ESCAPE CHARACTERS
txt = "We are the so-called \"kyrgyz\" from the SOUTH."
#\'	Single Quote
#\\	Backslash
#\n	New Line
#\r	Carriage Return
#\t	Tab
#\b	Backspace
#\f	Form Feed
#\ooo	Octal value
#\xhh	Hex value




#STRING METHODS
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isascii()	Returns True if all characters in the string are ascii characters
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning











