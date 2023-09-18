# Exercise 2_1

# 5
name = "james chan"
age = 24

print(f'My name is {name.title()} and I am {age} years old.')

# 7
places_to_visit = ['Tokyo', 'Paris', 'California', 'Seattle', 'Moscow']

print('The zeroth element: ' + places_to_visit[0])
print('The last element: ' + places_to_visit[-1])
places_to_visit.sort()

for place in places_to_visit:
    print(f'I want to go to {place}.')
