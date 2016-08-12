DEFAULT:
	@echo "usage:"
	@echo "  make cpython    # installs cpython (3.x) dependencies"
	@echo "  make pypy       # installs pypy dependencies"


cpython:
	pip install -r requirements.txt


pypy:
	# pypy 2 doesn't ship with futures
	pip install futures
	make cpython
