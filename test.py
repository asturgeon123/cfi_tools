from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

# Define the templates - assumes they are in the same directory as the code
template = r"C:\Users\astur\Downloads\Skybound_Paysheet.docx"
document = MailMerge(template)





# Final Example includes a table with the sales history

sales_history = [{
    'product_name': 'Red Shoes',
    'product_rate': '$10.00',
    'product_quantity': '2500',
    'total_purchases': '$25,000.00'
}, {
    'product_name': 'Green Shirt',
    'product_rate': '$20.00',
    'product_quantity': '10000',
    'total_purchases': '$200,000.00'
}, {
    'product_name': 'Purple belt',
    'product_rate': '$5.00',
    'product_quantity': '5000',
    'total_purchases': '$25,000.00'
}]


document.merge_rows('product_name', sales_history)
document.write('example3.docx')