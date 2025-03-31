# Level 1

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and brothers
sisters = ("Ana", "María")
brothers = ("Carlos", "José")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
num_siblings = len(siblings)

# 5. Modify the siblings tuple and add the name of your father and mother
family_members = siblings + ("Papá", "Mamá")

# Level 2

# 1. Unpack siblings and parents from family_members
*siblings_unpacked, father, mother = family_members

# 2. Create fruits, vegetables and animal products tuples
fruits = ("Manzana", "Banana", "Fresa")
vegetables = ("Zanahoria", "Espinaca", "Lechuga")
animal_products = ("Leche", "Huevo", "Queso")

# Join the three tuples into food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from food_stuff_tp or food_stuff_lt
middle_index = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[middle_index - 1: middle_index + 1] if len(food_stuff_lt) % 2 == 0 else [food_stuff_lt[middle_index]]

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in a tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
is_estonia_nordic = "Estonia" in nordic_countries
is_iceland_nordic = "Iceland" in nordic_countries

# Output to confirm everything is working
print("Empty Tuple:", empty_tuple)
print("Siblings:", siblings)
print("Number of siblings:", num_siblings)
print("Family Members:", family_members)
print("Unpacked Siblings:", siblings_unpacked)
print("Father:", father)
print("Mother:", mother)
print("Food Stuff List:", food_stuff_lt)
print("Middle Items:", middle_items)
print("First Three Items:", first_three)
print("Last Three Items:", last_three)
print("Is Estonia a Nordic Country?", is_estonia_nordic)
print("Is Iceland a Nordic Country?", is_iceland_nordic)
