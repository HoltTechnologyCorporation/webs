clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete

upload:
	python setup.py sdist upload

.PHONY: clean upload
