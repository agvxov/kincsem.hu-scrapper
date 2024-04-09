import os
import json

src_dir = 'out/'

files = os.listdir(src_dir)
file_count = len(files)

for i, filename in enumerate(files):
	filepath = src_dir + filename
	with open(filepath, 'r+') as f:
		print(f"\033[33mExploding '{filepath}' ({i+1}/{file_count})...\033[0m")
		top_level_json = json.loads(f.read())
		r = []
		for j in top_level_json:
			r.append(dict(json.loads('{' + j)))
		f.seek(0)
		f.write(str(r))
		print(f"\033[32mDone with '{filepath}' ({i+1}/{file_count}).\033[0m")
