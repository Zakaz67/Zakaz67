age = 20 

if age < 2:
    i = "младенец"
elif age < 4:
    i = "малыш"
elif age < 13:
    i =  "ребенок" 
elif age < 20:
    i = "подросток"
elif age < 65:
    i = "взрослый"
elif age >= 65:
    i =  "пожилой человек"
print(f"твой лвл {i}")