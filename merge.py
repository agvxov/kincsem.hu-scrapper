import os
import json

src_dir = 'out/'

files = os.listdir(src_dir)
file_count = len(files)

r = []
for i, filename in enumerate(files):
	filepath = src_dir + filename
	with open(filepath, 'r+') as f:
		top_level_json = json.loads(f.read())
		for j in top_level_json:
			r.append(dict(json.loads('{' + j)))
		print(f"\033[32mDone with '{filepath}' ({i+1}/{file_count}).\033[0m")

with open('horsey_data.json', 'w') as f:
	f.write(json.dumps(r))
