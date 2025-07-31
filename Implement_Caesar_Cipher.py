def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (E)ncrypt, (D)ecrypt or (Q)uit? ").strip().upper()
        
        if choice == 'Q':
            print("Exiting program.")
            break
        elif choice not in ['E', 'D']:
            print("Invalid choice. Please enter E, D, or Q.")
            continue
        
        message = input("Enter your message: ")
        while True:
            try:
                shift = int(input("Enter the shift value (integer): "))
                break
            except ValueError:
                print("Please enter a valid integer.")
        
        if choice == 'E':
            encrypted = encrypt(message, shift)
            print(f"Encrypted message: {encrypted}")
        else:
            decrypted = decrypt(message, shift)
            print(f"Decrypted message: {decrypted}")
        print()

if __name__ == "__main__":
    main()
