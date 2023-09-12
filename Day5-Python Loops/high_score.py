n = int(input("Number of records: "))
scores = input("Enter scores: ").split()
max = int(scores[0])
for i in range(0, n):
    scores[i] = int(scores[i])
    if max<scores[i]:
        max = scores[i]
print(max)
