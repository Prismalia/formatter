CWD := $(shell pwd)
HOME_DIR := $(shell echo $$HOME)

all: install

install:
	ln -sf $(CWD)/pformat $(HOME_DIR)/.local/bin/pformat

test:
	bash_unit tests/*.sh

