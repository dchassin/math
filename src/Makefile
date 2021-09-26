# math makefile

VERSION=$(shell ./math.py version)

SOURCE=src/math.py

ifndef PREFIX
PREFIX=/usr/local/bin
endif
TARGET=$(PREFIX)/math

ARCHIVE=../archive

all: Makefile
	@chmod +x $(TARGET)

clean:

install:
	@cp $(SOURCE) $(TARGET)
	@chmod +x $(TARGET)

uninstall:
	@rm -rf $(TARGET)

archive: $(ARCHIVE)/v$(VERSION).tar.gz

$(ARCHIVE)/v$(VERSION).tar.gz: $(shell ls -1 .)
	@tar cfz $@ $?
