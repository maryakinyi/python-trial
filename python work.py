# function add marks
marks = [21, 34, 45, 65, 78, 88]
marks_sum = sum(marks)
print("the total_mark is:", marks_sum)
# finding length.
length = len(marks)
print("length is:", length)

# finding average marks

average_marks = marks_sum/len(marks)
print("my average marks is:", average_marks)

# finding a remainder

remainder = marks_sum % len(marks)
print("the remainder is:", remainder)

# indexing
m = [1, 2, 3, 4, 5]
print(m[1])
print(m[-2])
print(m[0])

# slicing
print(m[1:3])
print(m[:-3])
print(m[2:])

# length of the string
length = len(m)
print(length)

# listing of strings
# combining lists
text = "I like reading"
text2 = "and enjoys it in a quite place"
result = text+text2
print(result)

# using escaping strings
text = "I love reading"
print("I love \n reading")
print("I love \t reading")
print("I love \v reading")
print("I love \b reading")

# capitalize,upper,lower,tittle
k = "I love reading"
print(k.capitalize())
print(k.lower())

