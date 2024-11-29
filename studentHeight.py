userInput = 2  
while True:  
    print("1. Add Student")
    print("0. Exit")
    userInput = int(input("Please Select Option:"))  
    if userInput == 0:
        break  
    class CalUtils:
        name = []
        height = []
        totalStudentHeight = 0
        totalStudentCount = 0

        def setList(self):
            f = open("listOfStudentHeight.txt", "r")
            for line in f:
                x = line.split("\t")
                self.name.append(x[0])
                self.height.append(float(x[1]))
                self.totalStudentCount += 1
                self.totalStudentHeight += float(x[1])
            f.close()
            self.printNames()

        def printNames(self):
            for x in range(len(self.name)):  
                print(self.name[x] + " Height: " + str(self.height[x]))

        def reset(self):
            self.name = []
            self.height = []
            self.totalStudentHeight = 0
            self.totalStudentCount = 0

        def calAvgHeight(self):
            self.reset()
            self.setList()
            avg = self.totalStudentHeight / self.totalStudentCount
            print("Student average height is ", str(round(avg, 2)) + " m for", str(self.totalStudentCount) + " students.")

        def addStudent(self):
            g = open("listOfStudentHeight.txt", "a")
            name = input("Please Enter Full Name:")
            while True:
                try:
                    height = float(input("Please Enter Height(in meter):"))
                    break
                except ValueError:
                    print("Please Enter Numeric Only")
            g.write(name + "\t" + str(height) + "\n")
            g.close()
            self.calAvgHeight()

    temp = CalUtils()
    temp.calAvgHeight()
    temp.addStudent()

print("Thank you!")
