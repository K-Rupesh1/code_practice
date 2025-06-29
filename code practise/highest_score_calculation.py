student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
sum=sum(student_scores)
print(sum)

sum1=0
for score in student_scores:
    sum1+=score
    print(sum1)
print(f"the highest score is :{sum1}")

score=[8,65,89,86,55,91,64,89]
out=sorted(score)
len=len(out)
print(out)
print(f"minimum value is:",out[0])
print(f"maximum value is:",out[len-1])