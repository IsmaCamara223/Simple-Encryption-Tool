from cryptography.fernet import Fernet
import os

def key_generator():
  key = Fernet.generate_key()
  with open("Confidential.key", "wb") as key_file:
    key_file.write(key)
    
def key_loader():
  return open("Confidential.key", "rb").read()

def encryption(filename, key):
  f = Fernet(key)
  with open(filename, "rb") as file:
    file_data = file.read()
    encrypted_data = f.encrypt(file_data)
  with open(filename, "wb") as file:
    file.write(encrypted_data)

def decryption(filename, key):
  f = Fernet(key)
  with open(filename, "rb") as file:
    encrypted_data = file.read()
    try:
      decrypted_data = f.decrypt(encrypted_data)
    except InvalidToken:
      print("Invalid Key")
      return 
  with open(filename, "wb") as file:
    file.write(decrypted_data)

choice = input("Enter 'e' to encrypt or 'd' to decrypt file: ")
if choice == "e":
  filename = input("Specify file to encrypt (including extension): ")
  if os.path.exists(filename):
    key_generator()
    key = key_loader()
    encryption(filename, key)
    print("File successfully encrypted!")
  else:
    print(f"File '{filename}' not found.")

elif choice == "d":
  filename = input("Specify file to decrypt (including extension): ")
  if os.path.exists(filename):
    key = key.loader()
    decryption(filename, key)
    print("File successfully decrypted!")
  else:
    print(f"File '{filename}' not found.")

else:
  print("Invalid Entry.")


