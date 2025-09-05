def encrypt(message, shift1, shift2):
    result = ""
    split_info = ""
    for char in message:
        if char.islower():
            idx = ord(char) - ord('a')
            if idx <= 12:
                shift = shift1 * shift2
                result += chr((idx + shift) % 26 + ord('a'))
                split_info += "0"
            else:
                shift = -(shift1 + shift2)
                result += chr((idx + shift) % 26 + ord('a'))
                split_info += "1"
        elif char.isupper():
            idx = ord(char) - ord('A')
            if idx <= 12:
                shift = -shift1
                result += chr((idx + shift) % 26 + ord('A'))
                split_info += "0"
            else:
                shift = shift2 ** 2
                result += chr((idx + shift) % 26 + ord('A'))
                split_info += "1"
        else:
            result += char
            split_info += "x"
    return result, split_info

def decrypt(message, shift1, shift2, split_info):
    result = ""
    for i, char in enumerate(message):
        if char.islower():
            if split_info[i] == "0":
                shift = -(shift1 * shift2)
            elif split_info[i] == "1":
                shift = (shift1 + shift2)
            else:
                shift = 0
            idx = ord(char) - ord('a')
            result += chr((idx + shift) % 26 + ord('a'))
        elif char.isupper():
            if split_info[i] == "0":
                shift = shift1
            elif split_info[i] == "1":
                shift = -(shift2 ** 2)
            else:
                shift = 0
            idx = ord(char) - ord('A')
            result += chr((idx + shift) % 26 + ord('A'))
        else:
            result += char
    return result


text = input("Enter your message: ")
shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

encrypted_text, split_info = encrypt(text, shift1, shift2)
print("Encrypted message:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift1, shift2, split_info)
print("Decrypted message:", decrypted_text)

if text == decrypted_text:
    print("Verification successful: The original and decrypted messages match.")
else:
    print("Verification failed: The original and decrypted messages do NOT match.")
