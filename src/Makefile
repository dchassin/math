# math makefile

SRCDIR=$(PWD)

SOURCE=$(SRCDIR)/math.py
ARCHIVE=$(subst /src,/archive,$(SRCDIR))
$(info $(ARCHIVE))

ifndef PREFIX
PREFIX=/usr/local/bin
endif
TARGET=$(PREFIX)/math

VERSION=$(shell $(SOURCE) version)

all: $(SRCDIR)/Makefile
	@chmod +x $(SOURCE)

clean:

install:
	@cp $(SOURCE) $(TARGET)
	@chmod +x $(TARGET)

uninstall:
	@rm -rf $(TARGET)

archive: $(ARCHIVE)/v$(VERSION).tar.gz

$(ARCHIVE)/v$(VERSION).tar.gz: $(SOURCE) $(SRCDIR)/Makefile
	(cd $(SRCDIR); tar cfz $@ .)
