import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Score calculation (out of 5)
    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Strength levels
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Feedback
    feedback = []
    if length_error:
        feedback.append("Password should be at least 8 characters long.")
    if lowercase_error:
        feedback.append("Include at least one lowercase letter.")
    if uppercase_error:
        feedback.append("Include at least one uppercase letter.")
    if digit_error:
        feedback.append("Include at least one digit.")
    if special_char_error:
        feedback.append("Include at least one special character (e.g., @, #, $, etc.).")

    return strength, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for f in feedback:
            print(" -", f)
    else:
        print("Your password is strong and meets all criteria.")
