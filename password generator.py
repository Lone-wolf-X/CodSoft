'''
In this program we build a Password Generator program, In which we generating a valid password of user desired length.
If user enter invalid length like (less than 8 then user have to again enter length), But user enter any non-integer value then, except valueError
part will be executed.  
    '''

import random 
import string

def generate_password(length):
    if length < 8:
        print("\nPassword length at least 8 characters.\n")
        return None
    pwd = string.ascii_letters + string.punctuation + string.digits
    password_chars = []
    for i in range(length):
        password_chars.append(random.choice(pwd))
        password = ''.join(password_chars)

    return password

def main():
    try:
        length = int(input("Enter the length, The password you want: "))
        password = generate_password(length)

        if password != None:
            print(f"Generated password: {password}")
        else:
            print("Enter valid length for password.\n\n")
            main()
    except ValueError:
        print("Please Enter Valid input....")
        main()

main()
    
