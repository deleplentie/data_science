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


# Individual school summary
### Merge the first task with this output
# print(school_data_complete)


# per student budget

def per_student_budget(data, col_school, col_budget, col_total_student):
    individual_budget = int()
    output = {'school_name': [1, 2, 3, 4, 5], 'Per Student Budget': [], 'Total Students': []}
    take_in = []

    # loop through school name, budget & size, divide budget by number of students. #
    # for school, budget, num_of_student in zip(data[col_school], data[col_budget], data[col_total_student]):
    #     individual_budget = budget / num_of_student
    #     # take_in =
    #     output['school_name'] = [school]
    #     output['Per Student Budget'] = [individual_budget]
    #     output['Total Students'] = [num_of_student]

    return output['school_name'][3]


print(per_student_budget(school_data_complete, 'school_name', 'budget', 'size'))
# print((school_data_complete))
