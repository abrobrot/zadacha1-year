#18. Написать функцию XOR_cipher, принимающая 2 аргумента: строку,
# которую нужно зашифровать, и ключ шифрования, которая возвращает строку,
# зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.

def XOR_cipher(text: str, key: int) -> str:
    encrypted_text = ""
    for char in text:
        encrypted_char = chr(ord(char) ^ key)
        encrypted_text += encrypted_char
    return encrypted_text


#def XOR_uncipher(encrypted_text: str, key: int) -> str:
#    return XOR_cipher(encrypted_text, key)  # XOR обратим, используем ту же функцию

def XOR_uncipher(text: str, key: int) -> str:
    uncrypted_text = ""
    for char in text:
        uncrypted_char = chr(ord(char) ^ key)
        uncrypted_text += uncrypted_char
    return uncrypted_text

if __name__ == "__main__":
    original_text = "Hello, World!"
    key = 42


encrypted_text = XOR_cipher(original_text, key)
print(f"Зашифрованный текст: {encrypted_text}")


decrypted_text = XOR_uncipher(encrypted_text, key)
print(f"Расшифрованный текст: {decrypted_text}")
#text = "Hello, World!"
#key = 5
#XOR_uncipher(text, key)