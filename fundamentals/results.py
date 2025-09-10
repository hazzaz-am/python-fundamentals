results = ["Mario", "Luigi"]

results.append("Princess")
results.append(["Yoshi", "Koopa"])
results.remove(["Yoshi", "Koopa"])
results.extend(["Yoshi", "Koopa"])

results.remove("Mario")
results.insert(0, "Mario")
results.insert(4, "Bowser")
results.reverse()

print(results)
