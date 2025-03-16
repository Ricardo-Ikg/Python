import os 

def encrypting(elements):
       asc = [ord(i) for i in list(elements)]
       shifted_values = [i << 1 for i in asc]
       new_letters = "".join([chr(i) for i in shifted_values])
       return new_letters

def writer(new_letters, file):
        encrypted_file = (os.path.basename(file) + "_encrypted.txt") 
        with open (encrypted_file, "w") as f:
            f.write(new_letters)
        print(f"encrypted file saved as {encrypted_file}")

file = input("Put the path of file to be encrypted:").strip()
with open (file,"r", encoding= "utf-8") as reading:
      content = reading.read()


encrypted_text = encrypting(content)
writer(encrypted_text, file)
