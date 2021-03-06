%?gnuxc_package_header

Name:           gnuxc-libgpg-error
Version:        1.17
Release:        1%{?dist}
Summary:        Cross-compiled version of %{gnuxc_name} for the GNU system

License:        LGPLv2+
Group:          System Environment/Libraries
URL:            http://www.gnu.org/software/gpg/
Source0:        ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{gnuxc_name}-%{version}.tar.bz2

BuildRequires:  gnuxc-glibc-devel

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       gnuxc-glibc-devel

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{gnuxc_name} on GNU systems.

%package static
Summary:        Static libraries of %{name}
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
The %{name}-static package contains the %{gnuxc_name} static libraries for
-static linking on GNU systems.  You don't need these, unless you link
statically, which is highly discouraged.


%prep
%setup -q -n %{gnuxc_name}-%{version}

# Create a host-dependent header when cross-compiling.
sed 's/i486-pc-gnu/%{gnuxc_target}/g' \
    < src/syscfg/lock-obj-pub.i486-pc-gnu.h \
    > src/syscfg/lock-obj-pub.%{gnuxc_target}.h

%build
%gnuxc_configure \
    --bindir=%{gnuxc_root}/bin \
    --disable-nls \
    \
    --disable-rpath \
    --enable-languages \
    --enable-static \
    --enable-threads=posix
%gnuxc_make %{?_smp_mflags} all

%install
%gnuxc_make_install

# Provide a cross-tools version of the config script.
install -dm 755 %{buildroot}%{_bindir}
ln %{buildroot}%{gnuxc_root}/bin/gpg-error-config \
    %{buildroot}%{_bindir}/%{gnuxc_target}-gpg-error-config

# There is no need to install binary programs in the sysroot.
rm -f %{buildroot}%{gnuxc_root}/bin/gpg-error

# We don't need libtool's help.
rm -f %{buildroot}%{gnuxc_libdir}/libgpg-error.la

# This functionality should be used from the system package.
rm -rf %{buildroot}%{gnuxc_datadir}/{aclocal,common-lisp}

# Skip the documentation.
rm -rf %{buildroot}%{gnuxc_mandir} %{buildroot}%{gnuxc_infodir}


%files
%{gnuxc_libdir}/libgpg-error.so.0
%{gnuxc_libdir}/libgpg-error.so.0.13.0
%doc AUTHORS ChangeLog* COPYING* NEWS README THANKS

%files devel
%{_bindir}/%{gnuxc_target}-gpg-error-config
%{gnuxc_root}/bin/gpg-error-config
%{gnuxc_includedir}/gpg-error.h
%{gnuxc_libdir}/libgpg-error.so

%files static
%{gnuxc_libdir}/libgpg-error.a


%changelog
