import csv

book_file = open("books.csv",'rt')
book_names = csv.reader(book_file)

author_file = open("authors.csv",'rt')
author_names = csv.reader(author_file)


def main():
    book_list = []
    count = 0
    another_entry = 1

    print("----------Welcome to the book store!----------")
    print("________________________________________________\n")
    
    print("Here's our catalogue to explore around:")
    print("""
    1. Books
    2.Authors
    3.Book Reviews
    """)

    choice = int(input("Enter your choice: "))

    if choice ==1:
        print("""
1. Browse through the book catalogue.
2. Add books to the catalogue.
		""")
		
        user_input = int(input("Enter your choice as '1' or '2': "))
        
        if user_input == 1:
            print("Here's our Book catalogue:")
            
            for row in book_names:
                print("|\t",row[0],"|\t", row[1],"|\t", row[2],"|\t", row[3])
                print("______________________________________________________")
        
        elif user_input == 2:
            
            print("""While making the entries, stick to the following order: 
'Book_Id, Book_Name, Author_id, Year_of_publication'
			""")
            
            while another_entry != 0:
                while count<4:
                    user_in = input("Enter the entries for books: ")
                    book_list.append(user_in)
                    count += 1
                
                with open('books.csv','a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(book_list)
                
                another_entry = int(input("You wish to make another entry? Enter '1' for YES and '0' for NO."))

    
    if choice ==2:
        print("Here's our Authors catalogue:")
        for row in author_names:
            print("|\t",row[0]," |\t", row[1]," |\t", row[2])
            print("________________________________________________")


    
if __name__ == "__main__":
    main()

book_file.close()
author_file.close()