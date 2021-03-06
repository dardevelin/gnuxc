%?gnuxc_package_header

Name:           gnuxc-pixman
Version:        0.32.6
Release:        1%{?dist}
Summary:        Cross-compiled version of %{gnuxc_name} for the GNU system

License:        MIT
Group:          System Environment/Libraries
URL:            http://pixman.org/
Source0:        http://xorg.freedesktop.org/releases/individual/lib/%{gnuxc_name}-%{version}.tar.bz2

BuildRequires:  gnuxc-libpng-devel

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       gnuxc-libpng-devel

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

%build
%gnuxc_configure \
    --disable-silent-rules \
    --enable-libpng
%gnuxc_make %{?_smp_mflags} all

%install
%gnuxc_make_install

# We don't need libtool's help.
rm -f %{buildroot}%{gnuxc_libdir}/libpixman-1.la


%files
%{gnuxc_libdir}/libpixman-1.so.0
%{gnuxc_libdir}/libpixman-1.so.%{version}
%doc AUTHORS ChangeLog COPYING NEWS README

%files devel
%{gnuxc_includedir}/pixman-1
%{gnuxc_libdir}/libpixman-1.so
%{gnuxc_libdir}/pkgconfig/pixman-1.pc

%files static
%{gnuxc_libdir}/libpixman-1.a


%changelog
