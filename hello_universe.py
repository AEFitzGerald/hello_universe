
print("Hello Universe!")    # 1.  print "Hello World"

name = "Noelle" # 2. print "Hello Noelle!" with the name in a variable

print("Hello", name,"!")	# 2. with a comma

print("Hello " + "Noelle!"  )	# 2. with a +

name = 42  # 3. print "Hello 42!" with the number in a variable

print( "Hello", name,"!")	# 3.  with a comma

print( "Hello " + "42!")	# 3. with a +	-- this one should give us an error!

fave_food1 = "sushi" # 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food2 = "pizza"
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string
print('I love to eat {} and {}.'.format(fave_food1, fave_food2)) # 4. with .format()