names = [""]
print(len(names))

food = ["pizza","pasta","rice","cake","burger"]
print(food[3])

print("4")

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
print(suitcase[5])

print(food[4])

print(suitcase[0:3])

sports = ['basketball', 'baseball', 'badminton', 'rugby', 'soccer']
print(sports[1:4])

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
vc = votes.count('Cassie')
print(vc)

countries = ['Canada','India','USA','Australia','Jamaica']
countries.sort()
print(countries)


def ulist():
    use = 'y'
    lst = []
    while use == 'y':
        t = input("Enter a list item ")
        lst.append(t)
        use = (input("Enter y to add another list item(y/n) "))
    else:
            print(t)

ulist()
    
