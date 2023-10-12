if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


eval_array = sorted(list(arr))
runner_score = eval_array[0]

for score in range(n):
    # print("Evaluating Score #" + str(score+1) + ": " + str(eval_array[score]))
    if eval_array[score] == max(eval_array):
        continue
    elif eval_array[score] <= max(eval_array) - 1 and eval_array[score] > runner_score:
        runner_score = eval_array[score]
        # print("New Runner-Up is Score #" + str(score+1) + ": " + str(eval_array[score]))
    else:
        continue
    
# print("The Runner-Up is: " + str(runner_score))
print(runner_score)
