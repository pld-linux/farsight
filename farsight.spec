#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static library

Summary:	FarSight - universal audio/video conference tool for Instant Messengers
Summary(pl.UTF-8):	FarSight - uniwersalne narzędzie do konferencji audio/video dla komunikatorów
Name:		farsight
Version:	0.1.28
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/farstream/releases/obsolete/farsight/%{name}-%{version}.tar.gz
# Source0-md5:	6439b749ecf83bb956a6c88a7843343e
Patch0:		%{name}-am.patch
URL:		https://www.freedesktop.org/wiki/Software/Farstream/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	check-devel >= 0.9.4
BuildRequires:	clinkc-devel
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnet-devel
BuildRequires:	gstreamer0.10-devel >= 0.10.13
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.13
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libtool
BuildRequires:	libjingle-devel >= 0.3.11
BuildRequires:	pkgconfig
%if %{with apidocs}
BuildRequires:	ImageMagick
BuildRequires:	ghostscript
# pic2plot
BuildRequires:	plotutils
%endif
Requires:	glib2 >= 1:2.6.0
Requires:	gstreamer0.10 >= 0.10.13
Requires:	gstreamer0.10-plugins-base >= 0.10.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Farsight is a library to allow you to easily setup network media
streaming, with various forms of NAT traversal. It has support for
protocol plugins.

%description -l pl.UTF-8
Farsight to biblioteka pozwalająca na łatwe rozpoczęcie przesyłania
strumieni multimedialnych z różnymi formami przechodzenia NAT. Ma
obsługę wtyczek protokołów.

%package devel
Summary:	Header files for farsight library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki farsight
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.6.0
Requires:	gstreamer0.10-devel >= 0.10.13

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# plugins
%{__rm} $RPM_BUILD_ROOT%{_libdir}/farsight-0.1-3/lib*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/farsight-0.1-3/lib*.a
%endif
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfarsight-0.1.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libfarsight-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfarsight-0.1.so.3
%dir %{_sysconfdir}/farsight
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/farsight/*.conf
%dir %{_libdir}/farsight-0.1-3
%attr(755,root,root) %{_libdir}/farsight-0.1-3/lib*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfarsight-0.1.so
%{_includedir}/farsight-0.1
%{_pkgconfigdir}/farsight-0.1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfarsight-0.1.a
%endif
