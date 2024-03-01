import string


class Caesar:
    def __init__(self) -> None:
        
        self.__alphabet = string.ascii_lowercase


    def create_alphabet(self, shift: int, decrypt: bool = False) -> dict:
        
        shifted_alphabet = {}
        index = len(self.__alphabet) - shift

        for i in range(len(self.__alphabet)):
            shifted_alphabet[self.__alphabet[i]] = self.__alphabet[-index]
            index -= 1
        
        if decrypt:
            return dict(zip(shifted_alphabet.values(), shifted_alphabet.keys()))

        return shifted_alphabet


    def encrypt(self, plain_text: str, shift: int) -> str:
        encryption_alphabet = self.create_alphabet(shift)
        encrypted_text = ''

        for sym in plain_text:
            encrypted_text += encryption_alphabet[sym]

        return encrypted_text
    

    def decrypt(self, encrypted_text: str, shift: int) -> str:
        decryption_alphabet = self.create_alphabet(shift, decrypt=True)
        decrypted_text = ''

        for sym in encrypted_text:
            decrypted_text += decryption_alphabet[sym]

        return decrypted_text
