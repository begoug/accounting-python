build:
	python setup.py bdist_wheel

install_user:
	pip install --user dist/*.whl
