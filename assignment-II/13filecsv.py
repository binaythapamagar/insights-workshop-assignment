import csv

class Solution:

    def writeCsv(self,fileName,tuples):
        with open('people.csv', 'w', newline='') as file:
            fieldnames = ['name', 'address','age']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for person in tuples:
                writer.writerow({'name': person[0], 'address': person[1],'age':person[2]})
        
if __name__ == "__main__":
    tuples = [('Binay','Kathmandu',23),('Bikal','Pokhara',24),('Bijay','Chitwan',22)]
    solution = Solution()
    solution.writeCsv("peoplecsv",tuples)