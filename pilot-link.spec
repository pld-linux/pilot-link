Summary:	Pilot Link - USR Pilot to Unix transfer utilities.
Name:		pilot-link
Version:	0.9.2
Release:	2
Copyright:	GPL/LGPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		ftp://ryeham.ee.ryerson.ca/pub/PalmOS/%{name}.%{version}.tar.gz 
Patch0:		pilot-link-perl-install.patch
Patch1:		pilot-link.perl.patch
Patch2:		pilot-link-pixdir.patch
Patch3:		ftp://ryeham.ee.ryerson.ca/pub/PalmOS/pilot-link.sync-ldif.patch
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
autoconf
%ifarch armv4l
libtoolize --copy --force
%endif

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates" \
./configure %{_target} \
	--prefix=/usr

make LIBDIR="/usr/share"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share

make install \
	prefix=$RPM_BUILD_ROOT/usr

mv $RPM_BUILD_ROOT/usr/lib/pilot-link $RPM_BUILD_ROOT/usr/share

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man*/* \
	ChangeLog README*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/lib/lib*.so.*.*
%attr(755,root,root) /usr/bin/*
/usr/share/pilot-link
/usr/share/man/man[17]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so
/usr/include/*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.2-2]
- now package is FHS 2.0 compiliat.

* Mon Apr 26 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.2-1]
- added "-fno-rtti -fno-exceptions -fno-implicit-templates" c++ optimization
  options,
- added patch with sync-ldif (application which sync the PalmPilot address
  book with a Netscape Communicator address book LDIF file,
- addded gzipping man pages and %doc,
- /sbin/ldconfig now is runed as -p parameter in %post, %postun,
- added Group(pl),
- added "BuildPrereq: glibc-devel".

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- added missing files from devel subpackage

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- move /usr/lib/pix to /usr/lib/pilot-link (dumb, BAD name)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Thu Jan 21 1999 Bill Nottingham <notting@redhat.com>
- arm fix

* Fri Sep 24 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file, updated package

* Tue May 19 1998 Michael Maher <mike@redhat.com>
- updated rpm

* Thu Jan 29 1998 Otto Hammersmith <otto@redhat.com>
- added changelog
- updated to 0.8.9
- removed explicit requires for /usr/bin/perl
