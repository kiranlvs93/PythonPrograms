class CaesarCipher(object):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, inp):
        self.name = inp.lower()

    def encrypt(self, rotate_by_int):
        encrypted = ""
        for ch in self.name:
            if ch not in CaesarCipher.alphabets:
                encrypted += ch
            else:
                encrypted += chr(ord(ch) + rotate_by_int)
        print("Encrypted:", encrypted)

    def decrypt(self, rotate_by_int):
        decrypted = ""
        for ch in self.name:
            if ch not in CaesarCipher.alphabets:
                decrypted += ch
            else:
                decrypted += chr(ord(ch) - rotate_by_int)
        print("Decrypted:", decrypted)

    def encrypt_by_shift(self, rotate_by_int):
        shift_encrypt = ""
        for ch in self.name:
            if ch not in CaesarCipher.alphabets:
                shift_encrypt += ch
            else:
                shift_no = CaesarCipher.alphabets.find(ch) + rotate_by_int
                shift_no = shift_no % 26
                shift_encrypt += CaesarCipher.alphabets[shift_no]
        print("Shift encrypted::", shift_encrypt)

    def decrypt_by_shift(self, rotate_by_int):
        shift_decrypt = ""
        for ch in self.name:
            if ch not in CaesarCipher.alphabets:
                shift_decrypt += ch
            else:
                shift_no = CaesarCipher.alphabets.find(ch) - rotate_by_int
                shift_no = shift_no % 26
                shift_decrypt += CaesarCipher.alphabets[shift_no]
        print("Shift decrypted::", shift_decrypt)


if __name__ == '__main__':
    enc_str1 = '''I confess at these words a shudder passed
through me. There was a thrill in the doctor’s voice
which showed that he was himself deeply moved
by that which he told us. Holmes leaned forward
in his excitement and his eyes had the hard, dry
glitter which shot from them when he was keenly
interested.'''

    dec_str1 = '''s myxpocc kd droco gybnc k crennob zkccon
drbyeqr wo. drobo gkc k drbsvv sx dro nymdyb’c fysmo
grsmr crygon drkd ro gkc rswcovp noozvi wyfon
li drkd grsmr ro dyvn ec. ryvwoc vokxon pybgkbn
sx rsc ohmsdowoxd kxn rsc oioc rkn dro rkbn, nbi
qvsddob grsmr cryd pbyw drow grox ro gkc uooxvi
sxdobocdon.'''

    enc_str2 = 'The cat sat on the mat'
    dec_str2 = 'esp nle dle zy esp xle'

    a = CaesarCipher(dec_str2)
    shift_by = 11
    # a.encrypt(shift_by)
    # a.decrypt(shift_by)
    # a.encrypt_by_shift(shift_by)
    a.decrypt_by_shift(shift_by)
