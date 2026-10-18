#Student scores
scores=[85,72,91,64,78]

print("Student Scores:")

for score in scores:
        print(score)

print()

#formulas
total_scores= sum(scores)
average_score= total_scores/len(scores)
highest_score= max(scores)
lowest_score= min(scores)

passed=0
failed=0

#condition

for i, score in enumerate(scores, start=1):

    if score>=90:
        grade = "Excellent"
        status = "Passed"
        passed +=1

    elif score>=80:
         grade = "Very Good"
         status = "Passed"
         passed +=1

    elif score>=75:
         grade = "Good"
         status = "Passed"
         passed +=1

    else :
         grade = ""
         status = "Failed"
         failed +=1

    if grade:
         print(f"Student {i}: {score} - {grade} - {status}")
    else:
         print(f"Student {i}: {score} - {status}")

#display results

print()
print(f"Total Score: {total_scores}")
print(f"Average Score: {average_score:.0f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")