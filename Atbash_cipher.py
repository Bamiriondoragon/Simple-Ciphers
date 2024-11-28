alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reversed_alphabet = alphabet[::-1]
# input text

passage = input("Text to encrypt ")
print("encrypting")
char = list(passage)

# encrypting
encrypted_text = ""

for c in char:
    if c in alphabet:  # Check if the character is a letter
        index = alphabet.index(c)  # Find the index in the original alphabet
        encrypted_text += reversed_alphabet[index]  # Replace with reverse letter
    else:
        encrypted_text += c  # If not a letter, keep the character as is
        
print("Encrypted text: " + encrypted_text)