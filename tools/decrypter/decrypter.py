import sys   
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from urllib.parse import quote_plus


iv = "1234567890123456".encode('utf-8')
key = "583dc269d3e8e93f3c4501c60a6d16b0"


def encrypt(data, key, iv):
    """
    Input raw data to encrypt, returns encrypted bytes, using iv and key
    """
    data = pad(data.encode(), 16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    encoded = base64.b64encode(cipher.encrypt(data))
    return(quote_plus(encoded.decode('UTF-8').rstrip("=")))
    # return encoded

def decrypt(enc, key, iv):
    """
    Input encrypted bytes, return decrypted bytes, using iv and key
    """
    enc = base64.b64decode(enc + "======")
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc), 16).decode('UTF-8')

def main():
    do_encrypt = False
    if sys.argv[1] == "encrypt":
        do_encrypt = True

    if do_encrypt:
        try: 
            if len(sys.argv)  >= 3:                
                if sys.argv[2] == "vin":
                    print(encrypt(sys.argv[3], key, iv) + "%3D%0A")
            else:
                print(encrypt(sys.argv[2], key, iv))
        except:
            pass

    else:
        print(decrypt(sys.argv[2], key, iv))

main()
