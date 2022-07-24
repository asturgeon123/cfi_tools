

import datetime
import json
import os

from mailmerge import MailMerge




def time_string_to_decimals(time_string):
    fields = time_string.split(":")
    hours = fields[0] if len(fields) > 0 else 0.0
    minutes = fields[1] if len(fields) > 1 else 0.0
    seconds = fields[2] if len(fields) > 2 else 0.0
    return float(hours) + (float(minutes) / 60.0) + (float(seconds) / pow(60.0, 2))

def make_document(input_data):
	template = r"./Skybound_Paysheet.docx"

	document = MailMerge(template)

	sales_history = []
	grand_total = 0


	#load Data

	data = input_data

	#Generate Flight Total
	if not data['hobbs_in'] == '' and not data['hobbs_out'] == '':

		hobbs1 = float(data['hobbs_in'])
		hobbs2 = float(data['hobbs_out'])
		hobbs_total = round(hobbs2 - hobbs1,1)
		data['hobbs_total'] = str(hobbs_total)

		total_cost = hobbs_total*float(data['remos_hourly_rate'])
		grand_total += total_cost

		#Add Product to Sales receipt

		line_row = {'product_name': 'Remos Rental','product_rate': '$'+str(data['remos_hourly_rate']),'product_quantity': str(round(hobbs_total,2)),'product_total': '$'+str(total_cost)}
		sales_history.append(line_row)

		total_cost = hobbs_total*float(data['flight_instruction_rate'])
		grand_total += total_cost

		line_row = {'product_name': 'Flight Instruction','product_rate': '$'+str(data['flight_instruction_rate']),'product_quantity': str(round(hobbs_total,2)),'product_total': '$'+str(round(total_cost,2))}
		sales_history.append(line_row)





	groundstart = data['ground_start']
	groundstop = data['ground_stop']
	#Generate Ground Total
	if not groundstart == '' and not groundstop == '':
		print("Times",groundstart,groundstop)

		#Calculate Ground Time
		time_delta = datetime.datetime.strptime(groundstop,"%H:%M") - datetime.datetime.strptime(groundstart,"%H:%M")

		time_total_decimal = round(time_string_to_decimals(str(time_delta)),1)

		#Calcualte Cost
		total_cost = round(time_total_decimal * float(data['ground_instruction_rate']),2)
		grand_total += total_cost

		data['ground_total'] = str(time_total_decimal)
		print("Ground Total",data['ground_total'])

		#Add Product to Sales receipt
		line_row = {'product_name': 'Ground Instruction','product_rate': '$'+data['ground_instruction_rate'],'product_quantity': str(round(time_total_decimal,2)),'product_total': '$'+str(total_cost)}
		sales_history.append(line_row)


	#Generate Other Product Total
	product_name = data['product_name']
	productprice = data['productprice']
	if not product_name == '' and not productprice == '':
		print("Adding Product: ")

		#Calcualte Cost
		total_cost = round(float(productprice),2)
		grand_total += total_cost

		#Add Product to Sales receipt
		line_row = {'product_name': product_name,'product_rate': '$'+productprice,'product_quantity': '1','product_total': '$'+str(total_cost)}
		sales_history.append(line_row)


		


	#Add Date
	today = datetime.date.today()
	data['date'] = str(today.month) +'/'+ str(today.day) +'/'+str(today.year)

	

	print(data)



	#Add Final Total Cost
	data['grand_total'] = str(round(grand_total,2))

	#Write to Merge Fields inside Document
	document.merge_rows('product_name', sales_history)
	document.merge(**data)
		
	#Output File
	path = os.getcwd() + '/test-output.docx'
	document.write(path)
	return [path,data]


if __name__ == "__main__":
	json = {'ground_instruction_rate':"50",'flight_instruction_rate':"50",'remos_block10_rate': '110', 'remos_block5_rate': '115', 'remos_hourly_rate': '120', 'cfi_name': 'Alex Sturgeon', 'student_name': 'Student Name', 'destination': 'KCGI', 'payment_method': 'Cash', 'tailnumber': '173PM', 'hobbs_in': '1234', 'hobbs_out': '1235.3', 'ground_start': '11:49', 'ground_stop': '13:52', 'product_name': 'PRODUCT 1', 'productprice': '204', 'hobbs_total': '1.0', 'date': '7/11/2022'}

	make_document(json)