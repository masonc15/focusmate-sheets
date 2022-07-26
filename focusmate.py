import requests
import gspread
import json

row_num = 1
col_num = 1

gc = gspread.oauth()
sh = gc.open_by_key('1QUTuje1-v6HU2j4cOC0uEBycc0gJwUCCZLw3-sAQyi4')
worksheet = sh.get_worksheet(0)

insert_row = 1
insert_col = 2

# cell_value = worksheet.cell(row_num, col_num).value
# print(cell_value)

url = "https://api.focusmate.com/v1/me"

payload = {}
headers = {'X-API-KEY': '0620bc9746ef49de98214cc49c0c4fd0'}

response = requests.request("GET", url, headers=headers, data=payload)

##print(response.text)

# convert GET response to JSON
json_response = json.loads(response.text)

total_session_count = json_response['user']['totalSessionCount']

worksheet.update_cell(insert_row, insert_col, total_session_count)