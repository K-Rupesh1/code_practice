print("tip calculator")
bill=float(input("enter bill amount:$"))
tip=int(input("select the bill percentage 10 12 15 :"))
person=int(input("how many persons going to split a bill:"))
#calaculating a tip
tip_per_person=tip/100
print(tip_per_person)
tip_per_all_persons=bill*tip_per_person
print(tip_per_all_persons)
#splitting a bill
bill_per_person=(bill+tip_per_all_persons)/person
print(bill_per_person)

bill=150.00
print(f"the total bill={bill}")
tip=12
print(f"tip is {tip}%")
persons=5
print(f"split bill between {persons} persons")

final_bill=(bill/5)*1.12
print(final_bill)
