##animals = ["dog","cat","monkey"]
##print(animals)
##
##colors = ["black","red","yellow","blue","pink"]
##print(colors)
##
##grades = [97,62,85,93]
##print(grades[0])
##print(grades[1])
##print(grades[3])
##
##grades = [97,62,85,93]
##print(grades[99])
##
##grades = [97,62,85,93]
##grades.append(42)
##print(grades)
##
##animals = ["dog","cat","monkey"]
##animals.append(37)
##print(animals)
##
##grades = [97,62,85,93]
##grades.insert(2,77)
##print(grades)
##
##animals = ["dog","cat","monkey"]
##animals.insert(1,37)
##print(animals)
##
##animals = ["dog","cat","monkey"]
##animals.insert(2,"giraffe")
##print(animals)
##
##grades = [97,62,85,93]+[90,77]
##print(grades)
##
##animals = ["dog","cat","monkey"] + ["giraffe","duck"]
##print(animals)
##
##grades = [97,62,85,93]
##grades.extend([82,77])
##print(grades)
##
##animals = ["dog","cat","monkey"]
##animals.extend(["giraffe","duck"])
##print(animals)
##
##grades = [97,62,85,93]
##del grades[0]
##print(grades)
##
##animals = ["dog","cat","monkey"]
##del animals[2]
##print(animals)
##
##

##grades = [97,62,85,93]
##grades.pop(3)
##print(grades)

##
##animals = ["dog","cat","monkey","dog"]
##animals.pop(0)
##print(animals)

##
##grades = [97,62,93,85,93]
##grades.remove(93)
##print(grades)
##
##animals = ["dog","cat","dog","monkey"]
##animals.remove("dog")
##print(animals)

##
##grades = [97,62,93,85,93]
##grades.remove(56)
##print(grades)
##
##animals = ["dog","cat","dog","monkey"]
##animals.remove("duck")
##print(animals)

def LIST():
    use = 'y'
    lst=[]
    while use == 'y':
        t = input("enter ur list item")
        lst.append(t)
        use = input("enter y to add a item and n to stop(y/n)")
    else:
        print(lst)
    
LIST()
