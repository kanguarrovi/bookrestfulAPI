DROP TABLE IF EXISTS books;
CREATE TABLE books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn VARCHAR(13) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    editorial VARCHAR(255) NOT NULL,
    date_edition VARCHAR(255) NULL,
    lenguage VARCHAR(255) NOT NULL,
    read BOOLEAN DEFAULT 0,
    info TEXT DEFAULT ""
);

INSERT INTO books(isbn, title, author, editorial, date_edition, lenguage)
VALUES('9788433920089', 'El almuerzo desnudo', 'William S. Burroughs', 'Anagrama', '06-2017', 'esp');
INSERT INTO books(isbn, title, author, editorial, date_edition, lenguage, info)
VALUES('9788497930994', 'Cementerio de animales', 'Stephen King', 'Debolsillo', '01-2013', 'esp', 'Nuevo');