# coding:utf-8

import xlrd

import urllib2 
data = xlrd.open_workbook('../api_list.xls')
table = data.sheet_by_name(u'zhe800_api_list')
col_value_list = table.col_values(1)



def get_api_content():
    i = 1	
    while(i < len(col_value_list)):
 	    #print col_value_list[i]
	    req = urllib2.Request(col_value_list[i]) 
	    req.add_header("User-Agent","tbbz|tao800|864587029106573|Android|4.2.0|wxhc4z")
	    res = urllib2.urlopen(req) 
	    html = res.read() 
	    print html
	    i += 1

if __name__ == "__main__":
	get_api_content()
