alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caeser(text,shift,direction):
    crypted_text = ""
    if direction == "decode":
        shift*=-1    
    for i in text:
        if i in alphabet:
            ind = alphabet.index(i)
            new_ind = ind + shift
            crypt_list = alphabet[new_ind]
            crypted_text += crypt_list
        else:
            crypted_text += i
    print(f"The {direction}ed text is ",crypted_text)

repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # If the user enters a large shift number
    caeser(text,shift,direction)
    user = input("Do you want to start it again? Yes or No").lower()
    if user == "no":
        repeat = False