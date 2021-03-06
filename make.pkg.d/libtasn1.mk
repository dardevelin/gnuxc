libtasn1                := libtasn1-4.2
libtasn1_url            := http://ftpmirror.gnu.org/libtasn1/$(libtasn1).tar.gz

configure-libtasn1-rule:
	cd $(libtasn1) && ./$(configure) \
		--disable-silent-rules \
		--enable-gcc-warnings

build-libtasn1-rule:
	$(MAKE) -C $(libtasn1) all

install-libtasn1-rule: $(call installed,glibc)
	$(MAKE) -C $(libtasn1) install
