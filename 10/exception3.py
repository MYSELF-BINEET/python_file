class FormulaError(Exception): pass

def length_check(lst) :
	try :
		if len(lst)!=3 :
			raise FormulaError("Invalid number of elements")
	except :
		print("FormulaError : Invalid number of elements")
		return FormulaError

def evalute(lst) :
	try :
		a = float(lst[0])
		b = float(lst[2])
	except :
		print("FormulaError : Invalid operands")
		return FormulaError
	try :
		if lst[1] == '+':
			val = a+b
			return val
		elif lst[1] == '-' :
			val = a-b
			return val
		else :
			print("FormulaError : Invalid operator")
			return FormulaError
	except :
		print("FormulaError : Invalid operator")
		return FormulaError

while True:
	exp = input("Enter the expression : ")
	if exp=="quit" :
		exit(1)
	lst = exp.split()
	if length_check(lst) != FormulaError :
		val = evalute(lst)
		if val != FormulaError:
		  print("Answer =",val)
			


















