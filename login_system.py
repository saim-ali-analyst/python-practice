# ==========================================
#   Gmail Signup & Login System
#   Author: Saim Ali
# ==========================================

# ---------- Signup ----------
print("=========== Signup ===========")

name = input("What is your name? ")
gmail = input(f"Create your gmail, {name}: ")
print("You have successfully created your Gmail.")

password = input("Create a strong password: ")
print("You have successfully created your password.")

print(f"\nWelcome {name}, you have successfully created your Gmail.\n")


# ---------- Login ----------
print("=========== Login ===========")

input_gmail = input("Enter your Gmail: ")
input_password = input("Enter your password: ")

if input_gmail == gmail and input_password == password:
    print(f"\nWelcome {name}, you are now logged in.")
else:
    print("\nInvalid login details.")