#
# Build UI online documentation
#

RSTFILES        := $(shell find . -name '*.rst')
HTMLFILES       := $(addsuffix .html, $(basename ${RSTFILES}))
RST2HTML        := rst2html --link-stylesheet --stylesheet-path= --stylesheet= \
                            --no-doc-title --no-doc-info

.PHONY: all clean

all: ${HTMLFILES}

%.html: %.rst
	args=`head -1 $< | sed -r -n '/^\.\. +/ {s/^\.\. +//; p}'` ; \
	${RST2HTML} $${args} $< > $@ ; \

clean:
	rm -f ${HTMLFILES}
