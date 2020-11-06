phrase = input("choisissez une phrase:")
cesar = "vigenere"   #ici on peut remplacer par un input si on veut proposer à l'utilisateur de choisir le code de décalage, le programme fonctionnera
code = ""
for i in range(len(phrase)):
    b= cesar[i%len(cesar)]
    n = ord(b)
    n= n-97
    if phrase[i] != " ":
        if ord(phrase[i])+n > 122:
            code += chr(ord(phrase[i])+n-26)
        else:
            code += chr(ord(phrase[i])+n)
    else:
        code += " "
print(code)