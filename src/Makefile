# math makefile

VERSION=$(shell ./math.py version)

SOURCE=math.py

ifndef PREFIX
PREFIX=/usr/local/bin
endif
TARGET=$(PREFIX)/math

ARCHIVE=../archive

all: Makefile

clean:

install:
	@cp $(SOURCE) $(TARGET)
	@chmod +x $(TARGET)

archive: $(ARCHIVE)/v$(VERSION).tar.gz

$(ARCHIVE)/v$(VERSION).tar.gz: $(shell ls -1 .)
	@tar cfz $@ $?
