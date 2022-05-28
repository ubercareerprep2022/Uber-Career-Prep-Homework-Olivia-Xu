from collections import deque

class OrganizationStructure:
    def __init__(self, ceo=None):
        self.ceo = ceo

    def printLevelByLevel(self):
        q = deque()
        if self.ceo: q.append(self.ceo)
        qSize = len(q)
        while qSize > 0:
            for i in range(qSize):
                currentEmp = q.popleft()
                print('Name: ', currentEmp.name, ', Tittle: ', currentEmp.title)
                q.extend(currentEmp.directReports)
            print()
            qSize = len(q)
    
    def printNumLevels(self):
        
        def findLevelBelow(currentEmp):
            level = 0
            if currentEmp:
                level += 1
                if len(currentEmp.directReports) > 0:
                    subLevels = [findLevelBelow(dr) for dr in currentEmp.directReports]
                    level += max(subLevels)
            return level

        print("Number of levels: ", findLevelBelow(self.ceo))

    
class Employee:
    def __init__(self, name='', title='', directReports=[]):
        self.name = name
        self.title = title
        self.directReports = directReports

# example case
salesIntern = Employee('K', 'Sales Intern')
salesRep = Employee('J', 'Sales Representative', [salesIntern])
director = Employee('I', 'Director', [salesRep])
cfo = Employee('B', 'CFO', [director])
engineerF = Employee('F', 'Engineer')
engineerG = Employee('G', 'Engineer')
engineerH = Employee('H', 'Engineer')
managerD = Employee('D', 'Manager', [engineerF, engineerG, engineerH])
managerE = Employee('E', 'Manager')
cto = Employee('C', 'CTO', [managerD, managerE])
ceo = Employee('A', 'CEO', [cfo, cto])
org = OrganizationStructure(ceo)

print('Example case: ')
org.printLevelByLevel()
org.printNumLevels()
print()

# null case
org = OrganizationStructure()
print('Null case: ')
org.printLevelByLevel()
org.printNumLevels()
print()

# single-value case
ceo = Employee('A', 'CEO')
org = OrganizationStructure(ceo)

print('Single-value case: ')
org.printLevelByLevel()
org.printNumLevels()
print()

# second example case
director = Employee('I', 'Director')
cfo = Employee('B', 'CFO', [director])
engineerF = Employee('F', 'Engineer')
engineerG = Employee('G', 'Engineer')
engineerH = Employee('H', 'Engineer')
managerD = Employee('D', 'Manager', [engineerF, engineerG, engineerH])
managerE = Employee('E', 'Manager')
cto = Employee('C', 'CTO', [managerD, managerE])
ceo = Employee('A', 'CEO', [cfo, cto])
org = OrganizationStructure(ceo)

print('Second example case: ')
org.printLevelByLevel()
org.printNumLevels()
print()