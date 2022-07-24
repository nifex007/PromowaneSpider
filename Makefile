.PHONY: setup, run


setup:
	pip install -r requirements.txt


run:
	scrapy runspider crawler/core.py

