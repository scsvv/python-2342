def my_generator():
    print("Function started")
    for i in range(5):
        print("Function in work")
        yield i 
    

gen = my_generator()

print(next(gen))
print("STEP")
print(next(gen))
print("STEP")
print(next(gen))
print("STEP")
print(next(gen))