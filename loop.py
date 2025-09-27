#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube

cubes = []
for number in range(1,11):
    cubes.append(number**3)
print(cubes)

#ex 3.1
names = ['Benize', 'Chelsie', 'Keya', 'KC', 'Kriel']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#ex 3.2
print("Hello ate " + names[0] + " you are such a reliable friend.")
print("Hello ate " + names[1] + " you are so fun to be with!")
print("Hello " + names[2] + "! I hope you well for your journey in Portsmouth university!")
print("Hellooooo baby " + names[3] + "!!! I love you so much!!")
print("Hello " + names[4] + "! I hope you all well for nursing!")
