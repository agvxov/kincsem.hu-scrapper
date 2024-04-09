#!/bin/python
import re
import json
import requests as reqs
import bs4

def get_page(url : str) -> str:
	print(f"\033[33mLoading '{url}'...\033[0m")
	p = reqs.get(url)
	print(f"\033[32mLoaded '{url}'!\033[0m")
	return p.text

def js_coll_2_py(c : str):
	r = c.replace(' true,', ' True,')
	return eval(r)

def collect_horsey_pages(txt : str) -> [str]:
	r = []
	day_list_regex = r"(?<=racing_days = )\[.*\](?=;)"
	matches = re.findall(day_list_regex, txt)
	for m in matches:
		v = js_coll_2_py(m)
		for e in v:
			r.append(e['date'])
	return r

def parse_horsey_page(s : str) -> [dict]:
	r = []
	info_dump_regex = r'(?<=races_table_divs)\[".*"\] = {.*}(?=;)'
	matches = re.findall(info_dump_regex, s)
	for m in matches:
		r.append(m[m.find('{') + 1:])
	return r

def main():
	year_range = range(1996, 2024 + 1)
	year_url = 'https://mla.kincsempark.hu/racing-days/gallop/{year}'
	date_url = 'https://mla.kincsempark.hu/results/gallop/{date}/'
	for i in year_range:
		print(f"\033[33;1m# Iterating '{i}'.\033[0m")
		for h in collect_horsey_pages(get_page(year_url.format(year=i))):
			data = parse_horsey_page(get_page(date_url.format(date=h)))
			filename = f"out/{h}.json"
			print(f"\033[36mSaving file '{filename}'.\033[0m")
			with open(filename, 'w') as f:
				json.dump(data, f)
		print(f"\033[32;1m# Done iterating '{i}'.\033[0m")
		

if __name__ == '__main__':
	main()
