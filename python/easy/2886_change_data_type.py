# https://leetcode.com/problems/change-data-type/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students.grade.astype(int)
    return students
