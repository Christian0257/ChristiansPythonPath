print("Sanity Check")

Number = 0

while Number != 11:
    print(Number)
    Number += 1

print("\nLucky Number Test\n")

LuckyNumber = 64
CurrentNumber = 0
while True:
    print(CurrentNumber)
    if CurrentNumber == LuckyNumber:
        print("My Lucky Number!")
        break
    CurrentNumber += 1