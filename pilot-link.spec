Summary:	Pilot Link - USR Pilot to Unix transfer utilities.
Name:		pilot-link
Version:	0.9.3
Release:	1
Copyright:	GPL/LGPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		ftp://ryeham.ee.ryerson.ca/pub/PalmOS/%{name}.%{version}.tar.gz 
Patch0:		pilot-link-perl-install.patch
Patch1:		pilot-link.perl.patch
Patch2:		pilot-link-pixdir.patch
Patch3:		pilot-link.sync-ldif.patch
BuildPrereq:	libstdc++-devel
BuildPrereq:	ncurses-devel
BuildPrereq:	readline-devel
BuildPrereq:	tcl-devel
BuildPrereq:	tk-devel
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This suite of tools allows you to upload and download programs
and data files between a *nix machine and the USR Pilot.  It has
a few extra utils that will allow for things like syncing the
Pilot's calendar app with Ical.  Note that you might still need
to consult the sources for pilot-link if you would like the
Python, Tcl, or Perl bindings.

%package devel
Summary:	Pilot development header files
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains the development headers that are used
to build the pilot-link package.  It also includes the static
libraries necessary to build static pilot apps.

%package static
Summary:	Pilot link static libraries
Group:		Development/Libraries
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

%build
chmod +w configure
autoconf
%ifarch armv4l
libtoolize --copy --force
%endif

CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include" \
LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates" \
./configure \
	--prefix=%{_prefix} \
	--target=%{_target_platform} \
	--host=%{_host}

make LIBDIR="%{_datadir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

mv $RPM_BUILD_ROOT%{_libdir}/pilot-link $RPM_BUILD_ROOT%{_datadir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	ChangeLog README*

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
