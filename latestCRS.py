from datetime import date
import sys

class carRental:
    def __init__(self, name='',  age= '', email='', pn= '',stock=10, car_type = '', num ='', days = '', car_brand="", option='',times = '', price=0,):

        print ("\n\n*****WELCOME TO ROSINA CAR RENTAL SERVICES*****\n")
        self.name=name
        self.age= age
        self.email= email
        self.pn = pn
        self.stock = stock
        self.car_type = car_type
        self.num = num
        self.days = days
        self.car_brand = car_brand
        self.option = option
        self.times = times
        self.price= price
        
        
    def Customerdata(self):
        self.name=input("\nEnter your Fullname: ")
        self.age= int(input("\nEnter your age here: "))
    
        while len(str(self.pn)) != 10:
            self.pn=int(input("\nEnter your registered phone number here: "))
            if len(str(self.pn)) != 10:
                print("Invalid Phone number! Enter a 10 digit number")
            else:
                None
           
        self.email=input("\nEnter your Email here: ")
        self.age_limit()
        

    def display_stock(self):
        print(f'Total number of cars available is for rent is {self.stock}')
        return self.stock
        

    def age_limit(self):
        if self.age < 18:
            print(f'Sorry {self.name}, you\'re {self.age} years and do not qualify to rent a car with us. Thank you')
        else:
            return None

    def price_list(self):
        carRental.display_stock(self)
        print("Our Updated Price List are Listed Below")
        print('1. TOYOTA CAMRY ===> $550.00 \n2. TOYOTA COROLLA ===> $550.00 \n3. TOYOTA AVENSIS ===> $650.00 \n4. TOYOTA LAND CRUISER ===> $850.00 \n5. TOYOTA PRAD0 ===> $850.00 \n6. LEXUS ===> $900.00 \n7. MERCEDES BENZ ===> $800.00 \n8. BMW ===> $800.00 \n9. RANGE ROVER ===> $1000.00 \n10. URVAN FAMILY BUS ===> $450.00 \n11. TRUCK ===> $450.00 ')

    def display_available_cars(self):
        print('THE FOLLOWING CARS ARE CURRENTLY AVAILABLE TO RENT')
        print('1. SALOON CAR')
        print('2. 4x4') 
        print('3. SPORTS CAR') 
        print('4. URVAN FAMILY BUS') 
        print('5. TRUCK ') 
        print('6. EXIT')

        self.car_type = int(input('KINDLY VISIT OUR MAIN MENU TO BOOK A CAR: '))
        
        if (self.car_type==1):
            print('1. TOYOTA CAMRY')
            print('2. TOYOTA COROLLA')
            print('3. TOYOTA AVENSIS')
            print('4. EXIT')
    
        elif (self.car_type==2):
            print('1. TOYOTA LAND CRUSOR')
            print('2. TOYOTA PRADO')
            print('3. LEXUS')
            print('4. EXIT')

        elif (self.car_type==3):
            print('1. BENZ')
            print('2. BMW')
            print('3. RANGE ROVER')
            print('4. EXIT')

        elif (self.car_type ==4):
            sys.exit()
        else:
            print("You've Enter an Invalid Key")

    def Daily(self):
        if self.num < 0:
            print('Invalid response, please enter a positive value')
            return None

        elif self.num > self.stock:
            print(f'Sorry, we currently have {self.stock} cars available for rent')
            return None

        else:
            now =  date.today()
            print(f'You have rented {self.num} {self.car_brand} on a daily basis at {now}')
            print(f'You will be charged ${self.price} per day')
            print('We hope you enjoy our service')
            self.stock = self.stock - self.num
            return now 

    def Weekly(self):
        if self.num < 0:
            print('Invalid response, please enter a positive value')
            return None

        elif self.num > self.stock:
            print(f'Sorry, we currently have {self.stock} cars available for rent')
            return None

        else:
            now =  date.today()
            print(f'You have rented {self.num} {self.car_brand} on a weekly basis at {now}')
            print(f'You will be charged ${self.price} per week ')
            print('We hope you enjoy our service')
            self.stock = self.stock - self.num
            return now

    def Monthly(self):
        if self.num < 0:
            print('Invalid response, please enter a positive value')
            return None

        elif self.num > self.stock:
            print(f'Sorry, we currently have {self.stock} cars available for rent')
            return None

        else:
            now =  date.today()
            print(f'You have rented {self.num} {self.car_brand} on daily a monthly at {now}')
            print(f'You will be charged ${self.price} per month')
            print('We hope you enjoy our service')
            self.stock = self.stock - self.num
            return now

    def requestCar(self):
        print('THE FOLLOWING CARS ARE CURRENTLY AVAILABLE TO RENT')
        print('1. SALOON CAR')
        print('2. 4x4') 
        print('3. SPORTS CAR') 
        print('4. URVAN FAMILY BUS') 
        print('5. TRUCK ') 
        print('6. EXIT')
        self.car_type = int(input('Enter a car of your choice please: '))
        
        if (self.car_type==1):
            print('1. TOYOTA CAMRY')
            print('2. TOYOTA COROLLA')
            print('3. TOYOTA AVENSIS')
            print('4. EXIT')
    
            self.car_brand = int(input('select a brand you want to rent: '))
            if (self.car_brand ==1):
                print('You have requested to ride in a Toyota Camry')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price = self.price + int(550)
                self.car_brand = "Toyota Camry"

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                elif (self.option ==4):
                    sys.exit()

                else:
                    print('You have entered an Invalid Option')


            elif (self.car_brand ==2):
                print('You have requested to ride in a Toyota Corolla')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price = self.price + int(550)
                self.car_brand = "Toyota Corolla"    

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                else:
                    sys.exit()


            if (self.car_brand ==3):
                print('You have requested to ride in a Toyota Avensis')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price = self.price + int(650)
                self.car_brand = "Toyata Avensis"

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                else:
                    sys.exit()

            elif (self.car_type==4):
                sys.exit()
        
        elif (self.car_type==2):
            print('1. TOYOTA LAND CRUISER')
            print('2. TOYOTA PRADO')
            print('3. LEXUS')
            print('4. EXIT')
    
            self.car_brand = int(input('Select a brand you want to rent: '))
            if (self.car_brand ==1):
                print('You have requested to ride in a Toyota Land Cruiser')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price = self.price + int(850)
                self.car_brand = "Toyota Land Cruiser"

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                else:
                    sys.exit()

            
            elif (self.car_brand ==2):
                print('You have requested to ride in a Toyota PRADO')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price = self.price + int(750)
                self.car_brand = "Toyota Prado"

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                else:
                    sys.exit()


            elif (self.car_brand ==3):
                print('You have requested to ride in a LEXUS')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price = self.price + int(900)
                self.car_brand = "Lexus"

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                else:
                    sys.exit()


            elif (self.car_type==4):
                sys.exit()

        elif (self.car_type==3):
            print('1. MERCEDES BENZ')
            print('2. BMW')
            print('3. RANGE ROVER')
            print('4. EXIT')
    
            self.car_brand = int(input('Select a brand of sport car you want to rent: '))
            if (self.car_brand ==1):
                print('You have requested to ride in a BENZ')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price= self.price + int(800)
                self.car_brand = "Mercedes Benz"

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                else:
                    sys.exit()

            
            elif (self.car_brand ==2):
                print('You have requested to ride in a BMW')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price = self.price + int(800)
                self.car_brand = "BMW"

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                else:
                    sys.exit()


            elif (self.car_brand ==3):
                print('You have requested to ride in a RANGE ROVER')
                print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
                self.option = int(input('Enter an option to select: '))
                self.num = int(input('Enter number of cars to rent: '))
                self.price = self.price + int(1000)
                self.car_brand = "Range Rover"

                if (self.option ==1):
                    carRental.Daily(self)
                     
                elif (self.option ==2):
                    carRental.Weekly(self)

                elif (self.option ==3):
                    carRental.Monthly(self)

                else:
                    sys.exit()

        elif (self.car_type==4):
            print('You have requested to ride in a URVAN FAMILY BUS')
            print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('Enter number of cars to rent: '))
            self.price = self.price + int(450)
            self.car_brand = "Urvan Family Bus"

            if (self.option ==1):
                carRental.Daily(self)
                    
            elif (self.option ==2):
                carRental.Weekly(self)

            elif (self.option ==3):
                carRental.Monthly(self)

            else:
                sys.exit()


        elif (self.car_type==5):
            print('You have requested to ride in a TRUCK')
            print('HOW LONG DO YOU WISH TO KEEP YOUR RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('Enter number of cars to rent: '))
            self.price = self.price + int(450)
            self.car_brand = "Truck"

            if (self.option ==1):
                carRental.Daily(self)
                    
            elif (self.option ==2):
                carRental.Weekly(self)

            elif (self.option ==3):
                carRental.Monthly(self)

            else:
                sys.exit()


        elif (self.car_type==6):
                sys.exit()


    def bill(self):
        print(' WHAT CAR DID YOU RENT\n')
        print('1. CAMRY \n2. COROLLA \n3. AVENSIS \n4. LAND CRUISER \n5. PRADO \n6. AVENSIS \n7. BENZ \n8. BMW \n9. RANGE ROVER \n10. URVAN FAMILY BUS \n11. TRUCK \n12. EXIT')
    
        self.car_brand = int(input('Select the car requested for here: '))
        if (self.car_brand ==1):
            print('You requested to ride in a Toyota Camry')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(550)
            self.car_brand = "Toyota Camry"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')

        elif (self.car_brand ==2):
            print('You requested to ride in a Toyota Corolla')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(550)
            self.car_brand = "Toyota Corolla"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')        


        elif (self.car_brand ==3):
            print('You requested to ride in a Toyota Avensis')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(650)
            self.car_brand = "Toyota Avensis"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')
        
        elif (self.car_brand ==4):
            print('You requested to ride in a Toyota Land Cruiser')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(850)
            self.car_brand = "Toyota Land Cruiser"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')

        if (self.car_brand ==5):
            print('You requested to ride in a Toyota PRADO')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(750)
            self.car_brand = "Toyota Prado"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')

        elif (self.car_brand ==6):
            print('You requested to ride in a LEXUS')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(900)
            self.car_brand = "Lexus"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')

        if (self.car_brand ==7):
            print('You requested to ride in a BMW')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(800)
            self.car_brand = "BMW"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')        

        
        if (self.car_brand ==8):
            print('You requested to ride in a BENZ')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(800)
            self.car_brand = "Mercedes Benz"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')

        elif (self.car_brand ==9):
            print('You requested to ride in a RANGE ROVER')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(1000)
            self.car_brand = "Range Rover"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')

        elif (self.car_brand ==10):
            print('You requested to ride in a URVAN FAMILY BUS')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(450)
            self.car_brand = "Urvan Family Bus"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')

        elif (self.car_brand ==11):
            print('You requested to ride in a TRUCK')
            print('HOW LONG DID YOU KEEP THE RIDE \n1. DAILY \n2. WEEKLY \n3. MONTHLY ' )
            self.option = int(input('Enter an option to select: '))
            self.num = int(input('How many cars did you request for: '))
            self.price = int(450)
            self.car_brand = "TRUCK"

            if (self.option ==1):
                self.times= int(input('Enter the number of days ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)}')
            
            elif (self.option ==2):
                self.times= int(input('Enter the number of weeks ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*7}')

            elif (self.option ==3):
                self.times= int(input('Enter the number of months ride was rented: '))
                carRental.Daily(self)
                print(f'YOUR BILL IS: ${(self.times)*(self.price)*(self.num)*28}')

            else:
                print(' Invalid Response')

        
        elif(self.car_brand == 12):
            sys.exit()

        else:
            print('INVALID RESPONSE')

def main():

    a = carRental()

    while(1):
        print("1. Enter Customer Data")
        
        print("2. Display Car Available for rent")

        print("3. Display Price List")

        print("4. Rent a Car")

        print("5. Calculate Car Bill")

        print("6. EXIT")

        b=int(input("\nEnter the number of your choice: "))
        if (b==1):
            a.Customerdata()

        elif (b==2):

            a.display_available_cars()

        elif (b==3):

            a.price_list()

        elif (b==4):

            a.requestCar()

        elif (b==5):
            a.bill()

        elif (b==6):

            quit()

        else:
            print("You've Enter an Invalid Key")



main()