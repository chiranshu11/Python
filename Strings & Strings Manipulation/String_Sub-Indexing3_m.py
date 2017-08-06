# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# Here's a spy yourself and want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever print any alias,
# the values for each alias will point to the string "Mary"

mary = "Mary"
#code goes here
gabriel = "Gabriel"
kathleen = "Kathleen"
salwa = "Salwa"
katie = "Katie"
randa = "Randa"



# In South America, the alias Kathleen is known as the alias Gabriel, this means that:
gabriel = kathleen
randa = mary
katie = randa
salwa = katie
kathleen = salwa
gabriel = kathleen
# Testing to see if all of these variables will print out the string "Mary"
print gabriel
print kathleen
print salwa
print katie
print randa
print mary
