import csv

class Solution:

    def readCsv(self,fileName):
        with open('people.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            lineCount = 0
            header = []
            result = []
            for person in reader:
                if lineCount == 0:
                    header.append([person])
                    lineCount +=1
                result.append({'name':person["name"],'address':person["address"],'age':person["age"]})

            return result
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.readCsv("people.csv"))