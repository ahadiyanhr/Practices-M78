import pickle
import dill

class User:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name} <{self.phone}>"
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


# Unpickling:
with open("users.pickled", 'rb') as f:
    users = pickle.load(f)

# Sort the instances based ID and write them to a file:
sorted_items = sorted(users, key=lambda x: x.id)
with open("output-q-3-1.txt", 'w') as f:
    for item in sorted_items:
        # write each item on a new line
        f.write("%s\n" % item)

# Filter the instances based PHONE(0919) and write them to a file:
filter_items = [x for x in users if x.phone[:4] == '0919']
with open("output-q-3-2.txt", 'w') as f:
    for item in filter_items:
        # write each item on a new line
        f.write("%s\n" % item)


# Write fullname of instances to a dill file:       
fullnames_list = [x.fullname() for x in users]
with open("output-q-3-3.dill", 'wb') as f:
    dill.dump(fullnames_list, f)



    