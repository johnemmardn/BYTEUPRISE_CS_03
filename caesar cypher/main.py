import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - shift_base + shift) % 26 + shift_base
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def encrypt_text():
    plaintext = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = caesar_cipher_encrypt(plaintext, shift)
    result_var.set(encrypted_text)

def decrypt_text():
    ciphertext = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
    result_var.set(decrypted_text)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place the text entry field
tk.Label(root, text="Text:").grid(row=0, column=0, padx=10, pady=10)
entry_text = tk.Entry(root, width=50)
entry_text.grid(row=0, column=1, padx=10, pady=10)

# Create and place the shift entry field
tk.Label(root, text="Shift:").grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Create and place the Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

# Create and place the Decrypt button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Create and place the result label
tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10)
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, width=50)
result_label.grid(row=3, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
