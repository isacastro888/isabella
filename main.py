#The D.E.A (Dice Encryption Algprithm)
# input : str
# output : str

plaintext = input('Enter message you wish to encrypt. It must be between 3 to 100 characters: ')
#Use title and replace functions to get rid of all the spaces in the message, and capitalize firs letter of each word to distinguish
plaintext = plaintext.title()
plaintext = plaintext.replace(" ", "")
print(plaintext)
#create a list to put in alphabet values (1-26) of each letter in plaintext
letter_to_value = []
found_error = 'false'
#make sure message satisfies restrictions before continuing:
# - has to be min. 3 characters and max. 100
# - cannot contain symbols
if len(plaintext) < 3 or len(plaintext) > 100 or not str.isalpha(plaintext):
  found_error = 'true'
  print("Message must be between 3 and 100 characters, and cannot contain symbols")
 
else:
 
   ## Get ascii values of letters in plaintext and add to an empty list
   letters_ascii_vals = []
   for i in range(len(plaintext)):
       ascii_val = ord(plaintext[i])
       letters_ascii_vals.append(ascii_val)
   print(letters_ascii_vals)     
    
 
   #loop over each individual character of plaintext
   for i in range(len(plaintext)):
       #Find ascii value using ord function, deduct 96 in order to make equivalent
       #to alphabet values    
       alph_val = ord(plaintext[i]) - 96
       #add the alphabet value of the designated character to the list
       letter_to_value.append(alph_val)
   print(letter_to_value)
 
   # Simulate dice rolls
   import random as r
   designated_dices = []
   dice_rolls = []
   #for messages between 3 and 20
   if len(plaintext) >= 3 and len(plaintext) <= 20:
       dice_1 = r.randint(1,6)
       dice_2 = r.randint(1,6)
       dice_3 = r.randint(1,6)
       dice_rolls.append(dice_1)
       dice_rolls.append(dice_2)
       dice_rolls.append(dice_3) 
       #Create a dice list the lenght of the plaintext, using the values given by the random operator
       import math
       extend_repeats = len(plaintext) / 3
       extend_repeats = math.ceil(extend_repeats)
       for i in range(extend_repeats):
           designated_dices.extend(dice_rolls)     
       print(designated_dices)  
      
        
   else:
     #for messages between 21 and 50 characters
     if len(plaintext) >= 21 and len(plaintext) <= 50:
       dice_1 = r.randint(1,6)
       dice_2 = r.randint(1,6)
       dice_3 = r.randint(1,6)
       dice_4 = r.randint(1,6)
       dice_rolls.append(dice_1)
       dice_rolls.append(dice_2)
       dice_rolls.append(dice_3)
       dice_rolls.append(dice_4)
       import math
       extend_repeats = len(plaintext) / 4
       extend_repeats = math.ceil(extend_repeats)
       for i in range(extend_repeats):
           designated_dices.extend(dice_rolls)     
           print(designated_dices)
          
     else:
         #for messages between 51 and 100 characters
         if len(plaintext) >= 51 and len(plaintext) <= 100:
               dice_1 = r.randint(1,6)
               dice_2 = r.randint(1,6)
               dice_3 = r.randint(1,6)
               dice_4 = r.randint(1,6)
               dice_5 = r.randint(1,6)
               dice_rolls.append(dice_1)
               dice_rolls.append(dice_2)
               dice_rolls.append(dice_3)
               dice_rolls.append(dice_4)
               dice_rolls.append(dice_5)
               import math
               extend_repeats = len(plaintext) / 5
               extend_repeats = math.ceil(extend_repeats)
               for i in range(extend_repeats):
                 designated_dices.extend(dice_rolls)        
               print(designated_dices)
 
   #Create a new value for each character by altering the ascii values with the dice rolls
   new_values = []
   #reiterate through ascii values and designated dice roll at the same time
   for i in range(len(plaintext)):
     #determine wether values added are odd or even to determine how the ascii value will be altered
       if letters_ascii_vals[i] + designated_dices[i] % 2 == 0:
         #even = adding designated dice value 
           new_val = letters_ascii_vals[i] + designated_dices[i]
       else:
         #odd = subtracting designated dice value
           new_val = letters_ascii_vals[i] - designated_dices[i]
       new_values.append(new_val)     
   print(new_values)
    
     # Create a cipher_value list, values which will be used to encrypt the mesasge
    
   cipher_values = []
   for i in range(len(plaintext)):
     #assure all values are positive
       if letter_to_value[i] < 0:
         letter_to_value[i] = letter_to_value[i] * -1
       #Alter new values by subtracting the initial alphabet value to create our cipher value
       cipher_val = new_values[i] - letter_to_value[i]
       cipher_values.append(cipher_val)
   print(cipher_values)

   # create ciphertext by assigning deignated character to each value, according according to ascii table
   cipher_text = []
   for i in range(len(plaintext)):
     l = chr(cipher_values[i])
     cipher_text.append(l)
   print(cipher_text)

   #convert from a list, into a string
   encrypted_message = ''
   for i in range(len(plaintext)):
     encrypted_message = encrypted_message + cipher_text[i]
 
   print('Your encypted message is: ' + encrypted_message)
  
  ### DECRYPTIONNNNNNNNNNN
 
   encrypted_messagee = input('Enter message you wish to decrypt: ')
   
   #convert characters into its designated ascii values
   cipher_characters = []
   for i in range(len(encrypted_message)):
     cipher_char = ord(encrypted_message[i])
     cipher_characters.append(cipher_char)
   print(cipher_characters)
 
   #inverse the last altering step by adding back the alphabet values
   decrypt_new_values = []
   for i in range(len(cipher_text)):
     de_new_val = cipher_characters[i] + letter_to_value[i]
     decrypt_new_values.append(de_new_val)
   print(decrypt_new_values)
 
   #akcnowledge the keystream = the dice rolls used to encrypt the message
   key_stream = [designated_dices]
 
   # inverse function
   dice_decr_values = []
   for i in range(len(cipher_text)):
     dices_decr = decrypt_new_values[i] + designated_dices[i]
     dice_decr_values.append(dices_decr)
   print(dice_decr_values)
 
   # Assign character to each designated decripted ascii value
 
   decrypted_text = []
   for i in range(len(dice_decr_values)):
     c = chr(dice_decr_values[i])
     decrypted_text.append(c)
   print(decrypted_text)
 
   #put list of decripted characters into a string
 
   decrypted_message = ''
   for i in range(len(decrypted_text)):
     decrypted_message = decrypted_message + decrypted_text[i]
   print('Your decrypted message is: ' + decrypted_message)