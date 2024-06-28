try:
    grade = int(input("Please enter your grade:"))
    if grade>100 or grade<0:
        raise Exception("Please enter from 0-100!")
    else:
        print("grade is:",grade)


except Exception as e:
    print(e)