from tempfile import NamedTemporaryFile
import shutil
import csv
import random
import os

class Solution:
    def writeCsv(self,tuples):
        with open('student.csv', 'a', newline='') as file:
            fieldnames = ['id','name', 'address','balance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for person in tuples:
                writer.writerow({'id':person[0],'name': person[1], 'address': person[2],'balance':person[3]})
    
    def readCsv(self):
        with open('student.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            lineCount = 0
            print('student id \t name \t address \t balance')
            for person in reader:
                if lineCount == 0:
                    lineCount +=1
                print(f'{person["id"]} \t {person["name"]} \t {person["address"]} \t {person["balance"]}')
    
    def updateCsv(self,student):
        
        with open('student.csv', 'r', newline='') as file, open('new.csv', 'w') as output:
            fieldnames = ['id','name', 'address','balance']
            reader = csv.DictReader(file, fieldnames=fieldnames)
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            for person in reader:
                if person['id'] == student[0]:
                    person['name'], person['Course'], person['Year'] = student[1],student[2],student[3]
                person = {'id': person['id'], 'name': person['name'], 'address': person['address'], 'balance': person['balance']}
                writer.writerow(person)
        shutil.move('new.csv','student.csv')
    
    
    def deleteCsv(self,studentId):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open('student.csv', 'r') as file,tempfile:
            fieldnames = ['id','name', 'address','balance']
            reader = csv.DictReader(file, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for person in reader:
                print( person['id'],studentId)
                if person['id'] != studentId:
                    writer.writerow(person)
        shutil.move(tempfile.name, 'student.csv')
                    
           
    def makeEnquiry(self):
        print('SN Course Duration(weeks) \n 1 Software Development 1 \n 2 Html and Css 2 \n 3 Python 3 \n 4 Django 3 \n 5 reeactjs 2')
    
    def register(self):
        name = input('Full Name of Student :')
        address = input('Full Address :')
        payment = int(input('Make payment either 10000 or 20000: '))
        id = random.randrange(0,111111)
        
        self.writeCsv([(id,name,address,payment)])
        
    def showStudent(self):
        self.readCsv()
        
    def updateStudent(self):
        self.showStudent()
        studentId = input('Enter Student id: ')
        name = input('Full Name of Student :')
        address = input('Full Address :')
        payment = int(input('Make payment either 10000 or 20000: '))
        
        self.updateCsv((studentId,name,address,payment))
        
    def deleteStudent(self):
        self.showStudent()
        studentId = input('Enter Student id: ')
        self.deleteCsv(studentId)
        

    def refund(self):
        self.showStudent()
        studentId = input('Enter Student id: ')
        with open('student.csv', 'r', newline='') as file, open('new.csv', 'w') as output:
            fieldnames = ['id','name', 'address','balance']
            reader = csv.DictReader(file, fieldnames=fieldnames)
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            for person in reader:
                if person['id'] == studentId:
                    person['balance'] = 0
                person = {'id': person['id'], 'name': person['name'], 'address': person['address'], 'balance': person['balance']}
                writer.writerow(person)
        shutil.move('new.csv','student.csv')
if __name__ == '__main__':
    solution = Solution()
    print('S.N  Operations \t 1 Make an Enquiry \t 2 Register and Pay \t 3 Display Students \t 4 Update student \t 5 Delete student \t 6 Return Deposit \t 0 Exit')
    operation = int(input('Enter a prefered operation: '))
    while operation != 0:
        
        #perform operation
        if operation == 1:
            solution.makeEnquiry()
        elif operation == 2:
            solution.register()
        elif operation == 3:
            solution.showStudent()
        elif operation == 4:
            solution.updateStudent()
        elif operation == 5:
            solution.deleteStudent()
        elif operation == 6:
            solution.refund()
        else:
            operation == 0
        print('Key  Operations \n 1 Make an Enquiry \n 2 Register and Pay \n 3 Display Students \n 4 Update student \n 5 Delete student \n 6 Return Deposit \n 0 Exit')
        operation = int(input('Enter a prefered operation: '))
        