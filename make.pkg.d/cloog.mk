cloog                   := cloog-0.18.1
cloog_url               := http://www.bastoul.net/cloog/pages/download/$(cloog).tar.gz

prepare-cloog-rule:
	$(PATCH) -d $(cloog) < $(patchdir)/$(cloog)-update-isl.patch

configure-cloog-rule:
	cd $(cloog) && ./$(configure) \
		--disable-silent-rules \
		--enable-portable-binary \
		--with-gcc-arch=$(arch) \
		--with-gmp=system \
		--with-isl=system \
		--with-osl=system

build-cloog-rule:
	$(MAKE) -C $(cloog) all

install-cloog-rule: $(call installed,isl osl)
	$(MAKE) -C $(cloog) install
