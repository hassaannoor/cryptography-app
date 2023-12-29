import tkinter as tk
from tkinter import ttk, filedialog
from ttkbootstrap import Style
import os

def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(encrypted_text, shift):
    return encrypt_caesar(encrypted_text, -shift)

def encrypt_vigenere(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + ord(key[i % key_length]) - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + ord(key[i % key_length]) - ord('a')) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - (ord(key[i % key_length]) - ord('a'))) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - (ord(key[i % key_length]) - ord('a'))) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_rail_fence(text, key):
    key = int(key)
    encrypted_text = [''] * key
    index = 0
    direction = 1

    for char in text:
        encrypted_text[index] += char
        index += direction
        if index == key - 1 or index == 0:
            direction *= -1

    return ''.join(encrypted_text)

def decrypt_rail_fence(encrypted_text, key):
    key = int(key)
    decrypted_text = [''] * key
    index = 0
    direction = 1

    for char in encrypted_text:
        decrypted_text[index] += char
        index += direction
        if index == key - 1 or index == 0:
            direction *= -1

    result = [''] * len(encrypted_text)
    index = 0

    for row in decrypted_text:
        for char in row:
            result[index] = char
            index += 1

    return ''.join(result)
def encrypt_transposition(text, key):
    key = int(key)
    encrypted_text = [''] * key
    index = 0

    for char in text:
        encrypted_text[index] += char
        index = (index + 1) % key

    return ''.join(encrypted_text)

def decrypt_transposition(encrypted_text, key):
    key = int(key)
    columns = len(encrypted_text) // key
    rows = key
    leftover = len(encrypted_text) % key
    result = [''] * key

    index = 0
    for row in range(rows):
        for col in range(columns + (1 if row < leftover else 0)):
            result[index] += encrypted_text[row + col * rows]
            index += 1

    return ''.join(result)
def encrypt_substitution(text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += key[alphabet.index(char.upper())].lower()
            else:
                encrypted_text += key[alphabet.index(char)]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_substitution(encrypted_text, key):
    return encrypt_substitution(encrypted_text, key)

class CryptographyApp:
    def __init__(self, master):
        self.master = master
        master.title("Cryptography Application")

        # ttkbootstrap Style
        # self.style = Style(theme='azure')

        # GUI elements
        self.upload_button = ttk.Button(master, text="Upload File", command=self.upload_file, width=20)
        self.encrypt_button = ttk.Button(master, text="Encrypt", command=self.encrypt_file, width=20)
        self.decrypt_button = ttk.Button(master, text="Decrypt", command=self.decrypt_file, width=20)
        self.result_label = ttk.Label(master, text="Result: ")

        # Cipher selection
        self.cipher_label = ttk.Label(master, text="Select Cipher:")
        self.cipher_combobox = ttk.Combobox(master, values=["Caesar", "Vigenere", "Substitution", "Transposition", "Rail Fence"], width=18)
        self.cipher_combobox.set("Caesar")

        # Key input
        self.key_label = ttk.Label(master, text="Enter Key:")
        self.key_entry = ttk.Entry(master, width=20)

        # Layout
        master.geometry("600x600")  # Set initial dimensions
        self.upload_button.pack(pady=10)
        self.cipher_label.pack(pady=5)
        self.cipher_combobox.pack(pady=5)
        self.key_label.pack(pady=5)
        self.key_entry.pack(pady=5)
        self.encrypt_button.pack(pady=10)
        self.decrypt_button.pack(pady=10)
        self.result_label.pack(pady=10)

        # Additional instance variables for file_path, selected_cipher, and key
        self.file_path = None
        self.selected_cipher = "Caesar"
        self.key = ""

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a file")
        self.result_label.config(text=f"Selected File: {self.file_path}")

    def encrypt_file(self):
        if self.file_path:
            self.selected_cipher = self.cipher_combobox.get()
            self.key = self.key_entry.get()

            try:
                key_value = int(self.key)
            except ValueError:
                self.result_label.config(text="Invalid key. Please enter a valid integer key.")
                return

            with open(self.file_path, 'rb') as file:
                content = file.read()
                if self.selected_cipher == "Caesar":
                    encrypted_content = encrypt_caesar(content, key_value)
                elif self.selected_cipher == "Vigenere":
                    encrypted_content = encrypt_vigenere(content, self.key)
                elif self.selected_cipher == "Transposition":
                    encrypted_content = encrypt_transposition(content, self.key)
                elif self.selected_cipher == "Substitution":
                    encrypted_content = encrypt_substitution(content, self.key)
                elif self.selected_cipher == "Rail Fence":
                    encrypted_content = encrypt_rail_fence(content, self.key)
                else:
                    self.result_label.config(text="Invalid cipher selection")
                    return

            # Append "-encrypted" to the file name before the extension
            file_name, file_extension = os.path.splitext(os.path.basename(self.file_path))
            encrypted_file_name = f"{file_name}-encrypted{file_extension}"
            encrypted_file_path = os.path.join(os.path.dirname(self.file_path), encrypted_file_name)

            with open(encrypted_file_path, 'w') as encrypted_file:
                encrypted_file.write(encrypted_content)

            self.result_label.config(text=f"File Encrypted successfully. Encrypted file saved as: {encrypted_file_path}")
        else:
            self.result_label.config(text="Please select a file first.")

    def decrypt_file(self):
        if self.file_path:
            self.selected_cipher = self.cipher_combobox.get()
            self.key = self.key_entry.get()

            try:
                key_value = int(self.key)
            except ValueError:
                self.result_label.config(text="Invalid key. Please enter a valid integer key.")
                return

            with open(self.file_path, 'rb') as encrypted_file:
                encrypted_content = encrypted_file.read()
                if self.selected_cipher == "Caesar":
                    decrypted_content = decrypt_caesar(encrypted_content, key_value)
                elif self.selected_cipher == "Vigenere":
                    decrypted_content = decrypt_vigenere(encrypted_content, self.key)
                elif self.selected_cipher == "Transposition":
                    encrypted_content = decrypt_transposition(encrypted_content, self.key)
                elif self.selected_cipher == "Substitution":
                    encrypted_content = decrypt_substitution(encrypted_content, self.key)
                elif self.selected_cipher == "Rail Fence":
                    encrypted_content = decrypt_rail_fence(encrypted_content, self.key)
                else:
                    self.result_label.config(text="Invalid cipher selection")
                    return

            # Append "-decrypted" to the file name before the extension
            file_name, file_extension = os.path.splitext(os.path.basename(self.file_path))
            decrypted_file_name = f"{file_name}-decrypted{file_extension}"
            decrypted_file_path = os.path.join(os.path.dirname(self.file_path), decrypted_file_name)

            with open(decrypted_file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_content)

            self.result_label.config(text=f"File Decrypted successfully. Decrypted file saved as: {decrypted_file_path}")
        else:
            self.result_label.config(text="Please select a file first.")


if __name__ == "__main__":
    root = tk.Tk()
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "themes/dark")

    app = CryptographyApp(root)
    root.mainloop()
