
# coding:utf-8

import xlrd
import simplejson
import urllib2 
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

uri1="http://m.api.zhe800.com/deals/v1?image_type=si3&user_type=0&user_role=1&student=0&page=1&per_page=20"
uri2 ="http://m.api.zhe800.com/homepromotion/v2?user_type=1&user_role=1&student=0&platform=android&model=vivo%20X5Pro%20D&image_model=webp&baoyou_type=1&area="

def get_current_api_content():
    req = urllib2.Request(uri1) 
    req.add_header("User-Agent","tbbz|tao800|352571070322932|Android|4.8.6|678b3f|224824")
    #req.add_header("User-Agent","tbbz|tao800|98e026bba2ebb331a972b00da497f059e45eeb4f|iPhone|4.7.0|b2e1cc|71836335")
    
    res = urllib2.urlopen(req) 
    html = res.read() 
    html_dict = simplejson.loads(html)
    #print type(html_dict)
    #print html_dict.items()
    json_str = simplejson.dumps(html_dict)
    #print type(json_str)
    json_content = json_str.decode('unicode_escape')
    print json_content
    #for (k,v) in html_dict.items():
        #print k,">>>",type(html_dict["objects"][0]),html_dict["objects"][0]
            #for (k1,v1) in html_dict["objects"][0].items():
                #print k1,v1                

if __name__ == "__main__":
	get_current_api_content()
