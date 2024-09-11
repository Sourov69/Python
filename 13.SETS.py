# In python, a set is a buil-in data structure that represents an unordered collection of unique elements.
# Sets are commonly used for tasks that involve  checking presence of element, removing duplicates from list, union , intersection,
# Sets is define by carlie brackets {sets}

info = {"carla", 19, False, 5, 9, 5, 19}
s1 = {1, 2, 5, 6}
s2 = {3, 6, 2, 7}
print(s1.union(s2))                                      # collect all item without repeated value
cities1 = {"Bangladesh", "India", "Pakistan", "Mianmar"}
cities2 = {"Bangladesh", "America", "london", "India"}

print(cities1.union(cities2))                            # {'Mianmar', 'India', 'london', 'Pakistan', 'America', 'Bangladesh'}
print(cities1.intersection(cities2))                     # {'India', 'Bangladesh'}
print(cities1.symmetric_difference(cities2))             # {'America', 'Mianmar', 'Pakistan', 'london'}
# Symmetric_difference means (A Union B) - (A intesection B)

cities1.add("Palestine")
cities2.remove("london")

cities2.clear()
