import csv

from models import*

book_file = open("books.csv",'rt')
book_info = csv.reader(book_file)

author_file = open("authors.csv",'rt')
author_names = csv.reader(author_file)

review_file = open("reviews.csv",'rt')
book_reviews = csv.reader(review_file)


def main():

    #LISTS FOR STORING CSV FILE CONTENTS 
    book_list = []
    author_list = []
    review_list = []
    count = 0
    
    #LOOPING VARIABLES
    book_row_count = 4
    author_row_count = 3
    review_row_count = 3
    
    #WHILE LOOP VARIABLES
    another_book = 1
    another_author = 1
    another_review = 1
    
    print_messages()

    choice = int(input("Enter your choice: \t"))

    if choice == MainChoice.Books:
        print("""
        1. Browse through the book catalogue.
        2. Add books to the catalogue.
		""")
		
        book_input = int(input("Enter your choice as '1' or '2': "))
        
        if book_input == BookMenu.Browse:
            print("Here's our Book catalogue:")
            for row in book_info:
                book = Book(row[0],row[1],row[2],row[3])
                book.print()
        
        elif book_input == BookMenu.AddTo:
            
            print("""While making the entries, stick to the following order: 
        Book_Id, 
        Book_Name, 
        Author_id,
        Year_of_publication'
			""")
            
            while another_book != 0:
                while count< book_row_count:
                    user_in = input("Enter the entries for books: ")
                    book_list.append(user_in)
                    count += 1
                
                with open('books.csv','a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(book_list)
                
                another_book = int(input("You wish to make another entry? Enter '1' for YES and '0' for NO."))
    


    elif choice == MainChoice.Authors:
        print("""While making the entries, stick to the following order: 
            Author_Id, 
            First_Name, 
            Last_Name
			""")

        print("""
        1. Browse through the Author catalogue.
        2. Add Authors to the catalogue.
		""")
        
        author_input = int(input("Enter your choice as '1' or '2': "))
        
        if author_input == AuthorMenu.Browse:
           
            print("Here's our Authors catalogue:")
            for row in author_names:
                author = Author(row[0],row[1],row[2])
                author.print()
                
        elif author_input == AuthorMenu.AddTo:
            while another_author!=0:
                while count < author_row_count:
                    user_in = input("Enter your entries for Authors: ")
                    author_list.append(user_in)
                    count+=1
                
                with open('authors.csv','a')as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(author_list)
                
                another_author = int(input("You wish to make another entry? Enter '1' for YES and '0' for NO."))



    elif choice == MainChoice.BookReviews:
        print("""
        1. Browse through the Review Section.
        2. Add new Book Reviews to the catalogue.
		""")
        
        review_input = int(input("Enter your choice as '1' or '2': "))
        
        if review_input == ReviewMenu.Browse:
           
            print("Here's our Review Section:")
            for row in book_reviews:
                review = Review(row[0], row[1], row[2])
                review.print()
                
        elif review_input == ReviewMenu.AddTo:
            while another_review != 0:
                while count < review_row_count:
                    user_in = input("Enter your entries for Reviews: ")
                    review_list.append(user_in)
                    count+=1
                
                with open('reviews.csv','a')as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(review_list)
                
                another_review = int(input("You wish to make another entry? Enter '1' for YES and '0' for NO."))

    else:
        print("Enter a valid choice.")    


    
if __name__ == "__main__":
    main()

book_file.close()
author_file.close()