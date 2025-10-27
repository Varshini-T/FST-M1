DESCRIBE salesman;

INSERT INTO salesman (salesman_id, salesman_name, salesman_city, commission)
VALUES
(5001, 'James Hoog', 'New York', 15),
(5002, 'Nail Knite', 'Paris', 13),
(5005, 'Pit Alex', 'London', 11),
(5006, 'McLyon', 'Paris', 14),
(5007, 'Paul Adam', 'Rome', 13),
(5003, 'Lauson Hen', 'San Jose', 12);

ALTER TABLE salesman
ADD grade INT;

-- Set the value in the grade column for everyone to 100
UPDATE salesman
SET grade = 100;

-- View updated table
SELECT * FROM salesman;