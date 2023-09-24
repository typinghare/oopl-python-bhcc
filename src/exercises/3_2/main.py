import amazon

some_books = [
    {
        "title": "The Varieties of Scientific Experience",
        "author": "Carl Sagan",
        "price": 25.9,
    },
    {"title": "A Short History of Europe", "author": "Simon Jenkins", "price": 49.9},
]

amazon.checkout(some_books)
