student_scores = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Diana": 95,
    "Eve": 88,
    "Charlie": 90,
    "Frank": 82,
    "Grace": 91
}

# We calculate the average score of the students
total_scores = sum(student_scores.values())
total_students = len(student_scores)

average_score = total_scores / total_students

# We calculate the highest score and lowest score
highest_score = max(student_scores.values())
lowest_score = min(student_scores.values())

print("The average score of the student is: ", average_score)
print("The highest score is achieved by: ", {name for name, score in student_scores.items() if score == highest_score}, "which is ", highest_score)
print("The Lowest score is achieved by: ", {name for name, score in student_scores.items() if score == lowest_score}, "which is ", lowest_score)