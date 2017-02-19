#Arnav Gupta
#Ruhi Sharfuddin

import csv
import psycopg2
import os
import glob 

#connecting to postgres
try:
    conn = psycopg2.connect(database="postgres", user=os.environ['USER'], port="5432")
    cur = conn.cursor()
except:
    print "I am unable to connect to the database"
    print os.environ['USER']

#creating the tables

cur.execute("CREATE TABLE Student(CID INT, SID INT, Surname CHAR(30), Prefname CHAR(30), Level CHAR(10), Email CHAR(50), Status CHAR(10), Major VARCHAR(10), Class CHAR(4), TotalUnits DECIMAL(10,5), Term INT, PRIMARY KEY (CID, SID, TERM))")

cur.execute("CREATE TABLE Course(CID INT, Term INT, Subject CHAR(7), CRSE INT,Section INT, CourseUnits CHAR(20), PRIMARY KEY(CID,Term))")

cur.execute("CREATE TABLE Meeting(CID INT, Term INT, Instructor CHAR(40), Type CHAR(40), Days CHAR(6), TIME_ CHAR(40), Building CHAR(10), Room INT, PRIMARY KEY (CID, Term, Days, TIME_, Instructor, Type, Room))")

cur.execute("CREATE TABLE CourseStudents(CID INT, SID INT, Term INT, GPA DECIMAL(2,1), Grade CHAR(5), StudentUnits DECIMAL(10,5), Seat INT, Subject CHAR(7) , PRIMARY KEY(CID, SID, Term))")
conn.commit() 

################# Function to convert GRade to GPA and return GPA ##############################

def convertGPA(G):
	if G == 'A+':
		return 4.0
	elif G == 'A':
		return 4.0
	elif G == 'A-':
		return 3.7
	elif G == 'B+':
		return 3.3
	elif G == 'B':
		return 3.0
	elif G == 'B-':
		return 2.7
	elif G == 'C+':
		return 2.3
	elif G == 'C': 
		return 2.0
	elif G == 'C-':
		return 1.7
	elif G == 'D+':
		return 1.3
	elif G == 'D':
		return 1.0
	elif G == 'D-':
		return 0.7
	elif G == 'F':
		return 0 

###################################### Function to insert the data into the database #############################################

def Execfunction(course1, Meeting1, Student1, CourseStudent1): 
	random = ''
	if not course1 and not Meeting1 and not Student1:
		return  
	if not Student1: 
		return
	cur.execute("INSERT INTO Course(CID, Term, Subject, CRSE, Section, CourseUnits) VALUES (%s, %s, %s, %s, %s, %s)", (course[0], course[1], course[2], course[3], course[4], course[5]))
	for x in Meeting1:
		rm = x[7] 
		if rm == None: 
			rm = -1 
		if random != x: 
			cur.execute("INSERT INTO Meeting(CID, Term, Instructor, Type, Days, TIME_, Building, Room) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(x[0], x[1], x[2], x[3], x[4], x[5], x[6], rm))
		random = x
	for y in Student1:
		unitvalue = y[9]
		if unitvalue == '':
		 	unitvalue = None  
		cur.execute("INSERT INTO Student(CID, SID, Surname, Prefname, Level, Email, Status, Major, Class, TotalUnits, Term) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], unitvalue, y[10]))
	for z in CourseStudent1:
		unitvalue1 = z[3]
		if  unitvalue1 == '':
		 	unitvalue1 = None
		unitvalue2 = z[5]  
		if unitvalue2 == '':
		 	unitvalue2 = None  
		unitvalue3 = z[6]
		if unitvalue3 == '':
		 	unitvalue3 = None  
		cur.execute("INSERT INTO CourseStudents(CID, SID, Term, GPA, Grade, StudentUnits, Seat, Subject) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (z[0], z[1], z[2], unitvalue1, z[4], unitvalue2, unitvalue3, z[7]))

############# VARIABLE DECLARATION ####################

Meetinglist=[]
Studentlist=[]
CSList=[]
carryvalue = '' 
a = '' 
selection = 0
marker = False
course = None 

#######################################################

#Generating the file names

names = glob.glob('*.csv')
for x in names:
		print x 
		with open(x) as myfile:
			reader = csv.reader(myfile)
			for rowlist in reader:
				if len(rowlist)!=1:					# if not an empty line
					# if the section to be read in is course
					if selection == 1:
						course = rowlist
						selection = 0
					
					# if the section to be read in is Instructor
					elif selection == 2:
						#if Internship
						if rowlist[1] == 'Internship':
							instructor = rowlist
							#checkc for the value of room not being present
							if instructor[5] == '':
								instructor[5] = None
							b = (course[0], course[1], instructor[0], instructor[1], a, a, a, None)
							Meetinglist.append(b)			#putting it into one list
						
						#Regular Instructor entry with name given
						elif len(rowlist[0])!=0:
							instructor = rowlist
							if instructor[5] == '':
								instructor[5] = None
							c = (course[0], course[1], instructor[0], instructor[1], instructor[2], instructor[3], instructor[4], instructor[5])
							Meetinglist.append(c)
							marker = True
						
						# instructor entry without name but name given in previous line
						elif marker == True:
							if instructor[0] != '':
								carryvalue = instructor[0] 
							instructor = rowlist
							if instructor[5] == '':
								instructor[5] = None
							d = (course[0],course[1],carryvalue,instructor[1], instructor[2], instructor[3], instructor[4], instructor[5])
							Meetinglist.append(d)
						
						#instructor entry without instructor name
						elif marker == False:
							instructor = rowlist
							if instructor[5] == '':
								instructor[5] = None
							e = (a ,course[1],instructor[1], instructor[2], instructor[3], instructor[4], instructor[5],course[0])
							Meetinglist.append(e)
					
					# if the line to be read is a student
					elif selection == 3:
						student = rowlist
						#create a list variable for Student table
						f = (course[0], student[1], student[2], student[3], student[4], student[10], student[9], student[7], student[6], student[5], course[1])
						Studentlist.append(f)

						GP = convertGPA(student[8])			# conver the grade into GPA
	
						#create a list variable for CourseStudents
						g = (course[0], student[1], course[1], GP, student[8], student[5], student[0], course[2])
						CSList.append(g) 


				####################### Setting the variable for slection ########################
				
				#If the first word of the line is CID (if the line after is the CID data)
				if rowlist[0] == 'CID':
					Execfunction(course,Meetinglist, Studentlist,CSList)
					course = []
					Meetinglist = []
					Studentlist = []
					CSList = []
					selection = 1
				#if the line to read after is Instructor data
				elif rowlist[0] == 'INSTRUCTOR(S)':
					selection  = 2
					carryvalue = ''
				#if the line to read after is Student data
				elif rowlist[0] == 'SEAT':
					selection = 3
				#Reset the value
				elif len(rowlist) == 1: 
					selection = 0



conn.commit()