class Loans:
    #loans object keeps the relevant dates and the keys for the related objects
    def __init__(self, customer_id, book_name, loandate, returndate):
        self.customer_id = customer_id
        self.book_name = book_name
        self.loandate = loandate
        self.returndate = returndate

    #getters
    def customer_id (self):
        return self.customer_id
    def book_name (self):
        return self.book_name
    def loandate (self):
        return self.loandate
    def returndate (self):
        return self.returndate
        
    #defining how to display loans as text
    def __str__(self):
        text = (f"""
        customer id: {self.customer_id}
        book name: {self.book_name}
        loan date: {self.loandate} | return date: {self.returndate}""")
        return text
        