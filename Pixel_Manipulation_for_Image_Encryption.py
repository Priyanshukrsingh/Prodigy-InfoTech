from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Encrypt using XOR with key
    encrypted_array = img_array ^ key
    
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(encrypted_path, key, output_path):
    encrypted_img = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_img)
    
    # Decrypt using XOR with key (XOR again with the same key)
    decrypted_array = encrypted_array ^ key
    
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter choice (1 or 2): ")

    image_path = input("Enter image path: ")
    key = int(input("Enter encryption/decryption key (0-255): "))
    output_path = input("Enter output path to save result: ")

    if choice == '1':
        encrypt_image(image_path, key, output_path)
    elif choice == '2':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
