

try:
    num1 = int(input("please enter an integer:"))
    num2 = int(input("please enter an integer:"))
    result = num1/num2
    
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("No String Allowed")
except BaseException:
    print("Unknown Bug")
else:
    #if no exception, will excute this
    print("result:",result)
finally:
    #whatever any happen, this will be excuted at the end
    print("done!")



