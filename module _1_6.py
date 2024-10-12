my_dict = {"Alexandr": 1990, "Galya": 1999, "Alexey": 1991, "Victory": 1994}
print(my_dict)
print(my_dict["Galya"])
print(my_dict.get("Antone","Такого ключа нет в словаре"))
my_dict.update({"Vladimir": 998, "Vladislav": 1366})
my_dict_changed = my_dict.pop("Alexandr")
print(my_dict_changed)
print(my_dict)

my_set = {13, 25, 6, (8,8,8), "Date of Birth", True, 25, 25, "Яблоко", 13, 13, "Яблоко", True, "Date of Birth"}
print(my_set)
my_set.add("Бирюса"), my_set.add((6,6,6)), my_set.discard("Date of Birth")
print(my_set)