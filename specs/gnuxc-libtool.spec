%?gnuxc_package_header

Name:           gnuxc-libtool
Version:        2.4.4
Release:        1%{?dist}
Summary:        Cross-compiled version of %{gnuxc_name} for the GNU system

License:        GPLv2+ and LGPLv2+ and GFDL
Group:          Development/Tools
URL:            http://www.gnu.org/software/libtool/
Source0:        http://ftpmirror.gnu.org/libtool/%{gnuxc_name}-%{version}.tar.xz

BuildRequires:  gnuxc-glibc-devel

%description
%{summary}.

%package -n gnuxc-ltdl
Summary:        Cross-compiled version of libltdl for the GNU system
License:        LGPLv2+
Group:          System Environment/Libraries

%description -n gnuxc-ltdl
Cross-compiled version of libltdl for the GNU system.

%package -n gnuxc-ltdl-devel
Summary:        Development files for gnuxc-ltdl
License:        LGPLv2+
Group:          Development/Libraries
Requires:       gnuxc-ltdl = %{version}-%{release}
Requires:       gnuxc-glibc-devel

%description -n gnuxc-ltdl-devel
The gnuxc-ltdl-devel package contains libraries and header files for developing
applications that use libltdl on GNU systems.

%package -n gnuxc-ltdl-static
Summary:        Static libraries of gnuxc-ltdl
License:        LGPLv2+
Group:          Development/Libraries
Requires:       gnuxc-ltdl-devel = %{version}-%{release}

%description -n gnuxc-ltdl-static
The gnuxc-ltdl-static package contains the libltdl static libraries for -static
linking on GNU systems.  You don't need these, unless you link statically,
which is highly discouraged.


%prep
%setup -q -n %{gnuxc_name}-%{version}

%build
%gnuxc_configure \
    --disable-silent-rules \
    --enable-ltdl-install
%gnuxc_make %{?_smp_mflags} all

%install
%gnuxc_make_install

# We don't need libtool's help.
rm -f %{buildroot}%{gnuxc_libdir}/libltdl.la

# This functionality should be used from the system package.
rm -rf \
    %{buildroot}%{gnuxc_bindir}/{libtool,libtoolize} \
    %{buildroot}%{gnuxc_datadir}/{aclocal,libtool}

# Skip the documentation.
rm -rf %{buildroot}%{gnuxc_infodir} %{buildroot}%{gnuxc_mandir}


%files -n gnuxc-ltdl
%{gnuxc_libdir}/libltdl.so.7
%{gnuxc_libdir}/libltdl.so.7.3.1
%doc AUTHORS ChangeLog* COPYING NEWS README THANKS TODO

%files -n gnuxc-ltdl-devel
%{gnuxc_includedir}/libltdl
%{gnuxc_includedir}/ltdl.h
%{gnuxc_libdir}/libltdl.so

%files -n gnuxc-ltdl-static
%{gnuxc_libdir}/libltdl.a


%changelog
