password= "Garvit123"

score = 0

if len(password) >= 8:
    score += 1 

if any(char.isdigit() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

if password[0].isupper():
    score += 1
if "@" in password:
    score += 1
if score >= 4:
    print("Strong Password")
else:
    print("Weak Password")
  
