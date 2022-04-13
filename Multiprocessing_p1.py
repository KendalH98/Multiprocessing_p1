import multiprocessing

def print_attendance(attendance_list):
	"""
	function to print record(tuples) in records(list)
	"""
	for attendance in attendance_list:
		print("Name: {0}\nAttendance: {1}\n".format(attendance[0], attendance[1]))

def insert_attendance(attendance, attendance_list):
	"""
	function to add a new record to records(list)
	"""
	attendance_list.append(attendance)
	print("Attendance list updated!\n")
def print_attendees(attendance_list):
	attendees = 0
	for attendance in attendance_list:
		attendees += 1
    
	print("Name: {0}\nAttendees:",attendees)

if __name__ == '__main__':
	with multiprocessing.Manager() as manager:
		# creating a list in server process memory
		attendance_list = manager.list([('Michael', "Present"), ('Jim', "Not Present"), ('Sarah', "Present")])
		# new record to be inserted in records
		new_attendance = ('Kim', "Present")
	


		# creating new processes
		p1 = multiprocessing.Process(target=insert_attendance, args=(new_attendance, attendance_list))
		p2 = multiprocessing.Process(target=print_attendance, args=(attendance_list,))
		p3 = multiprocessing.Process(target=print_attendees, args=(attendance_list,))

		# running process p1 to insert attendance
		p1.start()
		p1.join()

		# running process p2 to print attendance
		p2.start()
		p2.join()

		#running process p3 to print attendees
		p3.start()
		p3.join()
