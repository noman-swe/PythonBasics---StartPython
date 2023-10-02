a = int(input("Enter a Number " ))

match a:
    case 1:
        print('Case is 1')
    case 2:
        print("Case is 2")
    case 13:
        print('Case is 13')
    case 22:
        print("Case is 22")
    case _:
        print("No Match found")