%?gnuxc_package_header

Name:           gnuxc-libvpx
Version:        1.3.0
Release:        1%{?dist}
Summary:        Cross-compiled version of %{gnuxc_name} for the GNU system

License:        BSD
Group:          System Environment/Libraries
URL:            http://www.webmproject.org/
Source0:        http://webm.googlecode.com/files/%{gnuxc_name}-v%{version}.tar.bz2

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
%setup -q -n %{gnuxc_name}-v%{version}

%build
%gnuxc_env
CROSS='%{gnuxc_host}-' ./configure \
    --target=generic-gnu \
    --prefix='%{gnuxc_prefix}' \
    --enable-debug \
    --enable-error-concealment \
    --enable-extra-warnings \
    --enable-install-{bin,lib}s \
    --enable-internal-stats \
    --enable-mem-tracker \
    --enable-pic \
    --enable-{,vp9-}postproc \
    --enable-shared \
    --enable-vp{8,9} \
    \
    --disable-install-bins
%gnuxc_make %{?_smp_mflags} all V=1

%install
%gnuxc_make_install V=1

# This link is overkill.
rm -f %{buildroot}%{gnuxc_libdir}/libvpx.so.1.3


%files
%{gnuxc_libdir}/libvpx.so.1
%{gnuxc_libdir}/libvpx.so.%{version}
%doc AUTHORS CHANGELOG LICENSE PATENTS README

%files devel
%{gnuxc_includedir}/vpx
%{gnuxc_libdir}/libvpx.so
%{gnuxc_libdir}/pkgconfig/vpx.pc

%files static
%{gnuxc_libdir}/libvpx.a


%changelog
