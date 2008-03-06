#
Summary:	Farsight library
Name:		farsight
Version:	0.1.25
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0: http://farsight.freedesktop.org/releases/farsight/farsight-0.1.25.tar.gz
# Source0-md5:	3023e5013e612c7debc5763e14c78123
URL:		http://farsight.freedesktop.org/
BuildRequires:	glib2-devel
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
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
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
%{__aclocal}
%{__autoconf}
#%%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
