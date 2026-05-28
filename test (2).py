#Karina Avila
#Test Scores

scores = [88, 42, 95, 70, 63, 82, 55, 91, 74, 85,
38, 77, 90, 61, 89, 72, 59, 98, 45, 81,
67, 73, 88, 52, 94, 79, 100, 68, 83, 71]

#Challenge 2.1
lowest_num=min(scores)
biggest_num=max(scores)
print(f"The lowest score is: {lowest_num}")
print(f"The highest score is: {biggest_num}")

#Challenge 2.2
total=sum(scores)
number=len(scores)
average=total/number
print(f"Average test score: {average}")

#Challenge 2.3
scores.sort()
print(scores)
lowest_three=scores[0:3]
print(f"Lowest 3 test scores: {lowest_three}")
#Challenge 2.4
#First item gets the value of the first item + 5
for i in range(len(scores)):
    scores [i] = scores [i] + 5


print(scores)
