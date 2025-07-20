empty_tuple = ()

sis = ('Sam', 'Vania', 'Kiara')
bros = ('Tito', 'Santi')

siblings = sis + bros
print("Siblings:", siblings)

print("Number of siblings:", len(siblings))

family_members = siblings + ('María (Mamá)', 'José (Papá)')
print("Family members:", family_members)

*siblings, mother, father = family_members
print("Siblings:", siblings)
print("Mother:", mother)
print("Father:", father)

fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'lettuce', 'spinach')
animal_products = ('milk', 'cheese', 'eggs')

food_stuff_tp = fruits + vegetables + animal_products
print("Food tuple:", food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print("Food list:", food_stuff_lt)

mid = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    print("Middle items:", food_stuff_lt[mid-1:mid+1])
else:
    print("Middle item:", food_stuff_lt[mid])

print("First 3 items:", food_stuff_lt[:3])
print("Last 3 items:", food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Is 'Estonia' a Nordic country?", 'Estonia' in nordic_countries)
print("Is 'Iceland' a Nordic country?", 'Iceland' in nordic_countries)
