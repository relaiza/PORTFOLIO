#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube

cubes = []
for number in range(1,11):
    cubes.append(number**3)
print(cubes)

