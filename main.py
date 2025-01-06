sentance=input("What do you sentance do you want to rainbonize:> ")
colors=['r','g']
for letter in sentance:
    if letter.lower()==colors[0]:#red
        print('\033[31m')
        
    elif letter.lower()==colors[1]:
        print('\033[32m')#green
    print(letter)