clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete

upload:
	python setup.py sdist upload; sudo python setup.py develop

.PHONY: clean upload
