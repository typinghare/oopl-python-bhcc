james = {
    "userID": "1128",
    "firstName": "James",
    "lastName": "Chan",
    "email": "jameschan312.cn@gmail.com",
}

andrew = {
    "userID": "1641",
    "firstName": "Andrew",
    "lastName": "Mo",
    "email": "andrew.mo@uiuc.edu",
}

howland = {
    "userID": "2109",
    "firstName": "Howland",
    "lastName": "Liu",
    "email": "howland.liu@bhcc.edu",
}

users = {
    "james": james,
    "andrew": andrew,
    "howland": howland,
}

# Print all three users
for username, user_info in users.items():
    print(
        f'User({user_info["userID"]}): first name = "{user_info["firstName"]}"; '
        f'last name = "{user_info["lastName"]}"; email = "{user_info["email"]}")'
    )
