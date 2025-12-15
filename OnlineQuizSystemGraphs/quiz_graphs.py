import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("quiz_data.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# Graph 1: Correct vs Wrong Answers (Line Graph)
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Correct_Answers'], marker='o', label='Correct Answers')
plt.plot(df['Date'], df['Wrong_Answers'], marker='o', label='Wrong Answers')
plt.title("Online Quiz System: Correct vs Wrong Answers")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 2: Quizzes Attempted (Bar Chart)
# -----------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Date'], df['Quizzes_Attempted'])
plt.title("Daily Quizzes Attempted")
plt.xlabel("Date")
plt.ylabel("Quizzes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 3: Students Registered (Line Graph)
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Students_Registered'], marker='o')
plt.title("Student Registration Trend")
plt.xlabel("Date")
plt.ylabel("Students")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 4: Average Score (Bar Chart)
# -----------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Date'], df['Average_Score'])
plt.title("Average Score per Day")
plt.xlabel("Date")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 5: Time Spent on Quiz (Line Graph)
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Time_Spent_Minutes'], marker='o')
plt.title("Average Time Spent on Quiz")
plt.xlabel("Date")
plt.ylabel("Time (Minutes)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 6: Pass vs Fail (Bar Chart)
# -----------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Date'], df['Pass_Count'], label='Pass')
plt.bar(df['Date'], df['Fail_Count'], bottom=df['Pass_Count'], label='Fail')
plt.title("Pass vs Fail Students")
plt.xlabel("Date")
plt.ylabel("Students")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 7: Correct Answer Percentage
# -----------------------------
df['Accuracy'] = (df['Correct_Answers'] /
                 (df['Correct_Answers'] + df['Wrong_Answers'])) * 100

plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Accuracy'], marker='o')
plt.title("Quiz Accuracy Percentage")
plt.xlabel("Date")
plt.ylabel("Accuracy (%)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 8: Quiz Participation Trend
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Quizzes_Attempted'], marker='o')
plt.plot(df['Date'], df['Students_Registered'], marker='o')
plt.title("Participation Trend in Online Quiz System")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend(['Quizzes Attempted', 'Students Registered'])
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
