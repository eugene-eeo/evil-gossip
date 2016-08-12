DEFAULT:
	@echo "usage:"
	@echo "  make cpython    # installs cpython (3.x) dependencies"
	@echo "  make pypy       # installs pypy dependencies"


cpython:
	pip install -r requirements.txt


pypy:
	# pypy3 and 2 doesn't ship with statistics.
	pip install statistics futures
	make cpython
