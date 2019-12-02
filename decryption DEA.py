keystream_dice = input("Enter The Keystream Dice With No Brackets: ")
keystream_dice = keystream_dice.replace(" ", "")
keystream_dice = [int(x) for x in keystream_dice.split(',')]

keystream_alpha = input("Enter The Keystream Alpha With No Brackets: ")
keystream_alpha = keystream_alpha.replace(" ", "")
keystream_alpha = [int(x) for x in keystream_alpha.split(',')]

encrypted_messagee = input('Enter message you wish to decrypt: ')
cipher_characters = []
for i in range(len(encrypted_messagee)):
     cipher_char = ord(encrypted_messagee[i])
     cipher_characters.append(cipher_char)
print(cipher_characters)

decrypt_new_values = []
for i in range(len(encrypted_messagee)):
     de_new_val = cipher_characters[i] + keystream_alpha[i]
     decrypt_new_values.append(de_new_val)
print(decrypt_new_values)

#akcnowledge the keystream = the dice rolls used to encrypt the message
### inverse
dice_decr_values = []
for i in range(len(encrypted_messagee)):
     dices_decr = decrypt_new_values[i] + keystream_dice[i]
     dice_decr_values.append(dices_decr)
print(dice_decr_values)

# Assing character to each designated decripted ascii value

decrypted_text = []
for i in range(len(dice_decr_values)):
     c = chr(dice_decr_values[i])
     decrypted_text.append(c)
print(decrypted_text)

#put list of decripted characters into a string

decrypted_message = ''
for i in range(len(decrypted_text)):
     decrypted_message = decrypted_message + decrypted_text[i]
print(decrypted_message)