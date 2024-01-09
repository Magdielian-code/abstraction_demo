class Author:
    def __init__(self,name,book_name,pages):
        self.name = name
        self.book_name = book_name
        self.pages = pages

    def __str__(self):
        return f"{self.book_name} by {self.name}"
    
    def __len__(self):
        return f"{self.pages}"

Jane = Author("Jane", "HAlf the Sun", 1200) 
print(Jane)
print(len(Jane))