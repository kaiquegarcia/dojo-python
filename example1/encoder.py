ENCODING_MAP = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

DECRYPTED_TEXT_WORD_SEPARATOR = " "
ENCRYPTED_TEXT_LETTER_SEPARATOR = " "
ENCRYPTED_TEXT_WORD_SEPARATOR = "/"

class MorseEncoder():
    def encode(self, decryptedText):
        txt = decryptedText.lower()
        words = txt.split(DECRYPTED_TEXT_WORD_SEPARATOR)
        encryptedWords = []
        for word in words:
            encryptedLetters = []
            for letter in word:
                encryptedLetters.append(ENCODING_MAP[letter])
            
            encryptedWords.append(ENCRYPTED_TEXT_LETTER_SEPARATOR.join(encryptedLetters))
        
        return ENCRYPTED_TEXT_WORD_SEPARATOR.join(encryptedWords)
            

    def decode(self, encryptedText):
        encryptedWords = encryptedText.split(ENCRYPTED_TEXT_WORD_SEPARATOR)
        words = []
        for encryptedWord in encryptedWords:
            encryptedLetters = encryptedWord.split(ENCRYPTED_TEXT_LETTER_SEPARATOR)
            word = ""
            for encryptedLetter in encryptedLetters:
                for letter, eLetter in ENCODING_MAP.items():
                    if eLetter == encryptedLetter:
                        word += letter
                        break
            words.append(word)
        return DECRYPTED_TEXT_WORD_SEPARATOR.join(words)