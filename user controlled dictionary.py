def ucondict():
    use = 'y'
    ucd = {}
    while use =='y':
        key = input("Enter a key for the dictionary")
        value = input("Enter a value in numbers, for your key in the dictionary")
        ucd[key]=value
        use = input("Enter y to continue and n to stop(y/n)")
    print(ucd)
        
ucondict()
    
