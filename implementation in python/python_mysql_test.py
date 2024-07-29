import mysql.connector

# Establishing the connection to the MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="Clint Work",  # Use the username you created
        password="root",  # Use the password you assigned to the user
        database="Book_Database_Management_System"
    )

    print("Connected to MySQL database successfully!")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")
    exit(1)

# Creating a cursor object to execute SQL queries
cursor = conn.cursor()

# Example query: Inserting data into the Author table
insert_author_query = """
INSERT INTO Author (first_name, last_name, DOB)
VALUES (%s, %s, %s)
"""
author_data = ("John", "Doe", "1980-01-01")
cursor.execute(insert_author_query, author_data)
conn.commit()
print("Data inserted into Author table successfully!")

# Example query: Inserting data into the Publisher table
insert_publisher_query = """
INSERT INTO Publisher (first_name, last_name)
VALUES (%s, %s)
"""
publisher_data = ("Sample", "Publisher")
cursor.execute(insert_publisher_query, publisher_data)
conn.commit()
print("Data inserted into Publisher table successfully!")

# Example query: Inserting data into the User table
insert_user_query = """
INSERT INTO User (username, email, password, date_joined)
VALUES (%s, %s, %s, %s)
"""
user_data = ("user1", "user1@example.com", "password123", "2024-05-12")
cursor.execute(insert_user_query, user_data)
conn.commit()
print("Data inserted into User table successfully!")

# Example query: Inserting data into the Rating table
insert_rating_query = """
INSERT INTO Rating (rating_value)
VALUES (%s)
"""
rating_data = (5,)
cursor.execute(insert_rating_query, rating_data)
conn.commit()
print("Data inserted into Rating table successfully!")

# Example query: Inserting data into the Book table
insert_book_query = """
INSERT INTO Book (ISBN, title, publication_date, summary, publisher_id)
VALUES (%s, %s, %s, %s, %s)
"""
book_data = ("978-3-16-148410-0", "Sample Book", "2024-05-12", "This is a sample summary.", 1)
cursor.execute(insert_book_query, book_data)
conn.commit()
print("Data inserted into Book table successfully!")

# Example query: Inserting data into the Authored table
insert_authored_query = """
INSERT INTO Authored (author_id, ISBN)
VALUES (%s, %s)
"""
authored_data = (1, "978-3-16-148410-0")
cursor.execute(insert_authored_query, authored_data)
conn.commit()
print("Data inserted into Authored table successfully!")

# Example query: Inserting data into the Owned_by table
insert_owned_by_query = """
INSERT INTO Owned_by (user_id, ISBN)
VALUES (%s, %s)
"""
owned_by_data = (1, "978-3-16-148410-0")
cursor.execute(insert_owned_by_query, owned_by_data)
conn.commit()
print("Data inserted into Owned_by table successfully!")

# Example query: Inserting data into the Reviewed_by table
insert_reviewed_by_query = """
INSERT INTO Reviewed_by (user_id, ISBN)
VALUES (%s, %s)
"""
reviewed_by_data = (1, "978-3-16-148410-0")
cursor.execute(insert_reviewed_by_query, reviewed_by_data)
conn.commit()
print("Data inserted into Reviewed_by table successfully!")

# Example query: Inserting data into the Rackings_of table
insert_rankings_of_query = """
INSERT INTO Rackings_of (ISBN, user_id, rating_id)
VALUES (%s, %s, %s)
"""
rankings_of_data = ("978-3-16-148410-0", 1, 1)
cursor.execute(insert_rankings_of_query, rankings_of_data)
conn.commit()
print("Data inserted into Rackings_of table successfully!")

# Example query: Retrieving data from the Book table
select_book_query = "SELECT * FROM Book"
cursor.execute(select_book_query)
books = cursor.fetchall()

print("\nBooks in the database:")
for book in books:
    print(book)

# Example query: Retrieving data from the Author table
select_author_query = "SELECT * FROM Author"
cursor.execute(select_author_query)
authors = cursor.fetchall()

print("\nAuthors in the database:")
for author in authors:
    print(author)

# Example query: Retrieving data from the Publisher table
select_publisher_query = "SELECT * FROM Publisher"
cursor.execute(select_publisher_query)
publishers = cursor.fetchall()

print("\nPublishers in the database:")
for publisher in publishers:
    print(publisher)

# Example query: Retrieving data from the User table
select_user_query = "SELECT * FROM User"
cursor.execute(select_user_query)
users = cursor.fetchall()

print("\nUsers in the database:")
for user in users:
    print(user)

# Example query: Retrieving data from the Rating table
select_rating_query = "SELECT * FROM Rating"
cursor.execute(select_rating_query)
ratings = cursor.fetchall()

print("\nRatings in the database:")
for rating in ratings:
    print(rating)

# Closing cursor and connection
cursor.close()
conn.close()

