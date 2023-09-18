# My favorite foods; "马蹄肉饼" is for testing non-ASCII characters
foods = ['chicken wing', 'brocoli', 'tofu', 'meat floss cake', 'croissant',
         '马蹄肉饼']

# Print each item in foods
for food in foods:
    print(food, end='  ')
print('\n')

# Print some foods
print(foods[0: 2])  # Print the first two elements
print(foods[1: -1])  # Print all elements except the first and the last one
print(foods[-3: -1])  # Print the second to last and third to last
# Sort and print the foods list;
# non-ASCII characters are greater than ord('z')
# ord('马') = 39352
foods.sort()
print('\nSorted list: ', foods)

# Store upper case version of foods in a new list and print it out;
# non-ASCII characters remain the same
foods_upper = [food.upper() for food in foods]
print('\nUppercase list: ', foods_upper)
