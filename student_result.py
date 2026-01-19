students = [
	["Ram", 80],
	["Ganesh", 97],
	["Radh", 69],
	["Rita", 30],
	["Kamal", 40]
]
pass_count = 0
fail_count = 0

for s in students:
	name =s[0]
	marks =s[1]

	if marks >= 35:
	    result = "Pass"
	    pass_count += 1
	else:
	    result = "fail"
	    fail_count +=1
	print(name, "-", marks,"-", result)
print("Total Pass:", pass_count)
print("Total Fail:", fail_count)	

