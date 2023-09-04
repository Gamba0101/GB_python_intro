
# single line comment
"""

multy line comment

"""
#
# to comment selected lines cmd + ?
"""
a = 8
b = 'hello'
c = 5.64

print(f"{a} - {b} - {c}")
print("{a} - {b} - {c}".format) 
"""

#print('Input your number: ')
#a1 = input()
#b1 = input('Input your second number: ')

c = 5.89
print(c)
print(type(c))
c = int(c)
print(c)
print(type(c))

# round (num, 3) - rounds up your number to only 3 characters after the .

# tabs are v important - they can cause an error 
# when writing algorythim add : at the end 
# if a < b: 
#   print(a-b)


# text.lower() - puts all letters in lower case
# text.upper() - puts all letters in UPPER case
# len(text) - gives back the lenght of the text in characters (outputs int)
# print('word' in text) - checks if there is 'word' in your text and outputs True or False (bool)
# text.replace('word', 'WORD') - replaces 'word' in your text to 'WORD'

# string can be counted as an array 
text = 'покушай пожалуйста'
print(text[0]) #will output  -   п

# len. - counts the length 
print(text[len(text)-1]) # will output  -   а

# indexing can start from the end if you add - to it
print(text[-1]) # will output  -   а
#index from the end start with -1 (not -0)

# : counts as 'all symbols'
print(text[:])
# but actually : works as "print from arg1 to arg2" where arg1:arg2
print(text[:3])
# if there is no argument it counts it as start:end
print(text[4:10])
# : is kind of like range
# you can also put neg index
print(text[2:-5]) # outputs   -   кушай пожал
# can have more than 2 elements
print(text[0:len(text):6]) #output every 6th element from text[0:len(text)]
print(text[::6]) #the same output as example above lol
#you can also add the string to make a monster uwu
text = text[:3] + text[4:10] + text[::6]
print(text) # ouput   -   покшай попйл 


# to add bibliotecs  import random