password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result['digit'] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result['uppercase'] = uppercase

print(result)

if all(result.values()):
    print("Password is Strong")
else:
    print("Password is Weak")