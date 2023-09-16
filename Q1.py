# -- 1. Create a table (student) with 3 columns (rollno, name, course).
# CREATE TABLE student (
#     rollno INT PRIMARY KEY,
#     name VARCHAR(255),
#     course VARCHAR(255)
# );

# -- 2. Insert records for 4 students.
# INSERT INTO student (rollno, name, course)
# VALUES
#     (1, 'Alice', 'Math'),
#     (2, 'Bob', 'History'),
#     (3, 'Charlie', 'Physics'),
#     (4, 'David', 'Chemistry');

# -- 3. Write a Select query to fetch all the students.
# SELECT * FROM student;

# -- 4. Update the student name of rollno 3 with ‘Mohan’.
# UPDATE student
# SET name = 'Mohan'
# WHERE rollno = 3;

# -- 5. Delete any student from table with their rollno.
# DELETE FROM student
# WHERE rollno = 2;

# -- 6. Delete all the data from student table.
# DELETE FROM student;

# -- 7. Drop the student table.
# DROP TABLE student;

# -- 8. Create Courses table (cid, cname) where cid is a primary key and Student table (rollno, name, cid) where rollno is a primary key and cid is a foreign key.
# CREATE TABLE courses (
#     cid INT PRIMARY KEY,
#     cname VARCHAR(255)
# );

# CREATE TABLE student (
#     rollno INT PRIMARY KEY,
#     name VARCHAR(255),
#     cid INT,
#     FOREIGN KEY (cid) REFERENCES courses (cid)
# );

# -- 9. Insert data in both the tables.
# INSERT INTO courses (cid, cname)
# VALUES
#     (1, 'Math'),
#     (2, 'History'),
#     (3, 'Physics'),
#     (4, 'Chemistry');

# INSERT INTO student (rollno, name, cid)
# VALUES
#     (1, 'Alice', 1),
#     (2, 'Bob', 2),
#     (3, 'Charlie', 3),
#     (4, 'David', 4);

# -- 10. Select all the students who are doing a specific course, eg. Python.
# SELECT student.name, courses.cname
# FROM student
# JOIN courses ON student.cid = courses.cid
# WHERE courses.cname = 'Physics';
