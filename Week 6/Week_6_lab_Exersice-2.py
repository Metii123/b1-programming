student_records = []
stats = {}
unique_scores = ()

for i in range(1,3):
    name = input(f"Student {i} name: ")
    score = int(input(f"Student {i} score: "))
    student_records.append((name, score))
    print()

scores = []
for name, score in student_records:
    scores.append(score)

stats["highest"] = max(scores)
stats["lowest"] = min(scores)
stats["average"] = sum(scores)/len(scores)

unique_scores = set(scores)

grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1

print("=== Student Records ===")
print(student_records)
print()
print("=== Class Statistics ===")
print(f"Highest Score: {stats["highest"]}")
print(f"Lowest Score: {stats["lowest"]}")
print(f"Average Score: {stats["average"]}")
print()
print("===Unique Scores===")
print(unique_scores)
print(f"Total unique scores: {len(unique_scores)}")
print()
print("=== Grade Distribution ===")
