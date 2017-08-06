# Given the definition of s below

s = 'audacity'

#Sub-Indexing works as <string>[<start>:<stop>]
#the region lying between this will be printed

print(s[:])
#Output is audacity
#it will print whole string

print(s[1:1])
#Output is nothing
#it will print nothing because between this region no alphabet or say string is present.

print(s[1:])
#Output is udacity
#it will print whole string from 1st index position

print(s[1:6])
#Output is udaci
#it will print string from 1st index position to 6th index position

print(s[:1])
#Output is 'a'
#it will print as being on :right-side it will stop till that position

 
print ('U' + s[2:8])
#It prints out Udacity (with a capital U)

print(s[:-1])
#Output is audacit
#it will print audacit leaving y as due to -ve sign it will start reading from backward
#and also being on :right-side it will stop till that position

print(s[2:-1])
#Output is dacit
#it will print dacit as being start from 2 it will start from d
#and due to -ve sign it will start reading from backward
# it will stop till that :right-side  position
