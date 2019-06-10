import datetime

class ServiceCost:
    
    def __init__(self,dockers=0):
        """
        Our constructor class that instantiates Service Cost Billing.
        """

        self.dockers = dockers

    def displaydocker(self):
        """
        Displays the dockers currently available for the particular service.
        """

        print("We have currently {} Services available.".format(self.dockers))
        return self.dockers

    def rentDockerOnSecondBasis(self, n):
        """
        Rents a docker on second basis to a customer.
        """
        if n <= 0:
            print("Number of dockers should be positive!")
            return None
        
        elif n > self.dockers:
            print("Sorry! We have currently {} dockers available to rent.".format(self.dockers))
            return None
        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} docker(s) on second basis today at {} seconds.".format(n,now.second))
            print("You will be charged $0.5 for each second per docker.")
            print("We hope that you enjoy our service.")

            self.dockers -= n
            return now      
     
    def rentDockerOnMinuteBasis(self, n):
        """
        Rents a docker on minute basis to a customer.
        """
        if n <= 0:
            print("Number of dockers should be positive!")
            return None

        elif n > self.dockers:
            print("Sorry! We have currently {} dockers available to rent.".format(self.dockers))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} docker(s) on minute basis today at {} minute.".format(n, now.minute))
            print("You will be charged $20 for each minute per docker.")
            print("We hope that you enjoy our service.")

            self.dockers -= n
            return now
        
    def rentDockerOnHourBasis(self, n):
        """
        Rents a docker on hourly basis to a customer.
        """
        if n <= 0:
            print("Number of dockers should be positive!")
            return None

        elif n > self.dockers:
            print("Sorry! We have currently {} dockers available to rent.".format(self.dockers))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("You have rented {} docker(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $500 for each hour per docker.")
            print("We hope that you enjoy our service.")
            self.dockers -= n

            return now
    

    
    def returnDocker(self, request):
        """
        1. Accept a rented container from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rentalTime, rentalBasis, numOfDockers = request
        bill = 0

        if rentalTime and rentalBasis and numOfDockers:
            self.dockers += numOfDockers
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
            mode = " "
        
            # Per second bill calculation
            if rentalBasis == 1:
                timeConsumed = round(rentalPeriod.seconds) 
                bill = timeConsumed  * .5 * numOfDockers
                mode = mode + "Seconds"
                
            # Per minute bill calculation
            elif rentalBasis == 2:
                timeConsumed = round(rentalPeriod.seconds / 60) 
                bill = timeConsumed  * 20 * numOfDockers
                mode = mode + "Minutes"
                
            # Per hour bill calculation
            elif rentalBasis == 3:
                timeConsumed = round(rentalPeriod.seconds / 3600) 
                bill = timeConsumed  * 500 * numOfDockers
                mode = mode + "Hours"
            
               
            if (3 <= numOfDockers <= 5):
                print("You are eligible for promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for using our docker. Hope you enjoyed our service!")
            print("You consumed {}{} That would cost you ${}".format(timeConsumed, mode , bill))
            return bill
        else:
            print("Are you sure you rented a docker with us?")
            return None



class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.containers = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    
    def requestContainer(self):
        """
        Takes a request from the customer for the number of dockers.
        """
                      
        containers = input("How many containers would you like to rent?")
        try:
            containers = int(containers)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if containers < 1:
            print("Invalid input. Number of containers should be greater than zero!")
            return -1
        else:
            self.containers = containers
        return self.containers
     
    def returnContainer(self):
        """
        Allows customers to return their containers to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.containers:
            return self.rentalTime, self.rentalBasis, self.containers  
        else:
            return 0,0,0
	
