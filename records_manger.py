import openpyxl
import os
from datetime import datetime




class excel_record:
	def __init__(self,filename):
		self.filename = filename

		self.headers = ['Date','Student','Flight Time','Ground Time','Bill Status','Notes']

		self.open_file()

	def open_file(self):
		if os.path.exists(os.getcwd() + '\\' + self.filename): #Check if file Exists,
			self.wb = openpyxl.load_workbook(filename=self.filename)

		else: # if not create it and add headers
			self.wb = openpyxl.Workbook()
			self.wb.active.append(self.headers)
			self.save()

	def save(self):
		try:
			self.wb.save(self.filename)
		except PermissionError:
			print("[!] Permission Error - Could not save file, is the file open?")
	def add_entry(self,list_of_data):
		self.wb.active.append(list_of_data)
		self.save()

	def add_flight(self,student_name,flight_time,ground_time,notes):
		write_data = [datetime.now().strftime("%m/%d/%Y")  , student_name.title() ,flight_time, ground_time,notes ]
		self.add_entry(write_data)

		

	
if __name__ == "__main__":
	file_name = 'work_time_sheet.xlsx'
	database = excel_record(file_name)
	database.add_flight('john doe' , 1.23 , 3.3 , "")
