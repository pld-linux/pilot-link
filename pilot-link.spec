Summary:	File transfer utilities between Linux and PalmPilots
Name:		pilot-link
Version:	0.9.5
Release:	4
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ryeham.ee.ryerson.ca/pub/PalmOS/%{name}-%{version}.tar.bz2
Patch0:		%{name}-pixdir.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-misc.patch
Patch3:		%{name}-ack.patch
URL:		http://www.gnu-designs.com/pilot-link/
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tk-devel >= 8.3.2
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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
libtoolize --copy --force
chmod +w configure
autoconf

CFLAGS="%{rpmcflags} -I/usr/X11R6/include"
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"
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
