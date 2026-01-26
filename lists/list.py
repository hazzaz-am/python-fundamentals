this_list = ["apple", "banana", "banana"]
this_list_1 = list(("orange", "cherry"))

new_list = this_list + this_list_1
this_list.extend(this_list_1)
# print(new_list)
# print(this_list)

new_list = list(this_list)
new_list = this_list[:]
this_list[0] = "Apple"
new_list[1] = "Banana"
# print(this_list)
# print(new_list)
number_list = [12, 237, 134, 834, 95,]
this_list.sort(key= str.lower)
# print(this_list)
new_list = [x if x != "banana" else "orange" for x in this_list]
# print(new_list)

new_list = [x for x in range(10) if x <= 5]
# print(new_list)

new_list = [x for x in this_list if x[0] == "a"]
# print(this_list)
# print(new_list)

this_list[1:3] = ["strawberry", "mango", "jackfruit"]
this_list[1:3] = ["pineapple"]
# print(this_list)

for fruit in range(len(this_list)):
  print(fruit)


this_list.append("orange")

this_list.clear()

copy_list = this_list.copy()

this_list[0] = "Apple"

# print(this_list)
# print(copy_list)
# print(this_list.count("banana"))

this_list.extend(copy_list)
points = (1, 3, 5, 6)
this_list.extend(points)
# print(this_list.index("banana"))

this_list.insert(1, "orange")
this_list.pop()
this_list.remove("banana")
this_list.reverse()
this_list.sort()
# print(type(this_list))
# print(this_list_1)

if "orange" in this_list:
    print(this_list.index("orange"))
