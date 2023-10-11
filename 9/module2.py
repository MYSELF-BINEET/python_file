import random as r
import datetime

a = r.randrange(0,6)
b = r.randrange(5,10)
c = r.randrange(0,11,3)
print("Generating integers with a step of 3 between the ranges : ")
print("Random integer between 0 and 6(excluiding 6) :",a)
print("Random integer between 5 and 6(excluiding 10) :",b)
print("Random integer between 0 and 10 :",c)

print("Enter dates in YYYY-MM-DD format : ")
l1 = list(map(int,input("Enter first date : ").split("-")))
l2 = list(map(int,input("Enter second date : ").split("-")))
d1 = datetime.date(l1[0],l1[1],l1[2])
d2 = datetime.date(l2[0],l2[1],l2[2])
print("Date-1 :",d1)
print("Date-2 :",d2)
time_diff = d1 - d2
days_diff = time_diff.days
if days_diff>=0 :
    day = r.randrange(days_diff+1)
    date = d2 + datetime.timedelta(days = day)
else :
	day = r.randrange(days_diff,1)
	date = d2 + datetime.timedelta(days = day)
print("Generating a random date between {} and {} : {}".format(d1,d2,date))
