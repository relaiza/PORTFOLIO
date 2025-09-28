#ex 3.1
names = ['Benize', 'Chelsie', 'Keya', 'KC', 'Kriel']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4] + ".\n")

#ex 3.2
print("Hello ate " + names[0] + " you are such a reliable friend.")
print("Hello ate " + names[1] + " you are so fun to be with!")
print("Hello " + names[2] + "! I hope you well for your journey in Portsmouth university!")
print("Hellooooo baby " + names[3] + "!!! I love you so much!!")
print("Hello " + names[4] + "! I hope you all well for nursing!" + '.\n')

pizzas = ['pepporini', 'hawaian', 'cheese']

for pizza in pizzas:
    print(f' I like {pizza.title()} is and I enjoy eating it!')
print('I really like pizzas!'+ ".\n")

animals = ['dog', 'cat', 'fish']
for animal in animals:
    print(f'I think {animal} will be a great pet!')
print("any of this animals would make a great pet" + ".\n")

print("The first three items in the list are:")
print(names[:3])
print("\nThe items from the middle of the list are:")
print(names[1:4])
print("\nLast three items from the list are:")
print(names[-3:])

pizzas.append("deluxe")
friend_pizzas = pizzas.copy()
friend_pizzas.append('mighty meaty')

for pizza in pizzas:
    print("\nMy fabourite pizzas are:")
    print(pizzas)
    print("\nMy friend's favourite pizzas are:")
    print(friend_pizzas)






