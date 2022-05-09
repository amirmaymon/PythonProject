#project by: Nadav Ido, Inbar Ginat

from Library import Library
import pickle

textDivider = "-"*50

#looking for and opening an existing save file
try:
    f = open('mysavefile.txt', 'rb')
    lib = pickle.load(f)
    f.close()
except:
    print('save File not found or could not be opened.')
    lib = Library()

#we decided to build each library in her own timeline to help with testing and skipping days
#welcoming the librerian and telling him the systems date
lib.newDayMsg()

#starting the work
working = True
while(working):

#menu(not trasting input):
    try:    
        menuChoice =  int(input(f"""{textDivider}
            choose action:
            1.Add a new customer
            2.Add a new book 
            3.Loan a book
            4.return a book
            5.Display all books
            6.Display all customers
            7.Display all loans
            8.Display late loans
            9.Display loans by customer
            10.Display loans by book
            11.Display book details
            12.Display customer details
            13.Remove book
            14.Remove customer
            15.skip a day           
            16.skip 2 days
            17.skip a week
            0.exit
{textDivider}
            """))
    #if exception don't do anyting
    except:
        menuChoice = -1
        print("not a valid number choice")
    print(textDivider)
    #sending choices to functions:

    #1.Add a new customer
    if(menuChoice == 1):
        lib.addNewCustomer()
    #2.Add a new book
    elif(menuChoice == 2):
        lib.addNewBook()
    #3.Loan a book
    elif(menuChoice == 3):
        lib.loanABook()
    #4.return a book
    elif(menuChoice == 4):
        lib.ReturnABook()
    #5.Display all books
    elif(menuChoice == 5):
        lib.DisplayAllBooks()
    #6.Display all customers
    elif(menuChoice == 6):
        lib.DisplayAllCustomers()
    #7.Display all loans
    elif(menuChoice == 7):
        lib.DisplayAllLoans()
    #8.Display late loans
    elif(menuChoice == 8):
        lib.DisplayLateLoans()
    #9.Display loans by customer
    elif(menuChoice == 9):
        lib.DisplayLoansByCustomer()
    #10.Display loans by book
    elif(menuChoice == 10):
        lib.DisplayLoansByBook()
    #11.Display book details
    elif(menuChoice == 11):
        lib.DisplayBookDetails()
    #12.Display customer details
    elif(menuChoice == 12):
        lib.DisplayCustomerDetails()
    #13.Remove book
    elif(menuChoice == 13):
        lib.RemoveBook()
    #14.Remove customer
    elif(menuChoice == 14):
        lib.RemoveCustomer()
    #timeskips:
    #restricting time jumps to set times avoid user nonsence
    elif(menuChoice == 15):
        lib.skipDays(1)
    elif(menuChoice == 16):
        lib.skipDays(2)
    elif(menuChoice == 17):
        lib.skipDays(7)
    #leaving and saving
    elif(menuChoice == 0):
        working = False
        print("have a nice day")
        fil = open('mysavefile.txt', 'wb')
        pickle.dump(lib, fil)
        fil.close()
        
        