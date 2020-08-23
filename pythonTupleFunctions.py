def employee_check(work_hours):
	current_max = 0
	employee_of_month = ''

	for em,hr in work_hours:
		if hr > current_max:
			current_max = hr
			employee_of_month = em
		else:
			pass
	return(employee_of_month,current_max)

work_hours = [('Abby',100),('Billy',400),('Cassie',200)]
employee_of_month = employee_check(work_hours) 
print(employee_of_month)