print("Hello World")
for i in range(5):
    print(i*"*")


main = True
while main == True:
    text = input("Enter your words")
    if text == "q":
        break
    print(text)
