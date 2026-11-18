dimensions = (200, 50)
print("Original dimensions:")

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")

for dimension in dimensions:
    print(dimension)

##2 code

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

##3 code

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())