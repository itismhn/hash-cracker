from time import sleep
import hashlib

def main():
    print("""
█──█ █▀▀█ █▀▀ █──█ ── █▀▀ █▀▀█ █▀▀█ █▀▀ █─█ █▀▀ █▀▀█ 
█▀▀█ █▄▄█ ▀▀█ █▀▀█ ▀▀ █── █▄▄▀ █▄▄█ █── █▀▄ █▀▀ █▄▄▀ 
▀──▀ ▀──▀ ▀▀▀ ▀──▀ ── ▀▀▀ ▀─▀▀ ▀──▀ ▀▀▀ ▀─▀ ▀▀▀ ▀─▀▀
@itisMHN v1.1 - https://github.com/itismhn/hash-cracker
""")
    user_input()
def user_input():
    try:
        input_hash = input("[+] Enter your hash: ")
        sleep(0.7)
        while True:
            print("----------\n[1] Hash Identifier\n[2] Hash Cracker")
            input_option = input("[+] Please Enter an Option: ")
            sleep(0.7)
            if input_option == '1':
                hash_type = hash_identifier(input_hash)
                print(f'[-] Hash is {hash_type}')
                break
            elif input_option == '2':
                hash_type = hash_identifier(input_hash)
                hash_cracker(input_hash,hash_type)
                break
            else:
                print("\n[!] Choose Correct Option!\n")
                sleep(0.7)
                continue
    except KeyboardInterrupt:
            print("\n [!] Exiting...")
    except Exception as err:
        print("[!] Got Error : ", err)
def hash_identifier(input_hash):
    md5_valid_hash = "9b63036e1089e21b8a599bdfb720b7da"
    sha1_valid_hash = "3b3a15497ad565a6045a1649d13114d625a93283"
    sleep(0.7)
    try:
        if(len(input_hash) == len(md5_valid_hash)):
            return('MD5')
        elif(len(input_hash) == len(sha1_valid_hash)):
            return('SHA1')
        else:
            print("[-] can't detect hash")
    except:
        print("[!] Got Error!")
def hash_cracker(input_hash,hash_type):
    try:
        print('----------')
        print("[++] choose an word-List to crack the hash")
        print("[-1-] number-list\n[-2-] Your word-list file")
        list_option = input("[*] Please Enter a list: ")
        if list_option == '1':
            print('----------')
            print("[+++] for example enter 4 for testing (0000 - 9999)")
            num_digit = int(input("[+] Enter a digit: "))
            main_cracker(input_hash,num_digit,hash_type)
        elif list_option == '2':
            print("coming soon ...")
        else:
            print("\n[!] Choose Correct Option!\n")
            sleep(0.7)
    except TypeError as err:
        print(f"Got {err}\n Enter valid number")
def main_cracker(input_hash,num_digit,hash_type):
    # create list by input digit
    def generate_numbers_with_digit(num_digit):
        min_number = 10**(num_digit-1)
        max_number = 10**num_digit - 1
        numbers_list = [str(i).zfill(num_digit) for i in range(min_number, max_number+1)]
        return numbers_list
    numbers_list = generate_numbers_with_digit(num_digit)
    if(hash_type == "MD5"):
        for number in numbers_list:
            number_hash = hashlib.md5(number.encode())
            number_hash = number_hash.hexdigest()
            if(input_hash == number_hash):
                print(f'[$] Plain password found!\n {input_hash} --> {number}')
            else:
                continue
    elif(hash_type == "SHA1"):
        print('SHA1')
    else:
        print('None')

if __name__ == "__main__":
    main()