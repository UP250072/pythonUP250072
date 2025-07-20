it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Samsung', 'Intel', 'Cisco'])
print(it_companies)

it_companies.remove('Intel')
print(it_companies)

# 5. What is the difference between remove and discard? La diferencia es que remove lanza un error si el elemento no existe, mientras que discard no lo hace, el remove se usa cuando se esta seguro de que el elemento existe, mientras que discard se usa cuando no se esta seguro.

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))

del A
del B

ages_set = set(age)
print("Length of list:", len(age))
print("Length of set:", len(ages_set))

print("List is bigger" if len(age) > len(ages_set) else "Set is bigger or equal")

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.replace(".", "").split()
unique_words = set(words)
print("Unique words:", len(unique_words))