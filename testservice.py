from serviceCost import ServiceCost, Customer

def main():
    shop = ServiceCost(100)
    customer = Customer()

    while True:
        print("""
        ====== Docker Delivery Service =======
        1. Display available dockers
        2. Request a docker on per second basis $0.5
        3. Request a docker on per minute basis $20
        4. Request a docker on per hour basis $500
        5. Return a docker
        6. Exit
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.displaydocker()
        
        elif choice == 2:
            customer.rentalTime = shop.rentDockerOnSecondBasis(customer.requestContainer())
            customer.rentalBasis = 1

        elif choice == 3:
            customer.rentalTime = shop.rentDockerOnMinuteBasis(customer.requestContainer())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.rentDockerOnHourBasis(customer.requestContainer())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnDocker(customer.returnContainer())
            customer.rentalBasis, customer.rentalTime, customer.containers = 0,0,0        
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")        
    print("Thank you for using the docker rental system.")


if __name__=="__main__":
    main()
