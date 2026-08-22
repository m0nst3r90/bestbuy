import os
import time
from operator import truediv

import products, store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store:store.Store):
    while True:
        exit = False
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print(f"\033[33m{'Store Menu':^30}\n{'----------':^30}\033[0m")
            print("\033[32m1.\033[0m List all products in store")
            print("\033[32m2.\033[0m Show total amount in store")
            print("\033[32m3.\033[0m Make an order")
            print("\033[32m4.\033[0m \033[31mQuit\033[0m")

            userinput = input("Please choose a \033[32mnumber\033[0m: ")
            if userinput == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\033[33m{'All Products':^30}\n{'------------':^30}\033[0m")
                print(f"{'Name':<28}{'Price':>10}{'Quantity':>10}")
                for i, product in enumerate(store.get_all_products()):
                    print(f"{i+1}. {product.name:<26} \033[34m{'$':>2}{product.price:>6}\033[0m\033[36m{product.quantity:>10}\033[0m")

                userinput = input("\nPress enter to go \033[32mback\033[0m")
                break
            elif userinput == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\033[33m{'Total Amount in Store':^30}\n{'---------------------':^30}\033[0m")
                print(f"Total of \033[36m{store.get_total_quantity()}\033[0m items in store")

                userinput = input("\nPress enter to go \033[32mback\033[0m")
                break
            elif userinput == "3":
                exit_order = False
                order: list[tuple[products.Product, int]] = []
                total_order_cost = 0

                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"\033[33m{'Order Menu':^30}\n{'----------':^30}\033[0m")
                    for i, product in enumerate(store.get_all_products()):
                        cart_product_amount = 0
                        for order_product, amount in order:
                            if order_product == product:
                                cart_product_amount += amount
                        print(f"{i + 1}. {product.name:<26} \033[34m{'$':>2}{product.price:>6}\033[0m\033[36m{product.quantity:>10}\033[0m \033[31m{('- '+str(cart_product_amount)) if cart_product_amount > 0 else ''}\033[0m")

                    print(f"When you want to finish order or leave, enter empty text.")
                    print(f"Current cart: \033[34m${total_order_cost}\033[0m")
                    userinput = input("\nWich product \033[32m#\033[0m do you want? ")

                    try:
                        userinput = int(userinput)
                        if userinput > 0 and userinput < len(store.get_all_products())+1:
                            choosen_product = store.get_all_products()[userinput - 1]
                            is_product_chosen = False
                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"\033[33m{'Order Menu':^30}\n{'----------':^30}\033[0m")
                            for i, product in enumerate(store.get_all_products()):
                                cart_product_amount = 0
                                is_product_chosen = product == choosen_product
                                for order_product, amount in order:
                                    if order_product == product:
                                        cart_product_amount += amount
                                print(f"{i + 1}. {'\033[33m' if is_product_chosen else ''}{product.name:<26}{'\033[0m' if is_product_chosen else ''} \033[34m{'$':>2}{product.price:>6}\033[0m\033[36m{product.quantity:>10}\033[0m \033[31m{('- ' + str(cart_product_amount)) if cart_product_amount > 0 else ''}\033[0m")

                            print(f"\nChoosen Product: \033[33m{choosen_product.name}\033[0m")
                            amount_input = int(input(f"\nWhat \033[36mamount\033[0m do you want? "))
                            if amount_input > 0:
                                total_oder_amount = amount_input
                                for order_product, order_amount in order:
                                    if order_product == choosen_product:
                                        total_oder_amount += order_amount

                                if not total_oder_amount > choosen_product.get_quantity():
                                    order.append((choosen_product, amount_input))
                                    for product, amount in order:
                                        total_order_cost += (product.price * amount)
                                    print(f"Product added to list")
                                    time.sleep(1)
                                else:
                                    print(f"\033[31mAmount not available\033[0m")
                                    time.sleep(1)



                    except ValueError:
                        if userinput == "":
                            if len(order) < 1:
                                break

                            print(f"Order made! Total payment: \033[34m${store.order(order)}\033[0m")
                            time.sleep(1)
                            order.clear()
                            total_order_cost = 0

                            break

                        elif userinput == "x":
                            exit_order =True
                            break
                if exit_order:
                    break
            elif userinput == "4":
                exit = True
                break
        if exit:
            break





start(best_buy)