try:
	data=int(input("please enter a number:"))
	if data==10:
		raise ZeroDivisionError
	else:
		raise TypeError
except ZeroDivisionError:
	print("From ZeroDivisionError")
except TypeError:
	print("this is TypeError")