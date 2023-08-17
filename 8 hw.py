##with open('8 hw.py') as cool_doc:
##    cool_contents = cool_doc.read()
##    print(cool_contents)
##with open('generated_file.txt', 'w') as gen_file:
##    gen_file.write("What an incredible file!")
##with open('generated_file.txt', 'a') as gen_file:
##    gen_file.write("... and it still is")

##with open('welcome.txt') as text_file:
##    text_data = text_file.read()
##    print(text_data)


with open('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

with open('bad_bands.txt', 'w') as bad_bands_doc:
    bad_bands_doc.write('The Eagles')


with open('cool_dogs.txt', 'a') as cool_dogs_file:
    cool_dogs_file.write("Air Buddy")
