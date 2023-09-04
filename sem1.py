# a = int(input('Input your 1st number: '))
# b = int(input('Input your 2nd number: '))

# print((a+(b-1))//b) # you add the min not full number to make sure it rounds UP and not DOWN

# # another possible way

# print(((-a)//b) * -1) # rounds DOWN but with neg numbers it's what we need so we just change the polarity

# # add spaces around + and - but not around /or* lol - synthaxis 

# class1 = int(input('Input num of students in 1st class: '))
# class2 = int(input('Input num of students in 2nd class: '))
# class3 = int(input('Input num of students in 3rd class: '))

# table1 = int((class1 + 1)//2)
# table2 = int((class2 + 1)//2)
# table3 = int((class3 + 1)//2)

# print(table1 + table2 + table3)

# print((((-class1)//2) * -1) + (((-class2)//2) * -1) + (((-class3)//2) * -1))

year = int(input('Input the year: '))
# res = bool(0)

if (year%4 == 0 and year%100 != 0) or (year%400 == 0): 
    print("YES")
    # res = bool(1)
    # print(res, ", the year is высокосный")
else:
    print("NO")
    # print(res, ", the year is NOT высокосный")