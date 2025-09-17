this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
one_tuple = ("apple",)
tuple_constructor = tuple(("apple", "banana", "cherry", "apple", "cherry"))
packed_tuple = ("apple", "audi", "duplex")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")


joined_tuple = one_tuple + tuple_constructor + fruits

print(joined_tuple.index("raspberry"))
print(joined_tuple.count("apple"))

joined_tuple = one_tuple + tuple_constructor + fruits
print(joined_tuple)

multiply_tuple = one_tuple * 2
print(multiply_tuple)

for fruit in this_tuple:
    print(fruit)


(*rest, summer_fruit, winter_fruit) = fruits
print(rest)
print(summer_fruit)
print(winter_fruit)

(summer, all_season, *rest) = fruits
print(rest)
print(summer)

(fruit, car, house) = packed_tuple
print(fruit)
print(car)
print(house)


del one_tuple

remove_tuple_item = list(this_tuple)
remove_tuple_item.remove("kiwi")
remove_tuple_item.pop()
this_tuple = tuple(remove_tuple_item)
print(this_tuple)


that_tuple = ("jackfruit",)
this_tuple += that_tuple
print(this_tuple)

tuple_list = list(this_tuple)
tuple_list.append("jackfruit")
this_tuple = tuple(tuple_list)
print(this_tuple)

convert_into_list = list(this_tuple)
convert_into_list[0] = "jackfruit"
convert_into_tuple = tuple(convert_into_list)
print(convert_into_tuple)
print("melon" in this_tuple)
print(this_tuple[-4:])
print(tuple_constructor)
print(one_tuple)
print(len(this_tuple))
print(this_tuple)
