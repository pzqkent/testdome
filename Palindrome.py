class Palindrome:

    @staticmethod
    def is_palindrome(word):
        return word.lower()[::-1] == word.lower()

print(Palindrome.is_palindrome('Deleveled'))