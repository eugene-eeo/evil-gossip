DEFAULT:
	@echo "usage:"
	@echo "  make cpython    # installs cpython (3.x) dependencies"
	@echo "  make pypy       # installs pypy dependencies"
	@echo "  make test       # runs the tests"


test:
	pip install hypothesis nose
	nosetests


cpython:
	pip install -r requirements.txt


pypy:
	# pypy 2 doesn't ship with futures
	pip install futures
	make cpython
