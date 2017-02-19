import csv
import psycopg2
import os

#connecting to postgres
try:
    conn = psycopg2.connect(database="postgres", user=os.environ['USER'], port="5432")
    print "Ruhi is cool"
    cur = conn.cursor()
except:
    print "I am unable to connect to the database"
    print os.environ['USER']




cur.execute("SELECT Sum(StudentUnits) FROM CourseStudents GROUP BY Term, SID HAVING SUM(StudentUnits) = 1 or SUM(StudentUnits) = 2 or SUM(StudentUnits) = 3 or SUM(StudentUnits) = 4 or SUM(StudentUnits) = 5 or SUM(StudentUnits) = 6 or SUM(StudentUnits) = 7 or SUM(StudentUnits) = 8 or SUM(StudentUnits) = 9 or SUM(StudentUnits) = 10 or SUM(StudentUnits) = 11 or SUM(StudentUnits) = 12 or SUM(StudentUnits) = 13 or SUM(StudentUnits) = 14 or SUM(StudentUnits) = 15 or SUM(StudentUnits) = 16 or SUM(StudentUnits) = 17 or SUM(StudentUnits) = 18 or SUM(StudentUnits) = 19 or SUM(StudentUnits) = 20;")  
x=cur.fetchall()

denom = len(x)
print 'THIS IS 3A'
cur.execute("SELECT DISTINCT S AS CS, COUNT(S) FROM (SELECT Sum(StudentUnits) AS S FROM CourseStudents GROUP BY Term, SID HAVING SUM(StudentUnits) = 1 or SUM(StudentUnits) = 2 or SUM(StudentUnits) = 3 or SUM(StudentUnits) = 4 or SUM(StudentUnits) = 5 or SUM(StudentUnits) = 6 or SUM(StudentUnits) = 7 or SUM(StudentUnits) = 8 or SUM(StudentUnits) = 9 or SUM(StudentUnits) = 10 or SUM(StudentUnits) = 11 or SUM(StudentUnits) = 12 or SUM(StudentUnits) = 13 or SUM(StudentUnits) = 14 or SUM(StudentUnits) = 15 or SUM(StudentUnits) = 16 or SUM(StudentUnits) = 17 or SUM(StudentUnits) = 18 or SUM(StudentUnits) = 19 or SUM(StudentUnits) = 20) AS Z GROUP BY CS ORDER BY CS;") 
y=cur.fetchall() 

unit1 = (y[0][1]/(denom * 1.0)) * 100 
print 'Percent for 1 unit: %s' %unit1 
unit2 = (y[1][1]/(denom * 1.0)) * 100 
print 'Percent for 2 units: %s' %unit2 
unit3 = (y[2][1]/(denom * 1.0)) * 100 
print 'Percent for 3 units: %s' %unit3
unit4 = (y[3][1]/(denom * 1.0)) * 100 
print 'Percent for 4 units: %s' %unit4
unit5 = (y[4][1]/(denom * 1.0)) * 100 
print 'Percent for 5 units: %s' %unit5
unit6 = (y[5][1]/(denom * 1.0)) * 100 
print 'Percent for 6 units: %s' %unit6
unit7 = (y[6][1]/(denom * 1.0)) * 100 
print 'Percent for 7 units: %s' %unit7
unit8 = (y[7][1]/(denom * 1.0)) * 100 
print 'Percent for 8 units: %s' %unit8
unit9 = (y[8][1]/(denom * 1.0)) * 100 
print 'Percent for 9 units: %s' %unit9
unit10 = (y[9][1]/(denom * 1.0)) * 100 
print 'Percent for 10 units: %s' %unit10
unit11 = (y[10][1]/(denom * 1.0)) * 100 
print 'Percent for 11 units: %s' %unit11
unit12 = (y[11][1]/(denom * 1.0)) * 100 
print 'Percent for 12 units: %s' %unit12
unit13 = (y[12][1]/(denom * 1.0)) * 100 
print 'Percent for 13 units: %s' %unit13
unit14 = (y[13][1]/(denom * 1.0)) * 100 
print 'Percent for 14 units: %s' %unit14
unit15 = (y[14][1]/(denom * 1.0)) * 100 
print 'Percent for 15 units: %s' %unit15
unit16 = (y[15][1]/(denom * 1.0)) * 100 
print 'Percent for 16 units: %s' %unit16
unit17 = (y[16][1]/(denom * 1.0)) * 100 
print 'Percent for 17 units: %s' %unit17
unit18 = (y[17][1]/(denom * 1.0)) * 100 
print 'Percent for 18 units: %s' %unit18
unit19 = (y[18][1]/(denom * 1.0)) * 100 
print 'Percent for 19 units: %s' %unit19
unit20 = (y[19][1]/(denom * 1.0)) * 100 
print 'Percent for 20 units: %s' %unit20

print ''
print 'THIS IS THE ANSWER FOR 3B'
print ''

cur.execute("SELECT DISTINCT S AS CS, AVG(AG) FROM (SELECT Sum(StudentUnits) AS S, AVG(GPA) AS AG FROM CourseStudents GROUP BY Term, SID HAVING SUM(StudentUnits) = 1 or SUM(StudentUnits) = 2 or SUM(StudentUnits) = 3 or SUM(StudentUnits) = 4 or SUM(StudentUnits) = 5 or SUM(StudentUnits) = 6 or SUM(StudentUnits) = 7or SUM(StudentUnits) = 8 or SUM(StudentUnits) = 9 or SUM(StudentUnits) = 10 or SUM(StudentUnits) = 11 or SUM(StudentUnits) = 12 or SUM(StudentUnits) = 13 or SUM(StudentUnits) = 14 or SUM(StudentUnits) = 15 or SUM(StudentUnits) = 16 or SUM(StudentUnits) = 17 or SUM(StudentUnits) = 18 or SUM(StudentUnits) = 19 or SUM(StudentUnits) = 20) AS Z GROUP BY CS ORDER BY CS;") 
z=cur.fetchall() 
gpa1 = z[0][1] 
print 'Average GPA for 1 unit: %s' %gpa1 
gpa2 = z[1][1]
print 'Average GPA for 2 units: %s' %gpa2 
gpa3 = z[2][1] 
print 'Average GPA for 3 units: %s' %gpa3 
gpa4 = z[3][1] 
print 'Average GPA for 4 units: %s' %gpa4 
gpa5 = z[4][1]
print 'Average GPA for 5 units: %s' %gpa5 
gpa6 = z[5][1]
print 'Average GPA for 6 units: %s' %gpa6 
gpa7 = z[6][1]
print 'Average GPA for 7 units: %s' %gpa7 
gpa8 = z[7][1]
print 'Average GPA for 8 units: %s' %gpa8 
gpa9 = z[8][1]
print 'Average GPA for 9 units: %s' %gpa9 
gpa10 = z[9][1]
print 'Average GPA for 10 units: %s' %gpa10 
gpa11 = z[10][1]
print 'Average GPA for 11 units: %s' %gpa11 
gpa12 = z[11][1]
print 'Average GPA for 12 units: %s' %gpa12 
gpa13 = z[12][1]
print 'Average GPA for 13 units: %s' %gpa13 
gpa14 = z[13][1]
print 'Average GPA for 14 units: %s' %gpa14 
gpa15 = z[14][1]
print 'Average GPA for 15 units: %s' %gpa15 
gpa16 = z[15][1]
print 'Average GPA for 16 units: %s' %gpa16 
gpa17 = z[16][1]
print 'Average GPA for 17 units: %s' %gpa17 
gpa18 = z[17][1]
print 'Average GPA for 18 units: %s' %gpa18 
gpa19 = z[18][1]
print 'Average GPA for 19 units: %s' %gpa19 
gpa20 = z[19][1]
print 'Average GPA for 20 units: %s' %gpa20 

print ''
######################## answer to part 3c ######################## - have to make it distinct i think - maybe not
# Select AVG(CourseStudents.GPA), Instructor FROM Meeting NATURAL JOIN CourseStudents GROUP BY Meeting.Instructor;
###############

print 'THIS IS 3C'

def convertGPA(G):
	if G >= 3.83 and G <= 4.0: 
		return 'A'
	elif G < 3.83 and G >= 3.67:
		return 'A-'
	elif G >= 3.33 and G < 3.67: 
		return 'B+'
	elif G < 3.32 and G >= 3.00:
		return 'B'
	elif G >= 2.67 and G < 3.00:
		return 'B-'
	elif G >= 2.33 and G < 2.67:
		return 'C+'
	elif G >= 2.00 and G < 2.33:
		return 'C'
	elif G >= 1.67 and G < 2.00: 
		return 'C-'
	elif G >= 1.33 and G < 1.67:
		return 'D+'
	elif G >= 1.00 and G < 1.33:
		return 'D'
	elif G >= 0.67 and G < 1.00: 
		return 'D-'
	elif G >= 0 and G < 0.67:
		return 'F'


cur.execute("SELECT MIN(A) FROM (SELECT AVG(CourseStudents.GPA) AS A, Instructor FROM Meeting NATURAL JOIN CourseStudents GROUP BY Meeting.Instructor) AS C;") 
mingrade=cur.fetchall()
print 'The lowest average grade is:'
for row in mingrade:
	m1=row[0]
mx = convertGPA(m1)
print mx 

print ''

cur.execute("SELECT Instructor FROM (SELECT AVG(CourseStudents.GPA) AS A, Instructor FROM Meeting NATURAL JOIN CourseStudents GROUP BY Meeting.Instructor) AS ZX WHERE A = (SELECT MIN(ASD) FROM (SELECT AVG(CourseStudents.GPA) AS ASD, Instructor FROM Meeting NATURAL JOIN CourseStudents GROUP BY Meeting.Instructor) AS ER);")
minprof=cur.fetchall()
print 'The hardest professor according the lowest average grade is:'
for row in minprof:
	m2=row[0]
print m2

print ''

cur.execute("SELECT MAX(A) FROM (SELECT AVG(CourseStudents.GPA) AS A, Instructor FROM Meeting NATURAL JOIN CourseStudents GROUP BY Meeting.Instructor) AS C;") 
maxgrade=cur.fetchall() 
print 'The highest average grade is:'
for row in maxgrade:
	m3=row[0]
my=convertGPA(m3)
print my 

print'' 
cur.execute("SELECT Instructor FROM (SELECT AVG(CourseStudents.GPA) AS A, Instructor FROM Meeting NATURAL JOIN CourseStudents GROUP BY Meeting.Instructor) AS ZX WHERE A = (SELECT MAX(ASD) FROM (SELECT AVG(CourseStudents.GPA) AS ASD, Instructor FROM Meeting NATURAL JOIN CourseStudents GROUP BY Meeting.Instructor) AS ER);")
maxprof = cur.fetchall()
print 'The easiest professor according to the highest average grade is:'
# for row in maxprof:
# 	m4=row[0] 
print maxprof 

print ''
print 'THIS IS 3D'
print ''


cur.execute("SELECT DISTINCT CRSE FROM COURSE WHERE CRSE > 100 AND CRSE <200;")
CRSEList = cur.fetchall()
# print CRSEList

for xg in CRSEList:
	print 'The CRSE is %s' %xg
	cur.execute("SELECT MIN(A) FROM (SELECT AVG(BIG.GPA) AS A, Instructor FROM (SELECT CID,CRSE,GPA,INSTRUCTOR,SUBJECT FROM ((SELECT CID, CRSE FROM Course) AS A NATURAL JOIN CourseStudents NATURAL JOIN(SELECT CID, INSTRUCTOR FROM Meeting) AS B)WHERE SUBJECT = 'ABC' AND CRSE = %s) AS BIG GROUP BY BIG.Instructor) as HH;",(xg))
	XMINGPA = cur.fetchall()
	for row in XMINGPA:
		min1=row[0]
	print 'The lowest average grade for this CRSE is', min1 

	cur.execute("SELECT INSTRUCTOR FROM (SELECT AVG(BIG.GPA) as AVGPA, INSTRUCTOR FROM (SELECT CID,CRSE,GPA,INSTRUCTOR,SUBJECT FROM (SELECT CID, CRSE FROM Course) AS A NATURAL JOIN CourseStudents	NATURAL JOIN(SELECT CID, INSTRUCTOR FROM Meeting) AS B WHERE SUBJECT = 'ABC' AND CRSE = %s) AS BIG GROUP BY BIG.Instructor) as HH where AVGPA = (SELECT MIN(A) FROM (SELECT AVG(BIG.GPA) AS A, Instructor FROM (SELECT CID,CRSE,GPA,INSTRUCTOR,SUBJECT FROM ((SELECT CID, CRSE FROM Course) AS A NATURAL JOIN CourseStudents NATURAL JOIN(SELECT CID, INSTRUCTOR FROM Meeting) AS B)WHERE SUBJECT = 'ABC' AND CRSE = %s) AS BIG GROUP BY BIG.Instructor) as HH);",(xg, xg))
	k= cur.fetchall()
	for row in k:
		k1=row[0]
	print 'The hardest professor for this CRSE is', k1

	cur.execute("SELECT MAX(A) FROM (SELECT AVG(BIG.GPA) AS A, Instructor FROM (SELECT CID,CRSE,GPA,INSTRUCTOR,SUBJECT FROM ((SELECT CID, CRSE FROM Course) AS A NATURAL JOIN CourseStudents NATURAL JOIN(SELECT CID, INSTRUCTOR FROM Meeting) AS B)WHERE SUBJECT = 'ABC' AND CRSE = %s) AS BIG GROUP BY BIG.Instructor) as HH;",(xg))
	XMAXGPA = cur.fetchall()
	for row in XMAXGPA:
		max1=row[0]
	print 'The highest average grade for this CRSE is', max1

	cur.execute("SELECT INSTRUCTOR FROM (SELECT AVG(BIG.GPA) as AVGPA, INSTRUCTOR FROM (SELECT CID,CRSE,GPA,INSTRUCTOR,SUBJECT FROM (SELECT CID, CRSE FROM Course) AS A NATURAL JOIN CourseStudents	NATURAL JOIN(SELECT CID, INSTRUCTOR FROM Meeting) AS B WHERE SUBJECT = 'ABC' AND CRSE = %s) AS BIG GROUP BY BIG.Instructor) as HH where AVGPA = (SELECT MAX(A) FROM (SELECT AVG(BIG.GPA) AS A, Instructor FROM (SELECT CID,CRSE,GPA,INSTRUCTOR,SUBJECT FROM ((SELECT CID, CRSE FROM Course) AS A NATURAL JOIN CourseStudents NATURAL JOIN(SELECT CID, INSTRUCTOR FROM Meeting) AS B)WHERE SUBJECT = 'ABC' AND CRSE = %s) AS BIG GROUP BY BIG.Instructor) as HH);",(xg, xg))
	j= cur.fetchall()
	for row in j:
		j2=row[0]
	print 'The easiest professor for this CRSE is', j2

print ''

print 'THIS IS FOR THE PASS RATE '
cur.execute("SELECT COUNT(case GRADE WHEN 'P' then 1 else null end)*100/(COUNT(case GRADE WHEN 'P' then 1 else null end)+COUNT(case GRADE WHEN 'NP' then 1 else null end)) AS A, Instructor AS inst, CRSE AS cr FROM (SELECT CRSE,Grade,INSTRUCTOR,SUBJECT FROM ((SELECT CID, CRSE FROM Course) AS A NATURAL JOIN CourseStudents NATURAL JOIN(SELECT CID, INSTRUCTOR FROM Meeting) AS B) AS BIG WHERE SUBJECT = 'ABC' AND (GRADE = 'P' OR GRADE = 'NP') AND INSTRUCTOR != '' AND (CRSE= 112 OR CRSE = 114 or CRSE = 113)) as ss GROUP BY cr, inst order by cr;")
totalstudent=cur.fetchall()
for row in totalstudent:
    print row[0], row[1], row[2]

print''
print'THIS IS 3E'

cur.execute("Select * from Course group by Term, CID having Count(*) >1;")
xy=cur.fetchall()
print xy
print 'There are no tuples printed here because we already took care of this case during the parsing, where we did not insert any CID information where the number of students is zero'
print ''

cur.execute("select SID, TERM, MAX(CID) AS CID1, MIN(CID) AS CID2 from Course NAtural join Student group by SID, TERM having Count(Distinct major)>1 OR count(Distinct class)>1 OR count (Distinct level)>1 OR count(distinct status) > 1;")
studentconflict=cur.fetchall()
print'These are all the summer session conflicts where the student changed major or level or status or class:'
print ''
print 'SID       TERM   CID1   CID2'
for row in studentconflict:
    print row[0], row[1], row[2], row[3]

print ''

cur.execute("Select room, building, term, MIN(CID) AS CID, min(j.subject) as subject1, min(j.crse) as crse1, max(j.subject) as subject2, max(j.CRSE) as crse2, time_ from Meeting NAtural Join Course as J where room != '-1' AND (building != '' AND building is not NULL) AND (time_ != '' AND time_ is not null) AND (days != '' AND days is not null) group by term,Building, room, meeting.time_ ,days having count(distinct concat(j.Subject,j.CRSE))>1;")
meetingconflict=cur.fetchall()
print'These are all the summer session conflicts that arise from a conflict with meeting time, day, building, room, etc:'
print ''
print 'ROOM BUILDING   TERM  CID   SUBJECT1   COURSE1      SUBJECT2       COURSE2    TIME' 
for row in meetingconflict:
    print row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]


print ''
print 'THIS IS 3F'

cur.execute("Select major from (SELECT major, (SUM(NEWGPA)/count(NEWGPA)) AS CGPA FROM (select (TotalUnits*GPA) as NEWGPA, major from Student NATURAL JOIN CourseStudents where SUBJECT = 'ABC') as Tab GROUP BY major) as newtable where CGPA = (Select min(CGPA) from (SELECT major, (SUM(NEWGPA)/count(NEWGPA)) AS CGPA FROM (select (TotalUnits*GPA) as NEWGPA, major from Student NATURAL JOIN CourseStudents where SUBJECT = 'ABC') as Tab GROUP BY major) as newtable);")
minmajor = cur.fetchall()
print "The major that performs the worst on average is" , minmajor
print ''
cur.execute("Select major from (SELECT major, (SUM(NEWGPA)/count(NEWGPA)) AS CGPA FROM (select (TotalUnits*GPA) as NEWGPA, major from Student NATURAL JOIN CourseStudents where SUBJECT = 'ABC') as Tab GROUP BY major) as newtable where CGPA = (Select max(CGPA) from (SELECT major, (SUM(NEWGPA)/count(NEWGPA)) AS CGPA FROM (select (TotalUnits*GPA) as NEWGPA, major from Student NATURAL JOIN CourseStudents where SUBJECT = 'ABC') as Tab GROUP BY major) as newtable);")
maxmajor = cur.fetchall()
print "The major that performs the best is on average is" , maxmajor

print''
print 'THIS IS 3G'
cur.execute("select count(DISTINCT A.SID) from (select DISTINCT SID, term from student where major like 'ABC%') AS A, (select DISTINCT SID, term from student where major not like '%ABC%') AS B where A.term > B.term and A.SID = B.SID;")
percentstudent=cur.fetchall()
for row in percentstudent:
	xy=row[0]
print 'The number of students that transferred to ABC major:', xy
print''

cur.execute("SELECT COUNT (DISTINCT SID) FROM STUDENT WHERE MAJOR NOT LIKE '%ABC%';")
totalstudent=cur.fetchall()
for row in totalstudent:
	x1=row[0]

cur.execute("SELECT COUNT (DISTINCT SID) FROM STUDENT WHERE MAJOR LIKE '%ABC%';")
totalstudent1=cur.fetchall()
for row in totalstudent1:
	x_1=row[0]

cur.execute("SELECT COUNT (DISTINCT SID) FROM STUDENT;")
totalstudent2=cur.fetchall()
for row in totalstudent2:
	x2=row[0]

g1  = (xy*1.0/x1*1.0) * 100
print 'The percent out of all non ABC majors that switch into ABC is:', g1

g2= (xy*1.0/x2*1.0) * 100
print 'The percent of all majors that swtiched into ABC is:', g2

g3= (xy*1.0/x_1*1.0) * 100
print 'The percent of all the students who switch into an ABC major out of all the ABC majors:', g3 
print''

print 'The top 5 majors of the students that tranfer into ABC and their percentages:'

xy1= xy*1.0 
cur.execute("select count(DISTINCT a.SID), b.major, (count(distinct a.sid*1.0)/1397.0)*100 as Percentage from (select DISTINCT SID, term from student where major like 'ABC%') AS A, (select DISTINCT SID, major, term from student where major not like '%ABC%') AS B where A.term > B.term and A.SID = B.SID group by b.major order by count(distinct a.SID) desc limit 5;")
top5=cur.fetchall()
for row in top5:
	print row[0], row[1],row[2]  	

