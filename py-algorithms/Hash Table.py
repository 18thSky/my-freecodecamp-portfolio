class HashTable():
    def __init__(self):
        self.collection = {}
        
    def hash(self,key):
        total = 0
        for keys in key:
            total += ord(keys)
        return total
        
    def add(self,key,value):
       hashed = self.hash(key)
       if hashed in self.collection:
        self.collection[hashed] = {}
        self.collection[hashed] [key] = value

    
        


    # def hash():
    #     input(string)

    # def add():

    # def remove():

    # def lookup():

table = HashTable()
print(table.collection)

table = HashTable()
print(table.hash("golf"))

