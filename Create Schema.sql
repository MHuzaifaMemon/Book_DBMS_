CREATE SCHEMA Book_Database_Management_System;
CREATE TABLE Book (
  ISBN varchar(255) PRIMARY KEY,
  title varchar(255) NOT NULL,
  publication_date date NOT NULL,
  summary text,
  publisher_id int NOT NULL,
  FOREIGN KEY (publisher_id) REFERENCES Publisher(publisher_id)
);

CREATE TABLE Author (
  author_id int PRIMARY KEY AUTO_INCREMENT,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL,
  DOB Date
);

CREATE TABLE Publisher (
  publisher_id int PRIMARY KEY AUTO_INCREMENT,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL
);


CREATE TABLE User (
  user_id int PRIMARY KEY AUTO_INCREMENT,
  username varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  password varchar(255) NOT NULL,
  date_joined datetime NOT NULL
);

CREATE TABLE Rating (
  rating_id int PRIMARY KEY AUTO_INCREMENT,
  rating_value int NOT NULL
);

CREATE TABLE Genre (
  genre varchar(255) NOT NULL,
  ISBN varchar(255) PRIMARY KEY,
  FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);

CREATE TABLE Authored (
  ISBN varchar(255) PRIMARY KEY,
  author_id int NOT NULL,
  FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
  FOREIGN KEY (author_id) REFERENCES Author(author_id)
);


CREATE TABLE Owned_by (
  ISBN varchar(255) PRIMARY KEY,
  user_id int NOT NULL,
  FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
  FOREIGN KEY (user_id) REFERENCES User(user_id)
);


CREATE TABLE Reviewed_by (
  ISBN varchar(255) PRIMARY KEY,
  user_id int NOT NULL,
  FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
  FOREIGN KEY (user_id) REFERENCES User(user_id)
  );

CREATE TABLE Location (
  location varchar(255) NOT NULL,
  publisher_id int PRIMARY KEY,
  FOREIGN KEY (publisher_id) REFERENCES Publisher(publisher_id)
);

CREATE TABLE Rackings_of (
  ISBN varchar(255) PRIMARY KEY,
  user_id int NOT NULL,
  rating_id int NOT NULL,
  FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
  FOREIGN KEY (user_id) REFERENCES User(user_id),
  FOREIGN KEY (rating_id) REFERENCES Rating(rating_id)
);
