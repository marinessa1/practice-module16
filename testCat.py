from cat import Cat
cat1 = Cat('Sam', 'мальчик', '10')
cat2 = Cat('Aleks', 'мальчик', '5')
cat3 = Cat('Niki', 'девочка', '3')
Cat = [(cat1.getname(), cat1.getgender(), cat1.getage()),
       (cat2.getname(), cat2.getgender(), cat2.getage()),
       (cat3.getname(), cat3.getgender(), cat3.getage())]
print("Список котов и кошек:")
for cat in Cat:
    print(",".join(cat))

