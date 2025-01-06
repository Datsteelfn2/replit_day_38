sentance=input("What do you sentance do you want to rainbonize:> ")
colors=['r','g','b','p','y',' ']
for letter in sentance:
    if letter.lower()==colors[0]:#red
        print('\033[31m',end='')
        
    elif letter.lower()==colors[1]:
        print('\033[32m',end='')#green
    elif letter.lower()==colors[2]:
        print('\033[34m',end='')#blue
    elif letter==colors[3]:
        print('\033[93m',end ='')#yellow
    elif letter.lower()==colors[4]:
        print('\033[35m',end='')#putple
    elif letter.lower()==colors[5]:
        print('\033[0m',end='')#space
    print(letter,end='')