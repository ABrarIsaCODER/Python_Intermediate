dict1 = {}
with open('new_clean_data.txt') as clean_data:
    for clean_text in clean_data.readlines():
##        print(clean_text
        temp = clean_text.strip(',')
        dict1[temp] = clean_text
    print(dict1)
