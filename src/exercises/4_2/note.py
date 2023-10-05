"""Note module"""


class Note:
    """Note class"""

    def __init__(self, _id, url):
        self.id = _id
        self.url = url

    def describe(self):
        """Prints the id and url."""
        print(f"[{self.id}]({self.url})")


class TextNote(Note):
    def __init__(self, _id, url, text):
        super().__init__(_id, url)
        self.text = text

    def describe(self):
        """Print the id, url, and text."""
        print(f"[{self.id}]({self.url}) {self.text}")


class PhotoNote(Note):
    def __init__(self, _id, url, caption):
        super().__init__(_id, url)
        self.caption = caption

    def describe(self):
        """Print the id, url, and caption."""
        print(f'[{self.id}]({self.url}) "{self.caption}"')


text_note = TextNote(1128, "https://github.com/typinghare", "My GitHub Profile")
photo_note = PhotoNote(
    3306,
    "https://pbs.twimg.com/media/F7GY16FacAAMDUq?format=jpg&name=large",
    "Ogerpon is cute",
)

text_note.describe()
photo_note.describe()
