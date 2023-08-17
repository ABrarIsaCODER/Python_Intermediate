print("2")

countries = ['spain','zimbabwe']
countries.extend(['Argentina'])
print(countries)

hobbies = ["tv","basketball"]
hobbies.extend(["Painting"])
print(hobbies)

food = ["butter chicken","shai paneer","chicken wings","pizza"]+["burger"]
food.insert(3,"burger")
print(food)

animals = ["dog","cat","bird","rhino"]
animals.insert(1,"hippo")
print(animals)

birds = ["robin","pigeon"]
birds.extend(["dove","eagle"])
print(birds)

num = ["69420","42069","02496"]
num.extend(["70","73","77"])
print(num)

cities = ["cleveland","calgary","california","toronto","new york"]
del cities[4]

nums = ["69420","42069","02496","35211"]
nums.pop(1)
print(nums)

things = ["watch","phone","clock","book"]
things.remove("book")
print(things)


