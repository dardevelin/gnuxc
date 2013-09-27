%?gnuxc_package_header
%undefine debug_package

Name:           gnuxc-videoproto
Version:        2.3.2
Release:        1%{?dist}
Summary:        Cross-compiled version of %{gnuxc_name} for the GNU system

License:        MIT
Group:          Development/System
URL:            http://www.x.org/
Source0:        http://xorg.freedesktop.org/releases/individual/proto/%{gnuxc_name}-%{version}.tar.bz2

Requires:       gnuxc-xextproto

BuildArch:      noarch

%description
%{summary}.


%prep
%setup -q -n %{gnuxc_name}-%{version}

%build
%gnuxc_configure \
    --enable-strict-compilation
%gnuxc_make %{?_smp_mflags} all

%install
%gnuxc_make_install

# Skip the documentation.
rm -rf %{buildroot}%{gnuxc_docdir}


%files
%{gnuxc_includedir}/X11/extensions/vldXvMC.h
%{gnuxc_includedir}/X11/extensions/Xv.h
%{gnuxc_includedir}/X11/extensions/XvMC.h
%{gnuxc_includedir}/X11/extensions/XvMCproto.h
%{gnuxc_includedir}/X11/extensions/Xvproto.h
%{gnuxc_libdir}/pkgconfig/videoproto.pc
%doc ChangeLog COPYING README


%changelog