1. Student Table
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    Email VARCHAR(100)
);

CREATE TABLE Club (
    ClubName VARCHAR(50) PRIMARY KEY,
    ClubRoom VARCHAR(10),
    ClubMentor VARCHAR(50)
);


CREATE TABLE Membership (
    StudentID INT,
    ClubName VARCHAR(50),
    JoinDate DATE,
    PRIMARY KEY (StudentID, ClubName),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClubName) REFERENCES Club(ClubName)
);


INSERT INTO Student (StudentID, StudentName, Email) VALUES 
(1, 'Asha', 'asha@email.com'),
(2, 'Bikash', 'bikash@email.com'),
(3, 'Nisha', 'nisha@email.com'),
(4, 'Rohan', 'rohan@email.com'),
(5, 'Suman', 'suman@email.com'),
(6, 'Pooja', 'pooja@email.com'),
(7, 'Aman', 'aman@email.com');


INSERT I