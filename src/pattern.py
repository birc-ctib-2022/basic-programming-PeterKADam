# Print the pattern

# this is impressivly terrible

listy = []
stop = 5
for each in range(1, stop):
    listy.append(("* " * (each - 1)) + "*")

for each in range(stop, 0, -1):
    listy.append(("* " * (each - 1)) + "*")

# print(listy)
for each in listy:
    print(each)
# print(" ".join([x for x in listy]) + "\n")
