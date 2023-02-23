"""Main Module"""
import string
from barcode import EAN13
from barcode.writer import ImageWriter
from UC3MLogistics import order_manager

# GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3


def Encode(word):
    """encode function"""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x_x = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x_x]
    return encoded

def Decode(word):
    """word function"""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x_x = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x_x]
    return encoded

def Main():
    """main function"""
    # successful test

    mng = order_manager()
    res = mng.read_product_code_from_json("test.json")
    str_res = str(res)
    print(str_res)
    encode_res = Encode(str_res)
    print("Encoded Res " + encode_res)
    decode_res = Decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("Codew: " + res.product_code)
    with open("./barcodeEan13.jpg", 'wb') as file:
        i_w = ImageWriter()
        EAN13(res.product_code, writer=i_w).write(file)

    '''
    # fail test
    res = mng.read_product_code_from_json("testFail.json")
    str_res = str(res)
    print(str_res)
    encode_res = Encode(str_res)
    print("Encoded Res " + encode_res)
    decode_res = Decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("Codew: " + res.product_code)
    with open("./barcodeEan13.jpg", 'wb') as file:
        i_w = ImageWriter()
        EAN13(res.product_code, writer=i_w).write(file)
'''

    # second successful test
    res = mng.read_product_code_from_json("testSuccess.json")
    str_res = str(res)
    print(str_res)
    encode_res = Encode(str_res)
    print("Encoded Res " + encode_res)
    decode_res = Decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("Codew: " + res.product_code)
    with open("./barcodeEan13.jpg", 'wb') as file:
        i_w = ImageWriter()
        EAN13(res.product_code, writer=i_w).write(file)


if __name__ == "__main__":
    Main()
