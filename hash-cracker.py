from time import sleep

def main():
    print("""
█──█ █▀▀█ █▀▀ █──█ ── █▀▀ █▀▀█ █▀▀█ █▀▀ █─█ █▀▀ █▀▀█ 
█▀▀█ █▄▄█ ▀▀█ █▀▀█ ▀▀ █── █▄▄▀ █▄▄█ █── █▀▄ █▀▀ █▄▄▀ 
▀──▀ ▀──▀ ▀▀▀ ▀──▀ ── ▀▀▀ ▀─▀▀ ▀──▀ ▀▀▀ ▀─▀ ▀▀▀ ▀─▀▀
@itisMHN v1.1
""")
    user_input()
def user_input():
    input_hash = input("[+] Enter your hash: ")
    sleep(0.7)
    while True:
        print("----------\n[1] Hash Identifier\n[2] Hash Cracker\n")
        input_option = input("[+] Please Enter an Option: ")
        if input_option == '1':
            hash_identifier(input_hash)
            break
        elif input_option == '2':
            hash_cracker(input_hash)
            break
        else:
            print("\n[!] Choose Correct Option!\n")
            sleep(0.7)

            continue

def hash_identifier(input_hash):
    md5_valid_hash = "9b63036e1089e21b8a599bdfb720b7da"
    sha1_valid_hash = "3b3a15497ad565a6045a1649d13114d625a93283"
    sleep(0.7)
    if(len(input_hash) == len(md5_valid_hash)):
        print('[-] Hash is MD5')
    elif(len(input_hash) == len(sha1_valid_hash)):
        print('[-] Hash is SHA1')
    else:
        print("[-] can't detect hash")
def hash_cracker(input_hash):
    pass
if __name__ == "__main__":
    main()