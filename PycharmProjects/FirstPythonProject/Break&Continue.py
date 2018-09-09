for number in range(0, 100, 1):
    if number == 64:
        print("Tis my favorite number! " + str(number))
        break
    if number == 13:
        print("Some numbers should never be mentioned...")
        continue
    print(number)