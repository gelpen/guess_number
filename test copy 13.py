class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        self.my_answer = ''
        original_text.lower()
        for i in original_text.lower():
            if self.alphabet.find(i) < 0:
                self.my_answer += i
            else:
                self.my_answer += self.alphabet[(self.alphabet.find(i) +
                                                 shift) % len(self.alphabet)]
        return self.my_answer

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        self.my_answer = ''
        cipher_text.lower()
        for i in cipher_text.lower():
            if self.alphabet.find(i) < 0:
                self.my_answer += i
            else:
                self.my_answer += self.alphabet[(self.alphabet.find(i) -
                                                 shift) % len(self.alphabet)]

        return self.my_answer


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
