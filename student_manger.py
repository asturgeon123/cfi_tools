
from flask import Flask, render_template, Response, request, redirect, url_for, send_from_directory, make_response,send_file
import io
from flask import jsonify
import json

import os
import subprocess

from doc_maker import make_document
from records_manger import excel_record



#print(document.get_merge_fields())






app = Flask(__name__, static_folder='', static_url_path='')
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    	print("nigga shit")
    else:
        return send_from_directory('', 'index.html')

@app.route("/pdf_gen", methods=['POST'])
def pdf_gen():
	
	data = request.get_json()
	#data = request.form
	print(data)



	path,data = make_document(data)

	timesheet = excel_record("time_sheet.xlsx")
	timesheet.add_flight(data['student_name'],data['hobbs_total'],data['ground_total'],"") #Log Flight in Time sheet


	print("Input Path", path)


	#Write Command Line arg to, Convert DOCX to PDF
	#os.system('docx2pdf ' + path + 'Skybound_Paysheet.pdf')
	#process = subprocess.Popen(['docx2pdf', path,'Skybound_Paysheet.pdf'])
	if os.name == 'nt': #If windows 
		process = subprocess.call(['docx2pdf', path, path[:-4] + 'pdf'])

	else: #Not windows
		print(os.name)
		process = subprocess.call(['libreoffice --headless --convert-to pdf '+path],shell=True)

	
	resp = jsonify(success=True)
	return resp


@app.route('/pdf', methods=['GET'])
def get_pdf():
    if request.method == 'POST':
    	print("nigga shit")
    else:
    	return send_from_directory('', 'test-output.pdf')






if __name__ == '__main__':
    #app.run()
    app.run(debug=False,host="0.0.0.0")