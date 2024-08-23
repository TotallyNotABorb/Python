old=input("Введите слово которое хотите заменить")
new=input("Введите слово на которое хотите заменить")
raw=input("Введите имя файла")
with open(raw,"wb+") as file:
    words=file.read()
    words.replace(old,new)
    file.write(words)