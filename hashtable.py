# Implement hashtable in python to store student record. Use student roll number to generate hash key.
# Search student in hashtable using roll number and full name

class StudentRecord:
    def __init__(self, roll_number: int = None, full_name: str = None, section: str = None) -> None:
        self.roll_number = roll_number
        self.full_name = full_name
        self.section = section


class HashTable:

    # hash table has default size of 10.
    def __init__(self, size=10) -> None:
        self.container = [None for i in range(size)]
        self.totalEntries = 0

    def generateHash(self, roll_number: int) -> int:
        hash = roll_number % (len(self.container) - 2)
        return hash

    def addRecord(self, roll_number: int = None, full_name: str = None, section: str = None) -> None:
        if self.totalEntries >= len(self.container):
            return print("Hashtable is full")

        newHash = self.generateHash(roll_number)
        i = newHash

        newRecord = StudentRecord(roll_number, full_name, section)

        while True:
            if self.container[i] is None:
                self.container[i] = newRecord
                break
            else:
                i += 1
        self.totalEntries += 1

    def findStudent(self, roll_number: int, full_name: str) -> None:
        print("====== Searching data ======")
        i = self.generateHash(roll_number)
        found = False
        while i < len(self.container) and found == False:
            if self.container[i].full_name == full_name:
                print("Data found at index %d ." % i)
                print(
                    f"Roll number: {self.container[i].roll_number} | Name: {self.container[i].full_name} | Section: {self.container[i].section}")
                found = True
            else:
                i += 1
        if found == False:
            print("Data not found.")

    def printStatus(self) -> None:
        print("====== Printing Status ======")
        i = 0
        while i < len(self.container):
            if self.container[i] is None:
                i += 1
            else:
                print(
                    f"Roll number: {self.container[i].roll_number} | Name: {self.container[i].full_name} | Section: {self.container[i].section}")
                i += 1


#  create new hashtable of size 5
hashtable = HashTable(size=5)

# Add five records in in hashtable
hashtable.addRecord(300, "Yaman Sarabariya", "C")
hashtable.addRecord(301, "Bibek Shah", "A")
hashtable.addRecord(302, "Shivansh Dutta", "A")
hashtable.addRecord(304, "Saugat Gautam", "A")
hashtable.addRecord(304, "Shambhu Yadav", "B")

# find student in hashtable using their roll number and full name
hashtable.findStudent(301, "Bibek Shah")


# display status
hashtable.printStatus()