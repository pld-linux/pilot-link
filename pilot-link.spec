Summary:     Pilot Link - USR Pilot to Unix transfer utilities
Name:        pilot-link
Version:     0.8.13
Release:     2
Copyright:   GPL
Group:       Utilities/System
Source:      ftp://ryeham.ee.ryerson.ca/pub/PalmOS/%{name}.%{version}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

%description
This suite of tools allows you to upload and download programs and data
files between a *nix machine and the USR Pilot.  It has a few extra utils
that will allow for things like syncing the Pilot's calendar app with Ical. 
Note that you might still need to consult the sources for pilot-link if you
would like the Python, Tcl, or Perl bindings.

%package devel
Summary:     Pilot Development Headers
Group:       Development/Building
Requires:    %{name} = %{version}

%description devel
This package contains the development headers that are used to build the
pilot-link package.

%package static
Summary:     Pilot static libraries
Group:       Development/Building
Requires:    %{name}-devel = %{version}

%description static
Static libraries necessary to build static pilot apps.

%prep 
%setup -q -n %{name}.%{version}
%patch0 -p1 -b .install
%patch1 -p1 -b .perl
#%patch2 -p1 -b .more-perl

%build
CFLAGS="$RPM_OPT_FLAGS" CXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--without-perl5

%install
rm -fr $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

gzip -9nf $RPM_BUILD_ROOT/usr/man/man{1,7}/*
strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644, roo, root, 755)
%doc ChangeLog README
/usr/lib/lib*.so.*.*
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man[17]/*
/usr/lib/pix

%files devel
%defattr(644, roo, root, 755)
/usr/lib/libpisock.so
/usr/include/*

%files static
%attr(644, roo, root) /usr/lib/lib*.a

%changelog
* Fri Dec  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.8.13-2]
- added -q %setup parameter,
- added gzipping man pages,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- fixed %post{un},
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added striping shared libraries,
- removed perl stuff (now is buggy),
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Tue May 19 1998 Michael Maher <mike@redhat.com>
- updated rpm

* Thu Jan 29 1998 Otto Hammersmith <otto@redhat.com>
- added changelog
- updated to 0.8.9
- removed explicit requires for /usr/bin/perl
