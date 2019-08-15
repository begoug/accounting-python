all:build install_user

.PHONY:build
build:
	cd source && python3.7 setup.py bdist_wheel

install_user:
	cd source && pip3.7 install --user --upgrade dist/*.whl

doc:
	cd docsource && make html

gitpage:
	rm -rf docs/* && cp -r docsource/build/html/* docs
