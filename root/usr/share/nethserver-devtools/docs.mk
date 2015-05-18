#
# Build UI online documentation
#

vpath %.rst /usr/share/nethserver-devtools

RSTFILES        := $(shell find . -name '*.rst')
HTMLFILES       := $(addsuffix .html, $(basename ${RSTFILES}))
RST2HTML        := rst2html --link-stylesheet --stylesheet-path= --stylesheet= \
                            --no-doc-title --no-doc-info

RST_INCLUDES	:= roles.rst
XML_LANG	?= en

.PHONY: all clean

all: ${HTMLFILES}

%.html: $(RST_INCLUDES) %.rst
	args=`head -1 $(lastword $^) | sed -r -n '/^\.\. +/ {s/^\.\. +//; p}'` ; \
	cat $^ | ${RST2HTML} -l $(XML_LANG) $${args} /dev/stdin  >$@

clean:
	rm -f ${HTMLFILES}
