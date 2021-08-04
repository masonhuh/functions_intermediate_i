# UPDATE VALUES IN DICTIONARIES AND LISTS

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1. Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]].

x[1][0] = 15
print(x)


# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]['last_name'] = 'Bryant'
print(students[0])

# 3. In the sports_directory, change 'Messi' to 'Andres'

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# 4. Change the value 20 in z to 30

z[0]['y'] = 30
print(z)

# ITERATE THROUGH A LIST OF DICTIONARIES
# create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

def iterateDictionary(some_list):
    for index in range(len(some_list)):
        for key in some_list[index]:
            print(key + "-" + some_list[index][key])

def itemsIterate(some_list):
    for index in range(len(some_list)):
        for key, value in some_list[index].items():
            print(key + "-" + value)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 
itemsIterate(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;

# GET VALUES FROM A LIST OF DICTIONARIES
#create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# and iterateDictionary2('last_name',students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary2(key_name, some_list):
    for index in range(len(some_list)):
        print(some_list[index][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# ITERATE THROUGH A DICTIONARY WITH LIST VALUES
# create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    for keys in some_dict:
        print(len(some_dict[keys]), keys.upper())
        for items in some_dict[keys]:
            print(items)
        print("")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon



