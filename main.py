# Dependencies and Setup
from ast import parse

import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
district = 'District'


# TASK 1.1, 1.2
### total num of schools
def total_schools(head, row):
    total = 0
    for num in head[row]:
        total += 1
    return total


def budget(data, each_budget):
    total = 0
    for amount in data[each_budget]:
        total += amount
    return total


def avg_score(data, scores):
    math_score = 0
    total_student = 0

    for score in (data[scores]):
        total_student += 1
        math_score += score
    average_score = math_score / total_student

    return round(average_score, 6)


def percentage(data, scores):
    cut_off_mark = 0
    total_student = total_schools(school_data_complete, 'student_name', )

    for score in data[scores]:
        if score >= 70:
            cut_off_mark += 1
    passing_score = (100 / total_student) * cut_off_mark
    return round(passing_score, 6)


def overall_percentage(data, scores_one, scores_two):
    passed = 0
    total_student = total_schools(school_data_complete, 'student_name')
    cut_off = 70

    # check total num of students with math and reading score over 70
    for a, b in zip(data[scores_one], data[scores_two]):
        if a >= cut_off and b >= cut_off:
            passed += 1
    overall = (100 / total_student) * passed
    return round(overall, 6)


# # total_num_of_school
print(f"Total Schools: {total_schools(school_data, 'school_name')}")
#
# # total_num_of_student
print(f"Total Students: {total_schools(school_data_complete, 'student_name')}")
#
# # total_budget
print(f"Total Budget: {budget(school_data, 'budget')}")
#
# # Average math score
print(f"Average Math Score: {avg_score(school_data_complete, 'math_score')}")
#
# # Average reading score
print(f"Average Reading Score: {avg_score(school_data_complete, 'reading_score')}")
#
# # Percentage of passing math score
print(
    f"% Passing Math: {percentage(school_data_complete, 'math_score')}")
#
# # Percentage of passing reading score
print(
    f"% Passing Reading: {percentage(school_data_complete, 'reading_score')}")
#
# # Percentage of passing reading score & math score
print(
    f"% Overall Passing: {overall_percentage(school_data_complete, 'reading_score', 'math_score')}")

######Create a dataframe to hold the above results#######


new_data = {'Total Schools': [total_schools(school_data, 'school_name')],
            'Total Students': [total_schools(school_data_complete, 'student_name')],
            'Total Budget': [budget(school_data, 'budget')],
            'Average Math Score': [avg_score(school_data_complete, 'math_score')],
            '% Passing Math': [percentage(school_data_complete, 'math_score')],
            '% Passing Reading': [percentage(school_data_complete, 'reading_score')],
            '% Overall Passing': [overall_percentage(school_data_complete, 'reading_score', 'math_score')]}


# Create the outcome in a data frame and store as new csv file.
district_summary = pd.DataFrame(new_data)
output = district_summary.to_csv("./Resources/district_summary.csv")
#Outcome:
print(f"\n\n{district_summary}")

