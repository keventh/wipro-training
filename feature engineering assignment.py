import pandas as pd
import numpy as np

data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "StudentName": ["Rahul", "Aisha", "John", "Fatima", "Arjun", "Sara", "David", "Priya", "Karan", "Meera"],
    "MathMarks": [78, 92, 65, 88, 95, 70, 60, 85, 98, 74],
    "ScienceMarks": [80, 95, 70, 90, 96, 72, 65, 88, 99, 76],
    "EnglishMarks": [75, 89, 68, 85, 91, 74, 62, 82, 95, 78],
    "StudyHoursPerDay": [2, 5, 1, 4, 6, 3, 1, 4, 7, 2],
    "AttendancePercentage": [70, 95, 60, 88, 98, 80, 55, 90, 99, 72],
    "SportsHoursPerWeek": [5, 2, 8, 3, 1, 4, 10, 2, 1, 6]
}

#Totalmarks
df = pd.DataFrame(data)

df['TotalMarks'] = df['MathMarks'] + df['ScienceMarks'] + df['EnglishMarks']

print(df)

#Average
df['AverageMarks'] = df['TotalMarks'] / 3
print(df)

#PassFailFeature
df['PassStatus'] = df['AverageMarks'].apply(lambda x:'Pass' if x >=40 else 'Fail')
print(df)

#GradeFeature
def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'D'
df['Grade'] = df['AverageMarks'].apply(assign_grade)
print(df)

#HighAttendanceFeature
df['HighAttendance'] = df['AttendancePercentage'] > 85
print(df)

#StudyEfficiency
df['StudyEfficiency'] = df['AverageMarks'] / df['StudyHoursPerDay']
print(df)

#PerformanceIndex
df['PerformanceIndex'] = df['AverageMarks'] + df['AttendancePercentage'] +(df['StudyHoursPerDay']) * 5
print(df)

#SportsCategory
def categorize_sports(hours):
    if hours >= 6:
        return 'High'
    elif hours >= 3:
        return 'Medium'
    else:
        return 'Low'
df['SportsCategory'] = df['SportsHoursPerWeek'].apply(categorize_sports)
print(df)

#Ranking
top_3_students = df.sort_values(by='AverageMarks', ascending=False).head(3)
print(top_3_students)

#ScholarshipEligibility
df['ScholarshipEligible'] = (df['AverageMarks'] > 85) & (df['AttendancePercentage'] > 90)
print(df)

#StrongestSubject
subjects = ['MathMarks', 'ScienceMarks', 'EnglishMarks']
df['StrongestSubject'] = df[subjects].idxmin(axis=1)
print(df)

#WeakestSubject
subjects = ['MathMarks', 'ScienceMarks', 'EnglishMarks']
df['WeakestSubject'] = df[subjects].idxmin(axis=1)
print(df)

#EncodeGrade
grade_map = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
df['GradeEncoded'] = df['Grade'].map(grade_map)
print(df)

#Visualizationchallenge
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Histogram of Average Marks
df['AverageMarks'].hist()
plt.show()

# 2. Scatter plot: StudyHours vs AverageMarks
plt.scatter(df['StudyHoursPerDay'], df['AverageMarks'])
plt.show()

# 3. Pie chart: Grade distribution
df['Grade'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()

# 4. Heatmap: Correlations
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True)
plt.show()

# 5. Boxplot: AttendancePercentage
sns.boxplot(x=df['AttendancePercentage'])
plt.show()