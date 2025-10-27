DESCRIBE salesman;

INSERT INTO salesman (salesman_id, salesman_name, salesman_city, commission)
VALUES
(5001, 'James Hoog', 'New York', 15),
(5002, 'Nail Knite', 'Paris', 13),
(5005, 'Pit Alex', 'London', 11),
(5006, 'McLyon', 'Paris', 14),
(5007, 'Paul Adam', 'Rome', 13),
(5003, 'Lauson Hen', 'San Jose', 12);

SELECT salesman_id, salesman_city FROM salesman;

SELECT * FROM salesman
WHERE salesman_city = 'Paris';

SELECT salesman_id, commission FROM salesman
WHERE salesman_name = 'Paul Adam';