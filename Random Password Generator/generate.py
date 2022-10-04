import random,string

l = str((string.digits)+(string.ascii_letters)+(string.punctuation))

len = int(input(("Enter the length of password")))

passwd = ""
for i in range(len):
  passwd += (random.choice(l))

print("="*50)
print("Generated Password is :"+passwd)
print("="*50)
