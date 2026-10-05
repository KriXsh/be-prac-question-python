"""Lecture: for / while loops, range, break / continue, for-else."""


for i in range(5):
    print(i)
    
#for with list---------
names:list[str] = ["krish","rahul","jatin","sam"]

for name in names:
    print(f"Hello, {name}!")

numbers: list[int] =[1,2,3,4,5,6]
for number in numbers:
    print(f"Number : {number}")



#while loops---------
i:int = 0
while i < 3:
    print(i)
    i+=1


##operators

a:int =2
b:int =5

print(a==b)
print(a<b)
print(a>b)
print(a!=b)
print(a<=b)
print(a>=b)



#if-elif-else


#user_input:str ="bye"
while True:
    user_input:str = input("you : ")

    if user_input=="hello":
        print("Hi")
    
    if user_input=="hi":
        print("hi! bro")
    
    elif user_input == "bye":
        print("Bye")
        
    else:
        print("Invalid input")  


    