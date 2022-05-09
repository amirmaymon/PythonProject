class Books:
    #books as a class mainly keeps dry information
    def __init__(self, name, author, year_published, type, copy_nums):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.type = type
        self.copy_nums = copy_nums      #number of copies in the library

        #getters
    def get_name (self):
        return self.name
    def get_author (self):
        return self.author
    def get_year_published (self):
        return self.year_published
    def grt_type (self):
        return self.type
    def get_copy_nums (self):
        return self.copy_nums
    
    #adds copies to library
    def add_copies (self,copies=0):
        self.copy_nums += copies

    #translates book type to loaning days
    def get_maximum_loan_time (self):
        if self.type == 1:
            return 10
        if self.type == 2:
            return 5
        if self.type == 3:
            return 2

    #the book side of loaning a book:
    #checks inventory for book and updates acordinly
    def loanOne(book):
        if (book.copy_nums>0):
            book.copy_nums -= 1
            return True
        else:
            print("out of stock")
            return False

    #defining how to display boos as text
    def __str__(self):
        text = f"""
        name: {self.name} | author: {self.author} | year published: {self.year_published}
        copies: {self.copy_nums} | rent time: {self.type}
        """
        return text




    
    






    
