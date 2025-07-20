#1
str_a = 'Thirty'
str_b = 'Days'
str_c = 'Of'
str_d = 'Python'
space = ' '
str_com = str_a + space + str_b + space + str_c + space + str_d
print(str_com)
#2
str_1 = 'Coding'
str_2 = 'For'
str_3 = 'All'
str_com2 = str_1 + space + str_2 + space + str_3
print(str_com2)
#3
company = 'Coding For All'
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[7:])
#10
print(company.index('Coding'))
#11
print(company.replace('Coding', 'Python'))
#12
replac = 'Python for Everyone'
print(replac.replace('Everyone', 'All'))
#13
print(company.split())
#14
social = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(social.split(', '))
#15-17
print(company[0])
print(company[-1])
print(company[10])
#18
all = 'Python For Everyone'
acr = ''.join([word[0] for word in all.split()])
print(acr)

cfa= 'Coding For All'
acr = ''.join([word[0] for word in cfa.split()])
print(acr)

print(company.index('C'))
print(company.index('F'))

people = "Coding For All People"
print(people.rfind('l'))

yce = 'You cannot end a sentence with because because because is a conjunction'
print(yce.find('because'))
print(yce.rindex('because'))
print(yce[31:54])

print(company.startswith('Coding'))

print(company.endswith('coding'))

cfa2 = '   Coding For All      '
print(cfa2.strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


radio = 10
area = 3.14 * radio ** 2
print("El area de un circulo con radio {} es {:.0f}".format(radio, area))

a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))