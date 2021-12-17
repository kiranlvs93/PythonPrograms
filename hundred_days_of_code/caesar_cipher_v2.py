logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabets = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

print(logo)


def encode_decode(enc_dec, msg, shift_by):
    encode = True if enc_dec == 'encode' else False
    cipher_text = ""
    # For decode, we need to go in negative direction
    if not encode:
        shift_by *= -1
    for ch in msg:
        # If the character is not in the alphabet list, we'll not shift it but simply append it
        if ch not in alphabets:
            cipher_text += ch
        else:
            pos = alphabets.index(ch)
            new_position = pos + shift_by
            cipher_text += alphabets[new_position]
    print(f"Here is the {enc_dec}d result::{cipher_text}")


# Continue until the user enters 'no'
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt::")
    text = input("Type your message::").lower()
    # %26 is necessary if the shift is >26 as the number of alphabets is only 26
    shift = int(input("Type the shift number::")) % 26
    encode_decode(direction, text, shift)
    print("***************************************************")
    if input("Type 'yes' if you want to go again else type 'no'::").lower() == 'no':
        print("GOOD BYE!!")
        break
