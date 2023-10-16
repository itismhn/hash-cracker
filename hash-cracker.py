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
    sleep(1)
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
            continue

def hash_identifier(input_hash):
    pass

def hash_cracker(input_hash):
    pass
if __name__ == "__main__":
    main()