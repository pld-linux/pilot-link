Summary:	File transfer utilities between Linux and PalmPilots
Name:		pilot-link
Version:	0.9.3
Release:	11
License:	GPL/LGPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ryeham.ee.ryerson.ca/pub/PalmOS/%{name}.%{version}.tar.gz
Patch0:		%{name}-perl-install.patch
Patch1:		%{name}.perl.patch
Patch2:		%{name}-pixdir.patch
Patch3:		%{name}.sync-ldif.patch
Patch4:		%{name}-DESTDIR.patch
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This suite of tools allows you to upload and download programs and
data files between a Linux/UNIX machine and the PalmPilot. It has a
few extra utils that will allow for things like syncing the
PalmPilot's calendar app with Ical. Note that you might still need to
consult the sources for pilot-link if you would like the Python, Tcl,
or Perl bindings.

%package devel
Summary:	Pilot development header files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains the development headers that are used to build
the pilot-link package. It also includes the static libraries
necessary to build static pilot apps.

%package static
Summary:	Pilot link static libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Pilot link static libraries.

%prep 
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
chmod +w configure
autoconf
%ifarch armv4l
libtoolize --copy --force
%endif

CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -I/usr/X11R6/include"
CXXFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure

%{__make} LIBDIR="%{_datadir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/pilot-link $RPM_BUILD_ROOT%{_datadir}

gzip -9nf ChangeLog README*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pilot-link
%{_mandir}/man[17]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
