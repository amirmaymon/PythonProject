
class Customers:
    #keeps customer info and a list of loans
    def __init__(self, id, name, city, age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age
        self.customer_loans = []

    #getters
    def getId (self):
        return self.id
    def getName (self):
        return self.name
    def getCity (self):
        return self.city
    def getAge (self):
        return self.age
    def getLoans (self):
        return self.customer_loans
    #returns number of active loans
    def numOfLoans(self):
        return len(self.customer_loans)

    #checks if allowed to loan from the customers side(by the number of active loans)
    def canLoan(customer):
        booksBorrowed = customer.numOfLoans()
        if booksBorrowed>2:
            print("you already have 3 books, please return them before taking another one")
            return False
        else:
            return True

    #update loans list:
    def loan(self,loan):
        self.customer_loans.append(loan)
    
    #shows the active loans and lets the user choose which one he wants to return:
    #pops the choise from the customers info and returns the entire object to use in modules
    def retLoan(self):
        #first displays all active loans
        self.DisplayLoansByCustomer()
        #asks for the user who to return first, and deciding for him if the input doesn't fit
        try:
            index = int(input("who are you returning? (0,1,2): "))  #is it an integer?
            if (index<0 or index>=self.numOfLoans()):       #is it a legal choice or just a random number? 
                index = Customers.decidingForCustomer()
        except:
            index = Customers.decidingForCustomer()
        #pops the loan chosen and sends it back:
        returnedLoan = self.customer_loans.pop(index)
        return returnedLoan

    #defining how to display customers information as text
    def __str__(self):
        text = (f"""
        customer id: {self.id} | customer name: {self.name}
        customer city: {self.city} | customer age: {self.age}
        """)
        return text

    #prints the customers active loans:
    def DisplayLoansByCustomer(self):
        numOfLoans = self.numOfLoans()
        i=0
        print(f"you have {numOfLoans} loans:")
        for l in self.customer_loans:
            print (f"{i}.{l}")
            i+=1

    #uses FIFO to decide for the user which book to return if user gives randoom input
    #(in the "story" the librarian is tired of people not following instructions and not returning their books in time)
    def decidingForCustomer():
        print("not a valid choice, i'm taking the first book i can find as punishment for wasting my time")
        return 0