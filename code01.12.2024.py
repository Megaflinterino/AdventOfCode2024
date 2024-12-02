#Creation of 2 empty lists a and b
a, b = [], []

#Opens the file with read properties as f and with makes sure the file is closed after
with open('inputs01.12.2024.txt', 'r') as f:
    #reads every line in the inpute and iterates it
    for lines in f.readlines():
        #The lines get split at spaces into x and y int(z) converts the numbers into integers
        x, y = (int(z) for z in lines.split())
        #The values x and y get appended to the Lists a and b
        a.append(x)
        b.append(y)


#sorts the lists
a.sort()
b.sort()

#prints the list to make sure everything is alright
print(a)
print(b)

#The avsolute(so no value is negative) difference of every values gets added for i in range is used to iterate over every value len(a) or len(b) is irrelevant
print(sum(abs(a[i]-b[i]) for i in range(len(a))))