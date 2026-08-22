import os
import time

import products, store

class Colors:
    """Colors class"""
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

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

            print(f"{Colors.YELLOW}{'Store Menu':^30}\n{'----------':^30}{Colors.RESET}")
            print(f"{Colors.GREEN}1.{Colors.RESET} List all products in store")
            print(f"{Colors.GREEN}2.{Colors.RESET} Show total amount in store")
            print(f"{Colors.GREEN}3.{Colors.RESET} Make an order")
            print(f"{Colors.GREEN}4.{Colors.RESET} {Colors.RED}Quit{Colors.RESET}")

            userinput = input(f"Please choose a {Colors.GREEN}number{Colors.RESET}: ")
            if userinput == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{Colors.YELLOW}{'All Products':^30}\n{'------------':^30}{Colors.RESET}")
                print(f"{'Name':<28}{'Price':>10}{'Quantity':>10}")
                for i, product in enumerate(store.get_all_products()):
                    print(f"{i+1}. {product.name:<26} {Colors.BLUE}{'$':>2}{product.price:>6}{Colors.RESET}{Colors.CYAN}{product.quantity:>10}{Colors.RESET}")

                userinput = input(f"\nPress enter to go {Colors.GREEN}back{Colors.RESET}")
                break
            elif userinput == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{Colors.YELLOW}{'Total Amount in Store':^30}\n{'---------------------':^30}{Colors.RESET}")
                print(f"Total of {Colors.CYAN}{store.get_total_quantity()}{Colors.RESET} items in store")

                userinput = input(f"\nPress enter to go {Colors.GREEN}back{Colors.RESET}")
                break
            elif userinput == "3":
                exit_order = False
                order: list[tuple[products.Product, int]] = []
                total_order_cost = 0

                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"{Colors.YELLOW}{'Order Menu':^30}\n{'----------':^30}{Colors.RESET}")
                    for i, product in enumerate(store.get_all_products()):
                        cart_product_amount = 0
                        for order_product, amount in order:
                            if order_product == product:
                                cart_product_amount += amount
                        print(f"{i + 1}. {product.name:<26} {Colors.BLUE}{'$':>2}{product.price:>6}{Colors.RESET}{Colors.CYAN}{product.quantity:>10}{Colors.RESET} {Colors.RED}{('- '+str(cart_product_amount)) if cart_product_amount > 0 else ''}{Colors.RESET}")

                    print(f"\nWhen you want to finish order or leave, enter empty text.")
                    print(f"Current cart: {Colors.BLUE}${total_order_cost}{Colors.RESET}")
                    userinput = input(f"\nWich product {Colors.GREEN}#{Colors.RESET} do you want? ")

                    try:
                        userinput = int(userinput)
                        if userinput > 0 and userinput < len(store.get_all_products())+1:
                            choosen_product = store.get_all_products()[userinput - 1]
                            is_product_chosen = False
                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"{Colors.YELLOW}{'Order Menu':^30}\n{'----------':^30}{Colors.RESET}")
                            for i, product in enumerate(store.get_all_products()):
                                cart_product_amount = 0
                                is_product_chosen = product == choosen_product
                                for order_product, amount in order:
                                    if order_product == product:
                                        cart_product_amount += amount
                                print(f"{i + 1}. {Colors.YELLOW if is_product_chosen else ''}{product.name:<26}{Colors.RESET if is_product_chosen else ''} {Colors.BLUE}{'$':>2}{product.price:>6}{Colors.RESET}{Colors.CYAN}{product.quantity:>10}{Colors.RESET} {Colors.RED}{('- ' + str(cart_product_amount)) if cart_product_amount > 0 else ''}{Colors.RESET}")

                            print(f"\nChoosen Product: {Colors.YELLOW}{choosen_product.name}{Colors.RESET}")
                            amount_input = int(input(f"\nWhat {Colors.CYAN}amount{Colors.RESET} do you want? "))
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
                                    print(f"{Colors.RED}Amount not available{Colors.RESET}")
                                    time.sleep(1)



                    except ValueError:
                        if userinput == "":
                            if len(order) < 1:
                                break

                            print(f"Order made! Total payment: {Colors.BLUE}${store.order(order)}{Colors.RESET}")
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
