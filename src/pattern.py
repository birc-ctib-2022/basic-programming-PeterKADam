# Print the pattern
listy = []
stop = 5
for each in range(1, stop):
    listy.append("*" * each)

for each in range(stop, 0, -1):
    listy.append("*" * each)

print(listy)
print(" ".join([x for x in listy]))
