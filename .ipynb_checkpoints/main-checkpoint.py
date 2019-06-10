{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'bikeRental'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-258bfee5e694>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mbikeRental\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mBikeRental\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mCustomer\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mshop\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBikeRental\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0mcustomer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mCustomer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'bikeRental'"
     ]
    }
   ],
   "source": [
    "from bikeRental import BikeRental, Customer\n",
    "\n",
    "def main():\n",
    "    shop = BikeRental(100)\n",
    "    customer = Customer()\n",
    "\n",
    "    while True:\n",
    "        print(\"\"\"\n",
    "        ====== Bike Rental Shop =======\n",
    "        1. Display available bikes\n",
    "        2. Request a bike on hourly basis $5\n",
    "        3. Request a bike on daily basis $20\n",
    "        4. Request a bike on weekly basis $60\n",
    "        5. Return a bike\n",
    "        6. Exit\n",
    "        \"\"\")\n",
    "        \n",
    "        choice = input(\"Enter choice: \")\n",
    "        \n",
    "        try:\n",
    "            choice = int(choice)\n",
    "        except ValueError:\n",
    "            print(\"That's not an int!\")\n",
    "            continue\n",
    "        \n",
    "        if choice == 1:\n",
    "            shop.displaystock()\n",
    "        \n",
    "        elif choice == 2:\n",
    "            customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())\n",
    "            customer.rentalBasis = 1\n",
    "\n",
    "        elif choice == 3:\n",
    "            customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())\n",
    "            customer.rentalBasis = 2\n",
    "\n",
    "        elif choice == 4:\n",
    "            customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())\n",
    "            customer.rentalBasis = 3\n",
    "\n",
    "        elif choice == 5:\n",
    "            customer.bill = shop.returnBike(customer.returnBike())\n",
    "            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0        \n",
    "        elif choice == 6:\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid input. Please enter number between 1-6 \")        \n",
    "    print(\"Thank you for using the bike rental system.\")\n",
    "\n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
