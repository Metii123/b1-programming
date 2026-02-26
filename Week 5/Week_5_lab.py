import string

def check_min_length(password, min_len=8):
    return len(password) >= min_len

def has_uppercase(password):
    return any(c in string.ascii_uppercase for c in password)

def has_lowercase(password):
    return any(c in string.ascii_lowercase for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_special_char(password):
    return any(c in string.punctuation for c in password)

def validate_password(password):
    results = {
        "min_length": check_min_length(password),
        "has_uppercase": has_uppercase(password),
        "has_lowercase": has_lowercase(password),
        "has_digit": has_digit(password),
        "has_special_char": has_special_char(password),
    }
    results["is_valid"] = all(results.values())
    return results

print("Password Validator!\n")

password = input("Enter your password: ")
results = validate_password(password)

print(f"\n{'[Met]' if results['min_length'] else '[Not met]'} Minimum length (8+)")
print(f"{'[Met]' if results['has_uppercase'] else '[Not met]'} Has a uppercase letter")
print(f"{'[Met]' if results['has_lowercase'] else '[Not met]'} Has a lowercase letter")
print(f"{'[Met]' if results['has_digit'] else '[Not met]'} Has a digit")
print(f"{'[Met]' if results['has_special_char'] else '[Not met]'} Has a special character")

if results["is_valid"]:
    print("\nStrong Password!")
else:
    print("\nWeak Password!")
