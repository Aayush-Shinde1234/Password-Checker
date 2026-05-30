# Password Strength check
print("="*30)
print("   PASSWORD STRENGTH CHECK")
print("="*30)

password = input("Enter the password :")
strength = 0

user = "yes"
while user.lower() == "yes" :
    if(" " in password):
        print("Invalid password (no spaces allowed)")
    else:
        has_length = len(password) >= 8
        has_number = any(ch.isdigit() for ch in password)
        has_upper = any(ch.isupper() for ch in password)
        has_special = any(ch in "!@#$*_" for ch in password)

        if has_length:
            strength += 1
        if has_number:
            strength += 1
        if has_upper:
            strength += 1
        if has_special:
            strength += 1
    
        if strength == 0:
            print("Very weak password")
        elif strength == 1:
            print("Weak password")
        elif strength == 2:
            print("Medium password")
        elif strength == 3:
            print("Strong password")
        elif strength == 4:
            print("Very strong password")

        if strength < 4:
            print("Missing:")
        
            if not has_length:
                print("- Length should be at least 8")
            if not has_number:
                print("- Add a number")
            if not has_upper:
                print("- Add an uppercase letter")
            if not has_special:
                print("- Add a special character (!@#$*)")

    print(f"Point :{strength}")
    user = input("\nDo you want to continue  yes/no :")
print("="*40)