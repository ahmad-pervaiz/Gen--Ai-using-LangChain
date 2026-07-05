from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str ='Ali'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=4 ,default=3.0,description='A value representing the cgpa of the student')
    
name={'name':'Ahmad','age':10,'email':'abc@gmail.com','cgpa':3.94}
age={'name':'32'}  # if we pass the '32' then it'll auto typecast the age into int
#when we'll pass this in the run function , it'll throw error because of the miss match stpe
student=Student(**name)
# st2=Student(**age)

st_json=student.model_dump_json()

print(student)
# print(st2)





# Pydantic

# Pydantic is a data validation and data parsing library for Python. It ensures that the data you
# work with is correct, structured, and type-safe.
#  use Cases:
# Basic example
# Default values
# Optional fields
# Coerce
# Builtin validation
# Field Function -> default values, constraints, description, regex
# expressions
# Returns pydantic object -> convert to ison/dict