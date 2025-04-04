# Исправленный шифратор

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if 'А' <= char <= 'Я':
            shift_start = ord('А')
            result += chr((ord(char) - shift_start + shift) % 32 + shift_start)
        elif 'а' <= char <= 'я':
            shift_start = ord('а')
            result += chr((ord(char) - shift_start + shift) % 32 + shift_start)
        elif char == 'Ё':
            shift_yo = (ord('Е') - ord('А') + shift) % 32 + ord('А')
            result += chr(shift_yo if shift_yo != ord('Ж') else ord('Ё'))
        elif char == 'ё':
            shift_yo = (ord('е') - ord('а') + shift) % 32 + ord('а')
            result += chr(shift_yo if shift_yo != ord('ж') else ord('ё'))
        else:
            result += char
    return result

text_to_encode = "Гнгзиплв ЫГЖ тскзугеових хидв ф ргфхцтгбьлп рсеюп жсзсп!"
shift_value = 0
encoded_message = caesar_cipher(text_to_encode, shift_value)
print(f"Закодированное сообщение: {encoded_message}")

# Дешифратор

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

decoded_message = caesar_decipher(encoded_message, shift_value)
print(f"Расшифрованное сообщение: {decoded_message}")



print("zzzzzz")