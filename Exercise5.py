empty_list = []

lista_5 = ['Collar', 'lentes', 'arete', 'anillo', 'pulsera', 'bolsa']
print("Length:", len(lista_5))

print("First item:", lista_5[0])
print("Middle item:", lista_5[len(lista_5)//2])
print("Last item:", lista_5[-1])

mixed_data_types = ['Sebastián', 25, 1.83, 'Solito', 'Aguascalientes, México']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print("Number of companies:", len(it_companies))
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies)//2])
print("Last company:", it_companies[-1])

it_companies[1] = 'Alphabet'
print("Modified:", it_companies)

it_companies.append('Tesla')
print("After append:", it_companies)

middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Intel')
print("After insert:", it_companies)

it_companies = [company.upper() if company != 'IBM' else company for company in it_companies]
print("Uppercase names:", it_companies)

joined = '#; '.join(it_companies)
print("Joined string:", joined)

print("Is GOOGLE in list?", 'GOOGLE' in it_companies)

it_companies.sort()
print("Sorted:", it_companies)
it_companies.reverse()
print("Reversed:", it_companies)

print("First 3 companies:", it_companies[:3])
print("Last 3 companies:", it_companies[-3:])
mid = len(it_companies)//2
if len(it_companies) % 2 == 0:
    print("Middle companies:", it_companies[mid-1:mid+1])
else:
    print("Middle company:", it_companies[mid])

it_companies.pop(0)  
print("After removing first:", it_companies)
mid = len(it_companies)//2
it_companies.pop(mid) 
print("After removing middle:", it_companies)
it_companies.pop()  
print("After removing last:", it_companies)


it_companies.clear()
print("All removed:", it_companies)


del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print("Full Stack:", full_stack)

# Ejercicios 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Sorted ages:", ages)
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)
ages.extend([min_age, max_age])
print("Ages with min and max added:", ages)

ages.sort()
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print("Median age:", median_age)

average_age = sum(ages) / len(ages)
print("Average age:", average_age)

age_range = max_age - min_age
print("Age range:", age_range)

print("Distance min to avg:", abs(min_age - average_age))
print("Distance max to avg:", abs(max_age - average_age))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid = len(countries) // 2
if len(countries) % 2 == 0:
    print("Middle countries:", countries[mid-1:mid+1])
else:
    print("Middle country:", countries[mid])


if len(countries) % 2 == 0:
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    first_half = countries[:mid+1]
    second_half = countries[mid+1:]
print("First half:", first_half)
print("Second half:", second_half)


c1, c2, c3, *scandic_countries = countries
print("First three countries:", c1, c2, c3)
print("Scandic countries:", scandic_countries)