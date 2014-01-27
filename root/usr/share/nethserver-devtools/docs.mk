#
# Build UI online documentation
#

RSTFILES        := $(shell find . -name '*.rst')
HTMLFILES       := $(addsuffix .html, $(basename ${RSTFILES}))
RST2HTML        := rst2html 

.PHONY: all

all: ${HTMLFILES}

%.html: %.rst
	${RST2HTML} $< $@

