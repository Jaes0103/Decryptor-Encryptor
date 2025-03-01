import tkinter as tk

def vigenere_cipher(text, key, mode):

  vigenere_square = [[chr((i + j) % 26 + ord('A')) for j in range(26)] for i in range(26)]
  result = ""
  j = 0
  for char in text.upper():
    if char.isalpha():
      key_index = ord(key[j % len(key)]) - ord('A')
      shift = key_index
      if mode == 'decrypt':
        shift *= -1
      new_char = vigenere_square[key_index][ord(char) - ord('A')]
      result += new_char
      j += 1
    else:
      result += char
  return result

def encrypt_decrypt():
  
  mode = mode_var.get()
  text = text_entry.get("1.0", tk.END).strip()
  key = key_entry.get().strip()
  if not text or not key:
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Please enter text and key!")
    return

  # Update label and text type based on button clicked
  output_label_text = "Plaintext:" if mode == "decrypt" else "Ciphertext:"
  output_label.config(text=output_label_text)
  text_label_text = "Ciphertext:" if mode == "encrypt" else "Plaintext:"
  text_label.config(text=text_label_text)

  result = vigenere_cipher(text, key, mode)

  # Prepare output in a table
  output_lines = []
  header_line = f"Plaintext                     Key                           Ciphertext\n"  # Bold header line
  output_lines.append(header_line)
  max_len = max(len(text.strip()), len(key.strip()), len(result.strip()))  # Find maximum length without spaces

  for i in range(len(text)):
    if not text[i].isalpha():
      output_lines.append(f"{text[i]:^{max_len}}   {key[i % len(key)]:^{max_len}}   {result[i]:^{max_len}}")
    else:
      output_lines.append(f"{text[i].upper().strip():^{max_len}}   {key[i % len(key)].upper().strip():^{max_len}}   {result[i].upper().strip():^{max_len}}")
  output_text.delete("1.0", tk.END)
  output_text.insert(tk.END, f"User Input:\n{text}\n\nKey: {key}\n\nOutput:\n" + "\n".join(output_lines))

# Create the main window
root = tk.Tk()
root.title("Vigenere Cipher")
root.geometry("800x800") 
# Radio buttons for wncrypt and decrypt
mode_var = tk.StringVar()
mode_var.set("encrypt")  

encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt")
encrypt_radio.pack()

decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt")
decrypt_radio.pack()

text_label = tk.Label(root, text="Plaintext:")  
text_label.pack()

text_entry = tk.Text(root, width=50, height=5)
text_entry.pack()

key_label = tk.Label(root, text="Key:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

# Button for encryption/decryption
encrypt_button = tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt)
encrypt_button.pack()

# Output text box
output_label = tk.Label(root, text="Output:")
output_label.pack()

output_text = tk.Text(root, width=100, height=40)
output_text.pack()

root.mainloop()