#!/usr/local/bin/python
import requests
from lxml import etree
import time
import fp

baseUrl = 'http://dl.v1.1tai.com/score_pics/'
r = requests.get(baseUrl)

html = etree.HTML(r.content)
result = html.xpath('//pre/a/text()')
for item in result:
	if ('../' == item):
		continue
	tryCount = 1
	while (tryCount <= 3):
		secondUrl = baseUrl + item
		picPage = requests.get(secondUrl)
		content = etree.HTML(picPage.content)
		title = content.xpath('//title/text()')
		if (title != '403 Forbidden'):
			pics = content.xpath('//pre/a/text()')
			for pic in pics:
				if ('../' == pic):
					continue
				picUrl = secondUrl + pic
				print picUrl
				req = requests.get(picUrl)
    			with open(str(time.time())+'.png', 'wb') as fp:
    				fp.write(req.content)
			break
		else:
			print 'request error.tryCount = ' + tryCount
			tryCount += 1
