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
            self.collection[hashed][key] = value
        else:
            self.collection[hashed] = {}
            self.collection[hashed][key] = value

    def remove(self,key):
        hashed = self.hash(key)

        if hashed in self.collection:
            if key in self.collection[hashed]:
                del self.collection[hashed][key]

    def lookup(self,key):
        hashed = self.hash(key)
        
        if hashed in self.collection:
            if key in self.collection[hashed]:
                return self.collection[hashed][key]
            else:
                return None

table = HashTable()

print(table.lookup("golf"))

table.add("golf", "sport")
print(table.lookup("golf"))

table.add("fcc", "coding")
table.add("cfc", "chemical")

print(table.collection)

table.remove("fcc")
print(table.collection)

print(table.lookup("cfc"))
print(table.lookup("fcc"))
