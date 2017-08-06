# Defining a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


def biggest(a, b, c):
    largest=a
    if(largest<b):
        largest=b
    if(largest<c):
        largest=c
    return largest  
    


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9
