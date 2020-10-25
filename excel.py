import xlsxwriter
from database import cursor

workbook = xlsxwriter.Workbook('static/doc/db.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

query = """select * from Usser"""
cursor.execute(query)
data_Usser = cursor.fetchall()

# def insert(chat_id, instagram, instagram_id,username,first_name ,last_name):

for user_id, chat_id, instagram, instagram_id,username,first_name ,last_name in data_Usser:
    worksheet.write(row, col, user_id)
    worksheet.write(row, col+1, chat_id)
    worksheet.write(row, col+2, instagram)
    worksheet.write(row, col+3, instagram_id)
    worksheet.write(row, col+4, username)
    worksheet.write(row, col+5, first_name)
    worksheet.write(row, col+6, last_name)
    row += 1

workbook.close()
