import tkinter as tk
from tkinter import ttk, filedialog
from ttkbootstrap import Style

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

class CryptographyApp:
    def __init__(self, master):
        self.master = master
        master.title("Cryptography Application")

        # ttkbootstrap Style
        self.style = Style(theme='superhero')

        # GUI elements
        self.upload_button = ttk.Button(master, text="Upload File", command=self.upload_file)
        self.encrypt_button = ttk.Button(master, text="Encrypt", command=self.encrypt_file)
        self.decrypt_button = ttk.Button(master, text="Decrypt", command=self.decrypt_file)
        self.result_label = ttk.Label(master, text="Result: ")

        # Layout
        self.upload_button.pack(pady=10)
        self.encrypt_button.pack(pady=10)
        self.decrypt_button.pack(pady=10)
        self.result_label.pack(pady=10)

        # Additional instance variable for file_path
        self.file_path = None

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a file")
        self.result_label.config(text=f"Selected File: {self.file_path}")

    def encrypt_file(self):
        if self.file_path:
            with open(self.file_path, 'r') as file:
                content = file.read()
                encrypted_content = encrypt_caesar(content, shift=3)  # You can change the shift value
                with open(self.file_path, 'w') as encrypted_file:
                    encrypted_file.write(encrypted_content)
            self.result_label.config(text="File Encrypted successfully.")
        else:
            self.result_label.config(text="Please select a file first.")

    def decrypt_file(self):
        if self.file_path:
            with open(self.file_path, 'r') as encrypted_file:
                encrypted_content = encrypted_file.read()
                decrypted_content = decrypt_caesar(encrypted_content, shift=3)  # You can change the shift value
                with open(self.file_path, 'w') as decrypted_file:
                    decrypted_file.write(decrypted_content)
            self.result_label.config(text="File Decrypted successfully.")
        else:
            self.result_label.config(text="Please select a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptographyApp(root)
    root.mainloop()
