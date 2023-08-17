##building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,"Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
##building_heights["Burj Khalifa"]
##building_heights["Ping An"]
##building_heights.get("Shanghai Tower")
##building_heights.get("My House")
##building_heights.get('Mt Olympus', 0)
##
##raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket",412123: "Necklace", 298787: "Pasta Maker"}
##raffle.pop(320291, "No Prize")
##{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "PastMaker"}
##raffle.pop(100000, "No Prize")
##{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "PastaMaker"}
##raffle.pop(872921, "No Prize")
##{223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}
##
##test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84],"Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
##list(test_scores)
##print(list)
##["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
##
##test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84],"Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
##for score_listin test_scores.values():
##    print(score_list)

zodiac_elements = {"water": ["Cancer","Scorpio","Pisces"],"fire": ["Aries","Leo","Sagittarius"],"earth": ["Taurus","Virgo","Capricorn"],"air":["Gemini","Libra","Aquarius"]}
print(zodiac_elements['earth'])

print(zodiac_elements['fire'])

user_ids = {"teraCoder": 100019,"pythonGuy": 182921,"samTheJavaMaam": 123112,"lyleLoop": 102931,"keysmithKeith": 129384}
t=user_ids.get("teraCoder",100000)
print(t)

t1 = user_ids.get("superStackSmash",100000)
print(t1)

available_items = {"health potion": 10,"cake of the cure": 5,"green elixir": 20,"strengthsandwich": 25,"stamina grains": 15,"power stew": 30}
print(available_items.pop(30,"powerstew"))
print(available_items.pop(15,"stamina grains"))

num_exercises = {"functions": 10,"syntax": 13,"control flow": 15,"loops": 22,"lists": 19,"classes": 18,"dictionaries": 18}
lessons=num_exercises.keys()
print(lessons)

num_exercises = {"functions": 10,"syntax": 13,"control flow": 15,"loops": 22,"lists": 19,"classes": 18,"dictionaries": 18}
total=num_exercises.values()
print(total)

women_in_occupation = {"CEO": 28,"Engineering Manager": 9,"Pharmacist": 58,"Physician": 40,"Lawyer": 37,"Aerospace Engineer": 9}
for occupation,percentage in women_in_occupation.items():
    print("Women make up "+str(percentage)+"percent of "+occupation + "s")
