.PHONY: run test

run:
ifeq ($(OS), Windows_NT)
	py test.py
else
	python3 test.py
endif

test:
	pytest test.py
