my_set = {"apple", "banana", "cherry"}
this_set = {"pineapple", "mango", "papaya"}
set_constructor = set(("apple", "cherry's"))
tuple_list = ("kiwi", "jackfruit")
my_list = ["orange", "watermelon"]
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
fruits = {"apple", "banana", "cherry", "mango"}

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}


unique_fruits = fruits.symmetric_difference(a)
print(unique_fruits)
x = fruits.issubset(b)
x = fruits.issuperset(a)
print(x)
joint = a.isdisjoint(c)
print(joint)

unique_a = a.difference(b, c)
unique_c = c.difference(a, b)
unique_b = b - c - a
print(unique_b)
x = set1.difference(set2)
print(x)

copy_fruit = fruits.copy()
print(copy_fruit)


set1.symmetric_difference_update(set2)
print(set1)

symmetric_set_1 = set1.symmetric_difference(set2)
symmetric_set_2 = this_set ^ set_constructor


print(symmetric_set_1)
print(symmetric_set_2)

set1.difference_update(set2)
print(set1)


difference_set = set1.difference(set2)
minus_set = my_set - set_constructor
print(difference_set)
print(minus_set)
set3 = set1.intersection(set2)
print(set3)


my_set.intersection_update(set_constructor)
print(my_set)


intersect_set_1 = my_set.intersection(set4)
intersect_set_2 = set_constructor & set4
print(intersect_set_2)


set_tuple = set2.union(tuple_list)
print(set_tuple)


join_all_set_1 = set1.union(set2, set3, set4)
join_all_set_2 = set1 | set2 | set3 | set4
print(join_all_set_2)
print(join_all_set_1)

join_set_1 = my_set.union(this_set)
join_set_2 = this_set | set_constructor
print(join_set_2)


my_set.clear()
del this_set
my_set.add("hello")
print(my_set)
popped = my_set.pop()
print(popped)
my_set.remove("cherry")
print(my_set)
my_set.discard("cherry")
print(my_set)
my_set.update(tuple_list)
my_set.update(my_list)
print(my_set)


my_set.update(this_set)
print(my_set)
print(this_set)
my_set.add("mango")
print(my_set)

print("jackfruit" in this_set)
if "mango" in my_set:
    print("mango")
else:
    print("No mango")

for fruit in my_set:
    print(fruit)

print(set_constructor)
print(type(my_set))
print(len(my_set))
print(this_set)
print(my_set)
