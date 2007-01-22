# TODO:
# - perl/python/tcl bindings subpackages
#
# Conditional build:
%bcond_with	tcl	# Tcl/Tk bindings
#
Summary:	File transfer utilities between Linux and PalmPilots
Summary(es):	Bibliotecas estáticas necesarias para generar aplicaciones Pilot
Summary(pl):	Narzêdzia do przesy³ania plików miêdzy Linuksem a PalmPilotami
Summary(pt_BR):	Utilitários de transferência de dados entre Unix e o Pilot
Summary(ru):	õÔÉÌÉÔÁ ÐÅÒÅÓÙÌËÉ ÆÁÊÌÏ× ÍÅÖÄÕ Linux É PalmPilot
Summary(uk):	õÔÉÌ¦ÔÁ ÐÅÒÅÓÉÌËÉ ÆÁÊÌ¦× Í¦Ö Linux ÔÁ PalmPilot
Name:		pilot-link
Version:	0.12.1
Release:	1
License:	GPL
Group:		Applications/Communications
# http://downloads.pilot-link.org/%{name}-%{version}.tar.bz2
# unfortunately forbids wget as User-Agent (used by our distfiles)
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	80579c6f68eb583f54294d5651c4632b
Patch0:		%{name}-ac.patch
URL:		http://www.pilot-link.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRequires:	readline-devel >= 5.0
%if %{with tcl}
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tk-devel >= 8.3.2
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
This suite of tools allows you to upload and download programs and
data files between a Linux/UNIX machine and the PalmPilot. It has a
few extra utils that will allow for things like syncing the
PalmPilot's calendar app with Ical. Note that you might still need to
consult the sources for pilot-link if you would like the Python, Tcl,
or Perl bindings.

Now also with support for USB PalmOS devices (Sony CLIE, Palm m5xx,
Handspring Visor).

%description -l es
Bibliotecas estáticas necesarias para generar aplicaciones Pilot.

%description -l pl
Ten zestaw narzêdzi pozwala na przesy³anie programów i plików z danymi
pomiêdzy maszyn± linuksow±/uniksow± a PalmPilotem. Ma kilka
dodatkowych narzêdzi pozwalaj±cych na synchronizacjê kalendarza
PalmPilota z programem Ical. Aby u¿ywaæ interfejsu do Pythona, Tcl lub
Perla, mo¿e byæ potrzeba zajrzenia do ¼róde³ pilot-linka.

Obecna wersja dzia³a równie¿ z urz±dzeniami z PalmOS wyposa¿onymi w
port USB (Sony CLIE, Palm m5xx, Handspring Visor).

%description -l pt_BR
Este conjunto de ferramentas permite transferir programas e dados
entre máquinas *nix e o Palm Pilot. Alguns utilitários extras permitem
coisas como sincronizar dados entre o calendário do Pilot e o Ical.

%description -l uk
ãÅÊ ÎÁÂ¦Ò ¦ÎÓÔÒÕÍÅÎÔ¦× ÄÏÚ×ÏÌÑ¤ ×ÁÍ ÐÅÒÅÎÏÓÉÔÉ ÐÒÏÇÒÁÍÉ ÔÁ ÆÁÊÌÉ ÄÁÎÉÈ
Í¦Ö ÓÉÓÔÅÍÁÍÉ Linux ÔÁ PalmPilot. ÷¦Î ÍÁ¤ ÔÁËÏÖ Ë¦ÌØËÁ ÄÏÄÁÔËÏ×ÉÈ
ÕÔÉÌ¦Ô, ÑË¦ ÚÁÂÅÚÐÅÞÕÀÔØ ÔÁË¦ ÒÅÞ¦ ÑË ÓÉÎÈÒÏÎÉÚÁÃ¦Ñ ËÁÌÅÎÄÁÒÑ
PalmPilot ÔÁ Ical.

%description -l ru
üÔÏÔ ÎÁÂÏÒ ÉÎÓÔÒÕÍÅÎÔÏ× ÐÏÚ×ÏÌÑÅÔ ×ÁÍ ÐÅÒÅÎÏÓÉÔØ ÐÒÏÇÒÁÍÍÙ É ÆÁÊÌÙ
ÄÁÎÎÙÈ ÍÅÖÄÕ ÓÉÓÔÅÍÁÍÉ Linux É PalmPilot. ïÎ ÉÍÅÅÔ ÔÁËÖÅ ÎÅÓËÏÌØËÏ
ÄÏÐÏÌÎÉÔÅÌØÎÙÈ ÕÔÉÌÉÔ, ÏÂÅÓÐÅÞÉ×ÁÀÝÉÈ ÔÁËÉÅ ×ÅÝÉ ËÁË ÓÉÎÈÒÏÎÉÚÁÃÉÑ
ËÁÌÅÎÄÁÒÑ PalmPilot É Ical.

%package devel
Summary:	Pilot development header files
Summary(es):	Archivos de inclusión para el desarrollo de programas
Summary(pl):	Pliki nag³ówkowe do biblioteki pilot-link
Summary(pt_BR):	Arquivos de inclusão para o desenvolvimento de programas
Summary(ru):	æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ ×ÚÁÉÍÏÄÅÊÓÔ×ÉÑ Ó PalmPilot
Summary(uk):	æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ ×ÚÁ¤ÍÏÄ¦§ Ú PalmPilot
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development headers that are used to build
the pilot-link package.

%description devel -l es
Este paquete contiene los archivos de inclusión necesarios para crear
aplicaciones Pilot.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe u¿ywane przy budowaniu pakietu
pilot-link.

%description devel -l pt_BR
Este pacote contém os arquivos de inclusão necessários para gerar
aplicações Pilot.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× C ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÐÒÏÇÒÁÍÍ
×ÚÁÉÍÏÄÅÊÓÔ×ÉÑ Ó PalmPilot.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÆÁÊÌÉ ÚÁÇÏÌÏ×Ë¦× C ÄÌÑ ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ ×ÚÁ¤ÍÏÄ¦§ Ú
PalmPilot.

%package static
Summary:	Pilot link static libraries
Summary(es):	Bibliotecas estáticas necesarias para crear aplicaciones Pilot
Summary(pl):	Statyczne biblioteki pilot-link
Summary(pt_BR):	Bibliotecas estáticas necessárias para gerar aplicações Pilot
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ ×ÚÁÉÍÏÄÅÊÓÔ×ÉÑ Ó PalmPilot
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ ×ÚÁ¤ÍÏÄ¦§ Ú PalmPilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Pilot link static libraries.

%description static -l es
Este paquete contiene las bibliotecas estáticas necesarias para crear
aplicaciones Pilot.

%description static -l pl
Statyczne biblioteki pilot-link.

%description static -l pt_BR
Este pacote contém as bibliotecas estáticas necessárias para gerar
aplicações Pilot.

%description static -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÐÒÏÇÒÁÍÍ
×ÚÁÉÍÏÄÅÊÓÔ×ÉÑ Ó PalmPilot.

%description static -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ ×ÚÁ¤ÍÏÄ¦§ Ú
PalmPilot.

%prep
%setup -q
%patch0 -p1

%if "%{_lib}" == "lib64"
sed -i -e 's#/lib #/lib64 #g' -e 's#/lib/#/lib64/#g' m4/python.m4
%endif

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	%{!?debug:--disable-debug} \
	--enable-conduits \
	--enable-threads \
	--enable-libusb \
	--with-libpng=%{_prefix} \
	--without-included-popt \
	--with-perl \
	%{!?with_tcl:--without-tcl}%{?with_tcl:--with-tcl=%{_ulibdir}} \
	--with-python


# perl part fails with -jN > 1
%{__make} -j1 \
	LIBDIR="%{_datadir}"

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
%doc ChangeLog README* doc/README.usb doc/README.debugging NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/pilot-link
%{_mandir}/man[17]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
