"""
Exercise 4 — Conditionals

Write:
score >= 90 → Excellent
score >= 75 → Good
score >= 60 → Average
otherwise   → Needs Improvement

Test at least:
95
80
65
40
"""

score = int(input("Enter the score: "))

if score>=90 and score<=100:
    print("Excellent")
elif score>=75 and score<90:
    print("Good")
elif score>=60 and score<75:
    print("Average")
else:
    print("Needs Improvement")

"""
PS C:\Users\amrit\Desktop\Python Mastering\00_Phase_1\project\Phase_1\lesson_2> python .\exercise_4.py
Enter the score: 95
Excellent
PS C:\Users\amrit\Desktop\Python Mastering\00_Phase_1\project\Phase_1\lesson_2> python .\exercise_4.py
Enter the score: 80
Good
PS C:\Users\amrit\Desktop\Python Mastering\00_Phase_1\project\Phase_1\lesson_2> python .\exercise_4.py
Enter the score: 65
Average
PS C:\Users\amrit\Desktop\Python Mastering\00_Phase_1\project\Phase_1\lesson_2> python .\exercise_4.py
Enter the score: 40
Needs Improvement
"""