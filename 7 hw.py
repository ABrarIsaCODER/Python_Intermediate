zodiac_elements = {"water": ["Cancer","Scorpio","Pisces"],"fire": ["Aries","Leo","Sagittarius"],"earth": ["Taurus","Virgo","Capricorn"],"air":["Gemini","Libra","Aquarius"]}
print(zodiac_elements['water'])

print(zodiac_elements['air'])

user_ids = {"superCoder": 103419,"pythonGuy": 182921,"samTheJavaMaam": 123112,"lyleLoop": 102931,"keysmithKeith": 129384}
t=user_ids.get("superCoder",100000)
print(t)

t1 = user_ids.get("fakeUser",100000)
print(t1)

fruits = {"apples": 10,"banana": 5,"berries": 20,"grapes": 25,"melon": 15,"pear": 30}
print(fruits.pop(20,"berries"))
print(fruits.pop(15,"melon"))

coding_languages = {"scratch": 10,"python": 13,"HTML": 15,"CSS": 22,"Java": 19,"C": 18,"Javascript": 18}
lessons=coding_languages.keys()
print(lessons)

total = coding_languages.values()
print(total)

Men_in_occupation = {"CEO": 28,"Engineering Manager": 9,"Pharmacist": 58,"Physician": 40,"Lawyer": 37,"Aerospace Engineer": 9}
for occupation,percentage in Men_in_occupation.items():
    print("Men make up "+str(percentage)+"percent of "+occupation + "s")




