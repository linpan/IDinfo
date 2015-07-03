# -*- coding: utf-8 -*-
#!/usr/bin/env python

#-----------------------------------------------------------------------
# developer :linpan
# time:20150705
# for any suggestions or improvements, my gmail is :yidiyu0507s@163.com
#-----------------------------------------------------------------------
'''ip查询调用的api接口http://apistore.baidu.com/apiworks/servicedetail/113.html
  logging,base64 format module的使用
  特别说明，编码问题unicode utf-8。
'''
import sys, urllib, urllib2, json,base64
import logging,json

logger = logging.getLogger('id')  
logger.setLevel(logging.DEBUG)
hdr=logging.StreamHandler()
format=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
hdr.setFormatter(format)
logger.addHandler(hdr)
#id check in here!
def readId(idinfo):
	yourid=idinfo.decode('utf-8')
	if yourid.isnumeric():
		if  len(yourid)>=15 and len(yourid)<=18:
			return yourid
		else:
			newid=raw_input('please in input your id:').encode()
			readId(newid)
			

idinfo=raw_input('please in input your id:').encode()
id=readId(idinfo)
logger.debug('inputidis:%s'%id)
apkey=' d30857accf5c58253313ed4cb663a18a'
url = 'http://apis.baidu.com/apistore/idservice/id?id={0}'.format(id)
logger.debug('apikeycode is right:%s'%url)

try:
	if yourid in url:
		logger.debug('apikeycode is right:(%s)'%url)

except:
	logger.debug('somewrong here!')


caki=base64.encodestring(apkey)
logger.debug('apikeycode is right:%s'%caki)

req = urllib2.Request(url)

req.add_header("apikey",base64.decodestring(caki))

resp = urllib2.urlopen(req)
content = resp.read()
iddata=json.loads(content)
sex= iddata['retData']['sex']
birthday=iddata['retData']['birthday']
addr=iddata['retData'][u'address'].encode('utf-8')
logger.debug('sex:%s'%sex)
print '-----Start-------'
print 'your sex is:{0}\nyour birthday is:{1}\nyour address is:{2}'.format(sex,birthday,addr)
