#!/Users/sreekanth_challa/python3
alphabets="abcdefghijklmnopqrstuvwxyz"
key=3
def encrypt(message):
    #alphabets="abcdefghijklmnopqrstuvwxyz"
    message=message.lower()
    #key=3
    e_message=""
    for character in message:
        if character in alphabets:
            index_of=alphabets.index(character)
            length_of=len(alphabets)
            new_index=(index_of+key)%length_of
            '''if new_index>length_of-1:
                new_index-=length_of'''
            e_message+=alphabets[new_index]
        else:
            e_message+=character
    return e_message  
def decrypt(e_message):
    d_message=""
    for i in e_message:
        index_of=alphabets.index(i)
        new_index=index_of-key
        d_message+=alphabets[new_index]
    return d_message
message=input("Enter a Message : ")
print("Encrypted Message is: {}".format(encrypt(message)))
opt=input("Do you want to Decrypt(y/n)?")
if opt.lower()=="y" or opt.lower()=="yes":
    print("Original Message is : {}".format(decrypt(encrypt(message))))

