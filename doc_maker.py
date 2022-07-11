from __future__ import print_function
import datetime



from mailmerge import MailMerge

import json

def make_document(input_data):
	template = r"C:\Users\astur\Downloads\Skybound_Paysheet.docx"

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

		line_row = {'product_name': 'REMOSGX Rental','product_rate': '$'+str(data['remos_hourly_rate']),'product_quantity': str(hobbs_total),'product_total': '$'+str(total_cost)}
		sales_history.append(line_row)



	groundstart = data['ground_start']
	groundstop = data['ground_stop']
	#Generate Ground Total
	if not groundstart == '' and not groundstop == '':
		print("Times",groundstart,groundstop)


		


	#Add Date
	today = datetime.date.today()
	data['date'] = str(today.month) +'/'+ str(today.day) +'/'+str(today.year)

	

	print(data)





	#Write to Merge Fields inside Document
	document.merge_rows('product_name', sales_history)
	document.merge(**data)
		
	#Output File
	path = './test-output.docx'
	document.write(path)
	return path


if __name__ == '__main__':


	tail_number='173PM'
	hobbs_in='1221.1'
	hobbs_out='1222.0'
	#ground_start='19:30:21'
	#ground_stop='19:30:21'

	#hobbs_total=hobbs_out-hobbs_in
	destination='KCGI'
	student_name="Lucy Vandeven"
	cfi_name="Alex Sturgeon"
	payment_method="Prepaid"

	product_name = ""
	productprice = ""

	json = {'remos_block10_rate':"110",'remos_block5_rate':"115",'remos_hourly_rate':"120",'cfi_name':"Alex","student_name":student_name,'destination':destination,'payment_method':payment_method,'tailnumber':tail_number,'hobbs_in':hobbs_in,'hobbs_out':hobbs_out,'ground_start':123213,'ground_stop':123132,'product_name':product_name,'productprice':productprice}



	make_document(json)