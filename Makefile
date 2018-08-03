# the library name
name = data-process
# may change to pip3 or python3 -m pip, etc.
pip = pip3

.PHONY: build
build:
	python setup.py sdist
	python setup.py bdist_wheel --universal

.PHONY: install
install: clean build
	$(pip) install --force-reinstall ./dist/*.whl

.PHONY: publish
publish: clean build
	twine upload dist/* && git push

.PHONY: uninstall
uninstall:
	$(pip) uninstall $(name)

.PHONY: clean
clean:
	rm -fr build dist *.egg-info
