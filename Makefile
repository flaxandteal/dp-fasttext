.PHONY: all build test

all: build test

build: requirements model

requirements:
	pip install -r requirements.txt

fastText:
	git submodule sync --recursive
	git submodule update --init --recursive
	pip install Cython==0.27.3 pybind11==2.2.3
	cd lib/fastText && python setup.py clean --all install

model: fastText
	python build_model.py supervised_models/ons_labelled.txt supervised_models/ons_supervised.bin

test: build
	pip install -r requirements_test.txt
	nosetests -s -v tests/
