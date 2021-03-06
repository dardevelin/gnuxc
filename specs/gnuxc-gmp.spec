%?gnuxc_package_header

Name:           gnuxc-gmp
Version:        6.0.0a
%global basever 6.0.0
Release:        1%{?dist}
Summary:        Cross-compiled version of %{gnuxc_name} for the GNU system

License:        LGPLv3+
Group:          System Environment/Libraries
URL:            http://www.gnu.org/software/gmp/
Source0:        http://ftpmirror.gnu.org/%{gnuxc_name}/%{gnuxc_name}-%{version}.tar.lz

BuildRequires:  gnuxc-gcc-c++

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       gnuxc-gcc-c++

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
%setup -q -n %{gnuxc_name}-%{basever}

# Seriously disable rpaths.
sed -i -e 's/\(need_relink\)=yes/\1=no/' ltmain.sh
sed -i -e 's/\(hardcode_into_libs\)=yes/\1=no/' configure
sed -i -e 's/\(hardcode_libdir_flag_spec[A-Za-z_]*\)=.*/\1=-D__LIBTOOL_NEUTERED__/' configure

%build
%gnuxc_configure \
    --enable-assembly \
    --enable-assert \
    --enable-cxx \
    --enable-fft
%gnuxc_make %{?_smp_mflags} all

%install
%gnuxc_make_install

# We don't need libtool's help.
rm -f %{buildroot}%{gnuxc_libdir}/libgmp{,xx}.la

# Skip the documentation.
rm -rf %{buildroot}%{gnuxc_infodir}


%files
%{gnuxc_libdir}/libgmp.so.10
%{gnuxc_libdir}/libgmp.so.10.2.0
%{gnuxc_libdir}/libgmpxx.so.4
%{gnuxc_libdir}/libgmpxx.so.4.4.0
%doc AUTHORS ChangeLog COPYING* NEWS README

%files devel
%{gnuxc_includedir}/gmp.h
%{gnuxc_includedir}/gmpxx.h
%{gnuxc_libdir}/libgmp.so
%{gnuxc_libdir}/libgmpxx.so

%files static
%{gnuxc_libdir}/libgmp.a
%{gnuxc_libdir}/libgmpxx.a


%changelog
