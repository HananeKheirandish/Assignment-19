INSERT INTO Customers
VALUES (1, 'Hana', 'Mashhad', 'Iran');

INSERT INTO Customers
VALUES (2, 'Negin', 'Colifornia', 'USA');


INSERT INTO Products
VALUES (1, 'Apple Watch', '16000000', '2');

INSERT INTO Products
VALUES (2, 'Tv-Sony', '80000000', '0');


SELECT * FROM Products WHERE count > 0;


DELETE FROM Customers WHERE country != 'Iran';


UPDATE Products SET price = price * 0.8;