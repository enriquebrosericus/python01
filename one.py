#prompt for age and return how old you are.
import datetime


print(f"Enter your age: ")

u_age =  input()

now = datetime.datetime.now()

u_birthyear = now.year - int(u_age)

print(f"My age is {u_age} and I was born in {u_birthyear}")




