git                     := git-2.2.1
git_url                 := http://www.kernel.org/pub/software/scm/git/$(git).tar.xz

git_configuration = V=1 \
	prefix=/usr \
	\
	AR='$(AR)' \
	CC='$(CC)' \
	CFLAGS='$(CFLAGS)' \
	LDFLAGS='$(LDFLAGS)' \
	PERL_PATH='$(PERL)' \
	PYTHON_PATH='$(PYTHON)' \
	STRIP= \
	\
	DEFAULT_EDITOR=emacs \
	DEFAULT_PAGER=less \
	GNU_ROFF=YesPlease \
	HAVE_CLOCK_GETTIME=YesPlease \
	HAVE_DEV_TTY=YesPlease \
	NO_CURL=YesPlease \
	NO_OPENSSL=YesPlease \
	NO_TCLTK=YesPlease \
	USE_LIBPCRE=YesPlease

ifneq ($(host),$(build))
git_configuration += \
	NO_PERL=YesPlease \
	UNAME_M=i686-AT386 \
	UNAME_O=GNU \
	UNAME_R=0.5 \
	UNAME_S=GNU \
	UNAME_V='GNU-Mach 1.4/Hurd-0.5'
endif

prepare-git-rule:
# Bypass asciidoc requirement for man pages.
	$(DOWNLOAD) $(git_url:$(git).tar.xz=$(git:git-%=git-manpages-%).tar.xz) | $(TAR) -JC $(git)/Documentation -x

build-git-rule:
	$(MAKE) -C $(git) all $(git_configuration)

install-git-rule: $(call installed,less pcre python zlib) # perl-Error perl-TermReadKey
	$(MAKE) -C $(git) install $(git_configuration)
# Bypass asciidoc requirement for man pages.
	$(INSTALL) -dm 755 $(DESTDIR)/usr/share/man/man{1,5,7}
	$(INSTALL) -pm 644 $(git)/Documentation/man1/* $(DESTDIR)/usr/share/man/man1/
	$(INSTALL) -pm 644 $(git)/Documentation/man5/* $(DESTDIR)/usr/share/man/man5/
	$(INSTALL) -pm 644 $(git)/Documentation/man7/* $(DESTDIR)/usr/share/man/man7/
