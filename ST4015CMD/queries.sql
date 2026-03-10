SELECT 
    Student.StudentName, 
    Club.ClubName, 
    Membership.JoinDate
FROM Student
JOIN Membership ON Student.StudentID = Membership.StudentID
JOIN Club ON Membership.ClubName = Club.ClubName;