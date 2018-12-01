import csv
import sys
import pandas as pd
import numpy as np
import operator
import os.path
def managestudent():
	print("\n *** WELCOME TO STUDENT's PLACEMENT ELIGIBILITY MANAGEMENT SYSTEM *** ")
	print("Select an option from below mentioned functions:-")
	print("""
1. Insert Student's data
2. Get list of students eligible for any company
3. Exit
		""")

array=[]
a=[]

def insertdata():
	my_file = sys.argv[1]
	if os.path.isfile(my_file):
		with open(sys.argv[1], 'r') as f:
			reader = csv.reader(f)
			next(reader)
			for line in reader:
				array.append(tuple(line))
		print("File uploaded")
		a.append(1)
		print('Student with highest GPA')
		print(max(array, key=operator.itemgetter(1)))
		print('Student with lowest GPA')
		print(min(array, key=operator.itemgetter(1)))
		aggregate()
	else:
		print("File not found")

def company():
	if 1 in a:
		print("Enter company's name")
		co=str(input())
		print("Enter the minimum required CGPA for " + co)
		mg=float(input())

		array.sort(key=operator.itemgetter(1), reverse=True)

		print("Students eligible for " + co)
		for x in array:
			if float(x[1])<=mg:
				break
			print(x[0], x[1])

		with open( co+'.csv' ,'w') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow(["Name" , "CGPA"])
			for x in array:
				if float(x[1])<mg:
					break
				filewriter.writerow([x[0], x[1]])

	else:
		print("Please upload a valid file first")

def aggregate():
	data = pd.read_csv('persons.csv')
	cgpa = np.array(data['CGPA'])
	#print(cgpa)
	print("Mean CGPA:       " + str(round(cgpa.mean())))
	print("Standard deviation:" + str(round(cgpa.std())))


while 1:
	managestudent()
	n=input()
	if int(n)==1:
		insertdata()
	elif int(n)==2:
		company()
	elif int(n)==3:
		print("Thank You!!  >>> application terminating....")
		exit()
	else:
		print("\n Oops!! Invalid entry try again!!\n")

