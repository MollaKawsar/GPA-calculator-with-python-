##user input section 
sub_ban=int(input("Enter Your Mark's here  (Bangla)!:"))
sub_eng=int(input("Enter Your Mark's here  (English)!:"))
sub_math=int(input("Enter Your Mark's here (Math):!"))
sub_sci=int(input("Enter Your Mark's here  (Science)!:"))


# average
Ava=sub_ban + sub_eng + sub_math + sub_sci 
Total_ava=Ava/4
print(f"Average Mark: {Total_ava:.2f}")
#logical site 
if Total_ava >=90 and Total_ava <= 100:
    print("GPA Grade is :'A+'")
elif Total_ava >= 80 and Total_ava < 90 :
    print("GPA Grade is :'A'")
elif Total_ava >=70 and Total_ava <80:
    print("GPA Grade is :'B'")
elif Total_ava >=60 and Total_ava <70:
    print("GPA Grade is :'C'")
elif Total_ava>=40 and Total_ava<60:
    print("GPA Grade is :'D'")
elif Total_ava>=0 and Total_ava<40:
    print("GPA Grade is :'F'")
else:
    print(" Invalid Mark's")