#functions-----------------
def add(a:float,b:float)->float:
    return a+b

print(add(1000.3324234,20.54567))


def greet(name:str,greet:str)->str:
    return(f"{greet},{name}")
print(greet("krish","hello"))
    

def hello() -> None:  ##type anotation is optional
    print("Hi")

hello()