import datetime
import Main


def test_ECB(PATH_TEXT):

    chose = input("1 - cipher, 2 - decipher:   ")
    if chose == "1":

        start_time = datetime.datetime.now()
        Main.cipher_ECB(PATH_TEXT, PATH_KEY, PATH_ENCRY_FILE)
        end_time = datetime.datetime.now()
        print("Время шифрации = ", (end_time - start_time))
    elif chose == "2":
        start_time = datetime.datetime.now()
        Main.decipher_ECB(PATH_ENCRY_FILE, PATH_KEY, PATH_DECRYPT_FILE)
        end_time = datetime.datetime.now()
        print("Время дешифрации = ", (end_time - start_time))


def test_CBC(PATH_TEXT):
    chose = input("1 - cipher, 2 - decipher:   ")
    if chose == "1":
        start_time = datetime.datetime.now()
        Main.cipher_CBC(PATH_TEXT, PATH_KEY, PATH_ENCRY_FILE)
        end_time = datetime.datetime.now()
        print("Время шифрации = ", (end_time - start_time))
    elif chose == "2":
        start_time = datetime.datetime.now()
        Main.decipher_CBC(PATH_ENCRY_FILE, PATH_KEY, PATH_DECRYPT_FILE)
        end_time = datetime.datetime.now()
        print("Время дешифрации = ", (end_time - start_time))


def test_PCBC(PATH_TEXT):
    chose = input("1 - cipher, 2 - decipher:   ")
    if chose == "1":
        start_time = datetime.datetime.now()
        Main.cipher_PCBC(PATH_TEXT, PATH_KEY, PATH_ENCRY_FILE)
        end_time = datetime.datetime.now()
        print("Время шифрации = ", (end_time - start_time))
    elif chose == "2":
        start_time = datetime.datetime.now()
        Main.decipher_PCBC(PATH_ENCRY_FILE, PATH_KEY, PATH_DECRYPT_FILE)
        end_time = datetime.datetime.now()
        print("Время дешифрации = ", (end_time - start_time))


if __name__ == '__main__':
    PATH_KEY = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_key.txt"
    PATH_ENCRY_FILE = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/encry_text.txt"
    PATH_DECRYPT_FILE = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/decrypt_text.txt"
    chose_cipher_mode = input("1 - ECB, 2 - CBC, 3 - PCBC:  ")
    if chose_cipher_mode == '1':
        chose = input("1 - 1 блок, 2 = 1000 блоков, 3 - 100000 блоков :    ")
        if chose == '1':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_1.txt"
            test_ECB(PATH_TEXT)
        elif chose == '2':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_1k.txt"
            test_ECB(PATH_TEXT)
        elif chose == '3':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_100k.txt"
            test_ECB(PATH_TEXT)

    elif chose_cipher_mode == '2':
        chose = input("1 - 1 МБ, 2 - 10 МБ, 3 - 100 МБ :   ")
        if chose == '1':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_1MB.txt"
            test_CBC(PATH_TEXT)
        elif chose == '2':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_10MB.txt"
            test_CBC(PATH_TEXT)
        elif chose == '3':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_100MB.txt"
            test_CBC(PATH_TEXT)
    elif chose_cipher_mode == '3':
        chose = input("1 - 1 МБ, 2 - 10 МБ, 3 - 100 МБ :   ")
        if chose == '1':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_1MB.txt"
            test_PCBC(PATH_TEXT)
        elif chose == '2':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_10MB.txt"
            test_PCBC(PATH_TEXT)
        elif chose == '3':
            PATH_TEXT = "/Users/truffy/Documents/Python/projects/blowfishLab/test_ECB/input_text_100MB.txt"
            test_PCBC(PATH_TEXT)
