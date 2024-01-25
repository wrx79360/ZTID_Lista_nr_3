#Lista nr 3
#Zad 1
#Filip Kuś 85992
import base64


def encode_and_decode(text):
    # Konwersja tekstu na bajty
    text_bytes = text.encode('ascii')
    # Szyfrowanie base64
    encoded_string = base64.b64encode(text_bytes).decode('ascii')
    # Odszyfrowanie base64
    decoded_string = base64.b64decode(encoded_string).decode('ascii')

    return encoded_string, decoded_string


input_string = "Lista nr3"
result_encode, result_decode = encode_and_decode(input_string)

print(f'Text to encrypt {input_string}')
print(f'Text encoded {result_encode}')
print(f'Text decoded {result_decode}')
