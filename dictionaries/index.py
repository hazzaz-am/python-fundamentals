this_dict = {"brand": "Ford", "model": "Mustang", "year": 2020, "color": "black"}

dict_constructor = dict(name="Hazzaz", age=24, country="Turkey")

my_family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}


x = ("key1", "key2", "key3")
y = 0


this_dict.update(dict_constructor)

print(this_dict)


color_dict = this_dict.setdefault("color", "white")
print(color_dict)
print(this_dict)


new_dict = dict.fromkeys(x, y)
print(new_dict)


for key, child in my_family.items():
    print(key)

    for key, value in child.items():
        print(f"{key}: {value}")


print(my_family["child2"]["year"])

dict_copied = dict(this_dict)
print(dict_copied)
new_dict = this_dict.copy()
new_dict["year"] = 2028
print(new_dict)
print(this_dict)


for key, value in this_dict.items():
    print(key, value)


for key in dict_constructor:
    print(dict_constructor[key])

for value in dict_constructor.values():
    print(value)


this_dict.pop("colors")
this_dict.popitem()
del this_dict["year"]
del this_dict
this_dict.clear()
print(this_dict)


dict_constructor.update(this_dict)
print(dict_constructor)
print("age" in dict_constructor)
as_tuples = this_dict.items()
print(as_tuples)
dict_constructor["car"] = "audi"
print(dict_constructor.keys())
print(dict_constructor.values())
print(dict_constructor.get("country"))
print(dict_constructor["age"])
print(len(this_dict))
print(this_dict)
