# In Python, a dictionary is a data structure that stores a collection of key-value pairs
# Dictionaries are unordered, changeable and indexed
# I can easily access the values in a dictionary using their associated keys.
# Dictionary are verry usefull for tasks like mapping, setting, or organize data meaningfully

# {"something is callkeys":"Keys value"}
dic = {
# "Sourov": "Humab beings",
# "phone": "Object"
"Sourov": 90,
"Abir": 80,
"Jeny": 70
}
print("Marks of Sourov is", dic["Sourov"])
print(dic["Abir"])                                   # 80 
info = {"name":"Sourov", "Age":20, "eligiable":True}
print( info)
print( info["Age"] )                                 # 20
# print(info["name2"])
print( info.get( "name2" ) )
print( info. keys( ) )                               # "name", "Age", "eligiable"
print( info.items( ) )

for key, value in info.items():
    print(f"the value corresponding to the key{key} is {value}")