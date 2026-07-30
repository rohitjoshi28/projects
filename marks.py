s1 = int(input("Enter First Student Marks:"))
s2 = int(input("Enter Second Student Marks:"))
s3 = int(input("Enter Third Student Marks:"))
s4 = int(input("Enter Fourth Student Marks:"))
s5 = int(input("Enter Fifth Student Marks:"))

if s1 <= 33 :
    print("First Student is Fail")
if s2 <= 33 :
    print("Second Student is Fail")
if s3 <= 33 :
    print("Third Student is Fail")
if s4 <= 33 :
    print("Fourth Student is Fail")
if s5 <= 33 :
    print("Fifth Student is Fail")


avg = ((s1+s2+s3+s4+s5)/5)
print("Avg:",avg)

highm = max(s1,s2,s3,s4,s5)
print("Highest Marks is:",highm)

total = (s1+s2+s3+s4+s5)
print("Total:",total)

