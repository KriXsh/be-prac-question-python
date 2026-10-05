a, b = 10, "krish"


try:
    print(a+b)

except TypeError as e:
    print(e)
    print("please enter a number")
except Exception as error:
    print("error", (error))


# else:
#     print("no error")
# finally:
#     print("done")
print("continue with the program")
