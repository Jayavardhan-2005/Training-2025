# Grade Wise Differentiation
student_marks={'sita':95,
               'akash':80,
               'anvesh':56,
               'honey':41,
               'mallesh':15,
               'arjun':54,
               'mani':29,}
for i,j in student_marks.items():
    if j>=90:
        print(i,":",j,"= A+")
    elif j>=80 and j<90:
        print(i,":",j,"= A")
    elif j>=70 and j<80:
        print( i,":",j,"= B+")
    elif j>=60 and j<70:
        print(i,":",j,"= B")
    elif j>=50 and j<60:
        print(i,":" , j,"= C")
    elif j<50:
        print(i,":",j,"= Fail")