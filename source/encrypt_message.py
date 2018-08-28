#!/Users/sreekanth_challa/python3
#This programme will encrypt the message
alphabets="abcdefghijklmnopqrstuvwxyz"
#key=int(input("Enter Leavel of Encryption(1-9).Default=3 :"))
key=input("Enter Leavel of Encryption(1-9).Default=3 :")
if key is "":
   key=3
def encrypt(message):
    message=message.lower()
    e_message=""
    for character in message:
        if character in alphabets:
            index_of=alphabets.index(character)
            length_of=len(alphabets)
            new_index=(index_of+int(key))%length_of
            '''if new_index>length_of-1:
                new_index-=length_of'''
            e_message+=alphabets[new_index]
        else:
            e_message+=character
    return e_message
message=input("Enter a Message : ")
print("Encrypted Message is: {}".format(encrypt(message)))
