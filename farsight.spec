#
Summary:	Farsight library
Name:		farsight
Version:	0.1.28
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://farsight.freedesktop.org/releases/farsight/%{name}-%{version}.tar.gz
# Source0-md5:	6439b749ecf83bb956a6c88a7843343e
URL:		http://farsight.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	check >= 0.9.4
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnet-devel
BuildRequires:	gstreamer-devel >= 0.10.13
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libtool
BuildRequires:	libjingle-devel >= 0.3.11
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for farsight library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki farsight
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for farsight library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki farsight.

%package static
Summary:	Static farsight library
Summary(pl.UTF-8):	Statyczna biblioteka farsight
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static farsight library.

%description static -l pl.UTF-8
Statyczna biblioteka farsight.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/farsight-0.1-3/lib*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/farsight-0.1-3/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libfarsight-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfarsight-0.1.so.3
%dir %{_sysconfdir}/farsight
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/farsight/*.conf
%dir %{_libdir}/farsight-0.1-3
%attr(755,root,root) %{_libdir}/farsight-0.1-3/lib*.so

%files devel
%attr(755,root,root) %{_libdir}/libfarsight-0.1.so
%{_libdir}/libfarsight-0.1.la
%{_includedir}/farsight-0.1
%{_pkgconfigdir}/farsight-0.1.pc

%files static
%{_libdir}/libfarsight-0.1.a
