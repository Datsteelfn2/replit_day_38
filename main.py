sentance=input("What do you sentance do you want to rainbonize:> ")
colors=['r','g',' ']
for letter in sentance:
    if letter.lower()==colors[0]:#red
        print('\033[31m',end='')
        
    elif letter.lower()==colors[1]:
        print('\033[32m',end='')#green
    elif letter==colors[2]:
        print('\033[0m',end ='')
    print(letter,end='')