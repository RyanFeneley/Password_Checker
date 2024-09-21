# Password Strength Checker
# Author: Ryan Feneley
# Date: September 2024
import re

def check_password_strength(password):
    """
    Evaluates the strength of a given password based on:
    - Length (min 8 characters)
    - Use of both uppercase and lowercase letters
    - Inclusion of digits
    - Use of special characters
    
    Returns a rating and suggestions for improvement.
    """
    
    strength = {
        "Length": len(password) >= 8,
        "Uppercase": bool(re.search(r'[A-Z]', password)),
        "Lowercase": bool(re.search(r'[a-z]', password)),
        "Digits": bool(re.search(r'[0-9]', password)),
        "Special Characters": bool(re.search(r'[@$!%*?&]', password))
    }
    
    suggestions = []
    if not strength["Length"]:
        suggestions.append("Password should be at least 8 characters long.")
    if not strength["Uppercase"]:
        suggestions.append("Password should include at least one uppercase letter.")
    if not strength["Lowercase"]:
        suggestions.append("Password should include at least one lowercase letter.")
    if not strength["Digits"]:
        suggestions.append("Password should include at least one digit.")
    if not strength["Special Characters"]:
        suggestions.append("Password should include at least one special character (@, $, !, %, *, ?, &).")
    
    score = sum(strength.values())
    
    if score == 5:
        result = "Strong Password"
    elif 3 <= score < 5:
        result = "Moderate Password"
    else:
        result = "Weak Password"
    
    return result, suggestions


# Test the function with a sample password
test_password = "Pass123!"
result, feedback = check_password_strength(test_password)
print(f"Result: {result}")
if feedback:
    print("Suggestions:")
    for suggestion in feedback:
        print(f"- {suggestion}")
