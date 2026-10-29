table = 0
num = 0
while table <= 10:
    print(f"Table de {table}: ", end="")
    table += 1 
    num = 0   #start from 0
    while num <= 10:
        print(table*num, end=" ")
        num += 1 
    print() #make space

            