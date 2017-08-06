# This segment is just a chance for you to play around with 
# finding strings within strings.

print ("Example 1: Finding substrings in a string")
print ("test".find("te"))
print ("test".find("st"))
print ("test".find("t"))
#it will start counting from very first position and when the expression is found first it will return the position
print ("test"[2:])
#after counting t at first,now  finding second time t
print ("test".find("t",1))
#find("expression",nth time expression is occuring)
print ("testttt".find("t",2))
print ("testttt".find("t",6))
#it will return -1 as 5th time no t is present in the string

print ("Example 2: Finding substrings in a string which is stored as a variable")
my_string = "test"
print (my_string.find("te"))
print (my_string.find("st"))
print (my_string[2:])

print ("Example 3: Printing out everything after a certain substring")
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print (favorite_color) # oops, this line prints out 'color: ' as well...
print (favorite_color[7:]) # this fixes it!

print ("Example 4: Other interesting things about string.find()...")
print( "text".find("text")) # prints 0
print( "text".find("Text")) # prints -1
print( "text".find(""))     # prints 0
print ("text".find(" "))    # prints -1  
