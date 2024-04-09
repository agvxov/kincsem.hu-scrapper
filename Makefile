fetch: venv
	source venv/bin/activate;\
	script -c 'python lovi_scrapper.py'

venv:
	python -m venv venv

clean:
	-rm out/*

.PHONY: fetch clean
