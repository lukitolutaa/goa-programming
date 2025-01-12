print('''avaliable products:

cola(1), fanta(2), pepsi(3),
lays(4), pringles(5), doritos(6)
kitkat(7), bount(8), biscrem(9),

 ''')

user_choice = int(input("Enter Product Number: "))

products = ['cola', 'fanta', 'pepsi',
            'lays', 'pringles', 'doritos',            
             'kitkat', 'bount', 'biscrem',]

user_choice = products[user_choice-1]

print(f'your received {user_choice}')