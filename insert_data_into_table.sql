CREATE TABLE employee(
         employee_id SERIAL PRIMARY KEY,
		 name VARCHAR(100) NOT NULL,
		 position VARCHAR(50),
		 department VARCHAR (50),
		 hire_date DATE,
		 salary NUMERIC(10,2)
		 
);

SELECT * FROM employee;


INSERT INTO employee( name, position, department, hire_date, salary )
            VALUES('Ram Kumar', 'data analyst', 'data science', '2022-05-12', 34000.90),
            ('Khushboo Rawat', 'human resource', 'IT', '2022-05-16', 34090.90),
			('Yashi Sahu', 'CA', 'company', '2022-05-16', 3780.90),
			('Yash Sharma', 'maketing', 'social media', '2022-05-31', 3400098.90),
			('Saurab Joshi', 'sales executive', 'sales', '2022-05-23', 358.90),
			('Elvish Yadav', 'python programmer', 'machine learning', '2022-05-31', 3408920.90),
			('Khushi Singh', 'software enginner', 'c++', '2022-12-14', 34007380.90),
			('Anamika Gupta', 'CEO', 'company', '2022-04-22', 8000.90);

TRUNCATE TABLE employee;
TRUNCATE TABLE employee RESTART IDENTITY;







