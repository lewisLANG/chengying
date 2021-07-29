# -*- coding:utf-8 -*-
import requests
import json

hang = "ip,port,hostname,country\r"
query = '搜索语句'
start = 0

def write_into_csv(start, query):
	headers = {"X-QuakeToken": "apikey"}
	data = {
		"query": query,
		"start": start,
		"size": 10
	}
	#transport、service、images、location、hostname、components、org、port、os_name、is_ipv6、time、ip、asn、os_version
	response = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
	datajson = response.json()
	with open("test.csv","a") as f:
		for data in datajson["data"]:
			f.write("{},{},{},{}\r".format(data["ip"],data["port"],data["hostname"],data["location"]["country_en"]))
		f.close()
	return datajson["meta"]["pagination"]["total"]
with open("test.csv","a") as f:
	f.write(hang)
	f.close()
total = write_into_csv(start, query)
while start < total:
	start = start+10
	write_into_csv(start, query)
