from Books import Books as Book
from Customers import Customers
from Loans import Loans
from datetime import datetime, timedelta


class Library():
    #basic init, dictionerys for customers and books and lists for loans
    #also keeps a dictionery of banned people by id: {'id':date of ban ending}
    #keeps the date in the local timeline 
    def __init__(self):
        self.books_list = {}
        self.customers_list = {}
        self.loans_list = [] 
        self.banned_list = {}
        self.day = datetime.today().date()  
    
    #creates customer
    #gets information from user and use it to create and add a new customer to the dict
    def addNewCustomer(self):
        #asks user for id
        new_customer_id = Library.getIdFromUser()   
        #checks if the id already exist in the systems list, and asks the user how to continue if already in use.
        while (new_customer_id in self.customers_list):    
            idChoice = input("""id already in the system,
            would you like to use another id or exit?
            1.use another
            0.exit
            """)
            #we assume the user wants to continue unless he specificaly choses to exit
            if idChoice == '0':
                return
            new_customer_id = Library.getIdFromUser()
        new_customer_name = input("Enter your customer name: ")
        new_customer_city = input("Enter your customer city: ")
        #customer age isn't used so can be saved as text 
        new_customer_age = input("Enter your customer age: ")
        #create customer object and save in the librarys list
        self.customers_list[new_customer_id] = (Customers(new_customer_id, new_customer_name, new_customer_city, new_customer_age))
        print(f"customer {new_customer_name} is registerd")

    #create book
    #gets information to make a book and put it in the library list
    def addNewBook(self):
        #ask for book name
        new_book_name = input("Enter your book name: ")
        #book names are unique, if the name is alredy in system it means the book is already in the system.
        if(new_book_name in self.books_list):
            #in that case ask user if he wants to just add more copies to an existig book storage      
            try:
                bookChoice = int(input("""
                book already in the system,
                would you like to add more copies or exit?
                1.add
                0.exit
                """))
            except:
                bookChoice = 0
            #add extra copies
            if bookChoice == 1:
                try:
                    moreBooks = int(input("enter how many copies you would like to add? "))
                except:
                    moreBooks = 0
                book = self.books_list[new_book_name]
                Book.add_copies(book,moreBooks)
                print(f"""added {moreBooks} more copies of "{new_book_name}""")
            return
        #if the book is new get the rest of the information to build it
        new_book_author = input("Enter your book author: ")
        new_book_year_published = input("Enter your book year published: ")
        #get book type
        try:
            new_book_type = int(input("Enter your book type (1/2/3): "))
        except:
            print("set to defualt = 1")
            new_book_type = 1
        #get number of copies
        try:
            new_book_number_of_copies = int(input("Enter your book number of copies: "))
        except:
            print("set to defualt = 1")
            new_book_number_of_copies = 1
        #create the book and store in the list
        self.books_list[new_book_name] = (Book(new_book_name, new_book_author,new_book_year_published,new_book_type, new_book_number_of_copies))
        print(f"new book stocked: {self.books_list[new_book_name]}")
    

    #checking all conditions and creating loans
    def loanABook(self):
        #get id
        customer_id = Library.getIdFromUser()
        #check if the customer appears in the system
        if customer_id not in self.customers_list:
            print("customer not registerd, please sign up before loaning books")
            return
        #check if the customer isn't banned 
        if customer_id in self.banned_list:
            #checks if the ban date has passed
            if (self.banned_list[customer_id] > self.day):
                #still banned -> go back to menu
                print("sorry you are still banned")
                return
            #if passed we can remove from the ban list and continue
            else:
                print("your bann has passed, feel free to get books")
                self.banned_list.pop(customer_id, None)
        #ask what book and check if exist:
        book_name = input("Enter book name: ")
        if book_name not in self.books_list:
            print("book is not avalable")
            return
        #get the objects for the book and customer to work on them
        customer = self.customers_list[customer_id]
        book = self.books_list[book_name]
        #translate from book type to loan time
        bookTime = Book.get_maximum_loan_time(book)
        #call for objects internal tests and actions(amounts of loans and books)
        if Customers.canLoan(customer) and Book.loanOne(book):
            #if all is well crate the loan object
            newLoan = Loans(customer_id,book_name,self.day,self.day+timedelta(days=bookTime))
            #store th loan in both customer and library lists
            Customers.loan(customer, newLoan)
            self.loans_list.append(newLoan)
            #print the results
            print(f"new loan created:")
            print(newLoan)

    #returns the book: calls other functions that choose what book to return and change objects information acordenly
    def ReturnABook(self):
        #get id
        customer_id = Library.getIdFromUser()
        #check if registerd
        try:
            customer = self.customers_list[customer_id]
        except:
            print("customer not found")
            return
        #check if has loans
        if Customers.numOfLoans(customer) == 0:
            print("you have no loans to return, go home")
            return
        #calls a function that lets the customer choose what to return
        #it also removes it from customer and returns the full loan object
        loanreturned = Customers.retLoan(customer)
        loanBookName = Loans.book_name(loanreturned)
        #update number of copies:
        Book.add_copies(self.books_list[loanBookName],1)
        print(f"you returned {loanBookName} to the library")
        #did they return the book on time?
        if Loans.returndate(loanreturned) < self.day:   
            self.banned_list[customer_id] = self.day+timedelta(weeks=2)
            print("you missed the return date! you are now banned for 2 weeks.")
        #finaly removes loan from library list 
        self.loans_list.remove(loanreturned)

    #goes through the dict of books and prints one by one
    def DisplayAllBooks(self):
        if len(self.books_list)==0:
            print("no books in the system currently")
            return
        print("BOOKS:")
        for b in self.books_list:
            print (self.books_list[b])

    #goes through the dict of customers and prints one by one
    def DisplayAllCustomers(self):
        print("those are the customers:")
        if len(self.customers_list)==0:
            print("no customers in the system currently")
            return
        print("CUSTOMERS:")
        for c in self.customers_list:
            print (self.customers_list[c])

    #goes through the list of loans and prints one by one
    def DisplayAllLoans(self):
        if len(self.loans_list)==0:
            print("no loans in the system currently")
            return
        print("LOANS:")
        for l in self.loans_list:
            print(l)

    #goes through the list of loans and one by one check if expired,
    #prints them and banns the customer for 2 weeks
    def DisplayLateLoans(self):
        isEmpty = True
        for l in self.loans_list:
            if Loans.returndate(l) < self.day:
                print (l)
                #if discoverd someon late ban him
                customer_id = Loans.customer_id(l)
                self.banned_list[customer_id]=(self.day+timedelta(weeks=2))
                isEmpty = False
        if isEmpty:
            print("no late loans found")

    #get user -> print his loans list
    def DisplayLoansByCustomer(self):
        #get user id
        customer_id = Library.getIdFromUser()
        #check if id is registerd:
        try:
            customer = self.customers_list[customer_id]
        except:
            print("customer not found")
            return
        #call customer class func to print his loans
        Customers.DisplayLoansByCustomer(customer)

    #get book name -> go trough all the loans  and prints the ones of this book
    def DisplayLoansByBook(self):
        noLoans = True
        bookName = input("Enter book name: ")
        for l in self.loans_list:
            if Loans.book_name(l) == bookName:
                print(l)
                noLoans = False
        if noLoans:
            print("no loans found for this book")

    #gets book name ->  prints it
    def DisplayBookDetails(self):
        bookName = input("Enter book name: ")
        if bookName in self.books_list:
            print(self.books_list[bookName])
        else:
            print("book not found")

    #gets customer id  prints it
    def DisplayCustomerDetails(self):
        customer_id = Library.getIdFromUser()
        if customer_id in self.customers_list:
            print(self.customers_list[customer_id])
        else :
            print("customer not found")

    #serches for relevant book loans and removes book if allowed
    def RemoveBook(self):
        #get book name
        bookName = input("Enter the name of the book you want to remove: ")
        if bookName not in self.books_list:
            print("book does not exist")
            return
        #check all loans for loans with this book
        for l in self.loans_list:
            if (Loans.book_name(l)==bookName):
                print(f"this book is still loaned and cannot be removed:{l}")
                return
        #if no loans found pop it
        self.books_list.pop(bookName)
        print(f"you have successfuly removed '{bookName}'from the library")

    #checks if the customers have active loans and only delete him if non are active
    def RemoveCustomer(self):
        customer_id = Library.getIdFromUser()
        if customer_id not in self.customers_list:
            print("customer not found")
            return
        #check loans status
        else:
            customer = self.customers_list[customer_id]
            loansLeft = Customers.numOfLoans(customer)
            if loansLeft > 0:
                print(f"the customer still has {loansLeft} books and cannot be deleated")
                return
            else:
                print(f"this customer will now be removed: {customer}")
                self.customers_list.pop(customer_id)

    #"in-game" time menegment
    def skipDays(self,SDays = 1):
        timeJump = timedelta(days = SDays)
        self.day += timeJump
        self.newDayMsg()

    #welcoming the user
    def newDayMsg(self):
        print("welcome to the library")
        print(f"today is {self.day} (in-game time)") 
    
    #asks for id and checks legality
    def getIdFromUser():
        while True:     #making sure id is valid
            try:
                new_customer_id = int(input("Enter your customer id: "))
                return new_customer_id
            except:
                print("please enter a valid number id")

