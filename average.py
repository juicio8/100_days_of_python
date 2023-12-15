students = input("Input a list of students height: ").split()

count = 0
heights = 0

for n in range(0, len(students)):
    print(n)
    count += 1
    heights += int(students[n])

print(f"avg: {round(heights/count)}")
