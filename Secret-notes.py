import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from base64 import b64encode, b64decode

def encrypt_data(key, plaintext):
    encrypted_data = []
    for i in range(len(plaintext)):
        key_c = key[i % len(key)]
        encrypted_data.append(chr((ord(plaintext[i]) + ord(key_c)) % 256))
    return b64encode("".join(encrypted_data).encode('utf-8')).decode('utf-8')

def decrypt_data(key, ciphertext):
    decrypted_data = []
    ciphertext = b64decode(ciphertext.encode('utf-8')).decode('utf-8')
    for i in range(len(ciphertext)):
        key_c = key[i % len(key)]
        decrypted_data.append(chr((ord(ciphertext[i]) - ord(key_c)) % 256))
    return "".join(decrypted_data)

def save_and_encrypt():
    title = entry_1.get()
    text = text_1.get("1.0", 'end-1c')
    password = entry_2.get()

    if len(title) == 0 or len(text) == 0 or len(password) == 0:
        messagebox.showwarning("", "Xahiş edirik məlumatları tam daxil edin!")
    else:
        encrypted_text = encrypt_data(password, text)
        try:
            with open('shifrlenmish.txt', 'a') as data_file:
                data_file.write(f"\n{title}\n{encrypted_text}")
        except FileNotFoundError:
            with open('shifrlenmish.txt', 'w') as data_file:
                data_file.write(f"\n{title}\n{encrypted_text}")
        finally:
            entry_1.delete(0, tk.END)
            text_1.delete('1.0', 'end')
            entry_2.delete(0, tk.END)

def back_decrypt():
    text = text_1.get("1.0", 'end-1c')
    password = entry_2.get()

    if len(text) == 0 or len(password) == 0:
        messagebox.showwarning("", "Xahiş edirik məlumatları tam daxil edin!")
    else:
        decrypted_text = decrypt_data(password, text)
        if decrypted_text:
            text_1.delete('1.0', 'end')
            text_1.insert('1.0', decrypted_text)

pencere = tk.Tk()
pencere.title('Şifrlənmiş notlar')
pencere.minsize(width=280, height=250)
pencere.config(padx=20, pady=20)


image = Image.open("secret.png")
resized_image = image.resize((180, 90))
photo = ImageTk.PhotoImage(resized_image)

image_label = tk.Label(pencere, image=photo, bg="gray10")
image_label.pack()

label_1 = tk.Label(text='Başlığınızı daxil edin')
label_1.cget("text")
label_1.pack()

entry_1 = tk.Entry(width=30)
entry_1.pack()

label_2 = tk.Label(text="Mətni daxil edin")
label_2.pack()

text_1 = tk.Text(width=30, height=10)
text_1.pack()

label_3 = tk.Label(text='Şifrənizi daxil edin!')
label_3.pack()

entry_2 = tk.Entry(width=30)
entry_2.pack()

button_1 = tk.Button(text="Yadda saxla və mətni şifrlə", command=save_and_encrypt)
button_1.pack()

button_2 = tk.Button(text="Mətni deşifrləyin", command=back_decrypt)
button_2.pack()

pencere.mainloop()
S