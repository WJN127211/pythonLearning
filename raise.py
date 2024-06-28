try:
    boolean = input("Please enter true or false:")
    if boolean !="true" and boolean !="false":
        raise Exception("only true or false allowed!")
    else:
        print("you entered",boolean)
except Exception as e:
    print(e)