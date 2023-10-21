class RansomNote:
    """
    Ransom Note Class.
    """

    def can_construct(self, ransom_note, magazine):
        """
        Returns true if the ransome_note can be constructed
        from magazine.
        """

        a = ord("a")  # The ASCII index of the letter 'a'

        # Find the number of each letter in <ransom_note>
        map1 = [0] * 26
        for c in ransom_note:
            map1[ord(c) - a] += 1

        # Find the number of each letter in <magazine>
        map2 = [0] * 26
        for c in magazine:
            map2[ord(c) - a] += 1

        print(map1)
        print(map2)

        for i in range(0, 26):
            if map2[i] < map1[i]:
                return False

        return True


note = RansomNote()
print(note.can_construct("a", "b"))  # false
print(note.can_construct("aa", "bb"))  # false
print(note.can_construct("aa", "aab"))  # true
print(note.can_construct("aa", "a"))  # false
print(note.can_construct("ca", "abc"))  # true
