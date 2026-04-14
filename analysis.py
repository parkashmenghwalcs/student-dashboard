import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("students.csv")

print(df)

print("Average Marks:", df["Marks"].mean())

# Bar chart
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Student Marks")
plt.show()