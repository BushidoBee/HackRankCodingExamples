if __name__ == '__main__':
    student_array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_array.append([name, score])

# grab all scores from students
# print("All records entered: " + str(student_array))

# separate the scores; sort to find second worst grade
scores_array = []
sw_score = 0
for i in range(len(student_array)):
    scores_array.append(student_array[i][1])
scores_array = sorted(scores_array)
# print("Scores separated and Sorted: " + str(scores_array))
s = 0
sw_score = scores_array[s]
while (sw_score == scores_array[s]):
    if sw_score == scores_array[s]:
        s+=1
    else:
        sw_score = scores_array[s]
# print("Second Worst Score is: " + str(scores_array[s]))

# Find Students with 2nd worst score
sw_scores = []
for i in range(len(student_array)):
    if student_array[i][1] == scores_array[s]:
        sw_scores.append(student_array[i][0])
sw_scores = sorted(sw_scores)
# print("Here are the Students: " + str(sw_scores))
for a in sw_scores:
    print(a)
