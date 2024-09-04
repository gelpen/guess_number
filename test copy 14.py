class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        if is_encrypt is True:
            self.my_answer = ''
            for i in text.lower():
                if self.alphabet.find(i) < 0:
                    self.my_answer += i
                else:
                    self.my_answer += self.alphabet[(self.alphabet.find(i) +
                                                     shift) % len(self.alphabet)]
            return self.my_answer
        else:
            self.my_answer = ''
            for i in text.lower():
                if self.alphabet.find(i) < 0:
                    self.my_answer += i
                else:
                    self.my_answer += self.alphabet[(self.alphabet.find(i) -
                                                     shift) % len(self.alphabet)]

            return self.my_answer


# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
