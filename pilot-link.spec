Summary:	File transfer utilities between Linux and PalmPilots
Summary(es):	Bibliotecas estАticas necesarias para generar aplicaciones Pilot
Summary(pl):	NarzЙdzia do przesyЁania plikСw miЙdzy Linuksem a PalmPilotami
Summary(pt_BR):	UtilitАrios de transferЙncia de dados entre Unix e o Pilot
Summary(ru):	Утилита пересылки файлов между Linux и PalmPilot
Summary(uk):	Утил╕та пересилки файл╕в м╕ж Linux та PalmPilot
Name:		pilot-link
Version:	0.11.7
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.pilot-link.org/source/%{name}-%{version}.tar.gz
URL:		http://www.pilot-link.org/
Patch0:		%{name}-configure.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	perl-devel >= 5.6
BuildRequires:	python-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tk-devel >= 8.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Bibliotecas estАticas necesarias para generar aplicaciones Pilot.

%description -l pl
Ten zestaw narzЙdzi pozwala na przesyЁanie programСw i plikСw z danymi
pomiЙdzy maszyn╠ linuksow╠/uniksow╠ a PalmPilotem. Ma kilka
dodatkowych narzЙdzi pozwalaj╠cych na synchronizacjЙ kalendarza
PalmPilota z programem Ical. Aby u©ywaФ interfejsu do Pythona, Tcl lub
Perla, mo©e byФ potrzeba zajrzenia do ╪rСdeЁ pilot-linka.

Obecna wersja dziaЁa rСwnie© z urz╠dzeniami z PalmOS wyposa©onymi w
port USB (Sony CLIE, Palm m5xx, Handspring Visor).

%description -l pt_BR
Este conjunto de ferramentas permite transferir programas e dados
entre mАquinas *nix e o Palm Pilot. Alguns utilitАrios extras permitem
coisas como sincronizar dados entre o calendАrio do Pilot e o Ical.

%description -l uk
Цей наб╕р ╕нструмент╕в дозволя╓ вам переносити програми та файли даних
м╕ж системами Linux та PalmPilot. В╕н ма╓ також к╕лька додаткових
утил╕т, як╕ забезпечують так╕ реч╕ як синхронизац╕я календаря
PalmPilot та Ical.

%description -l ru
Этот набор инструментов позволяет вам переносить программы и файлы
данных между системами Linux и PalmPilot. Он имеет также несколько
дополнительных утилит, обеспечивающих такие вещи как синхронизация
календаря PalmPilot и Ical.

%package devel
Summary:	Pilot development header files
Summary(es):	Archivos de inclusiСn para el desarrollo de programas
Summary(pl):	Pliki nagЁСwkowe do biblioteki pilot-link
Summary(pt_BR):	Arquivos de inclusЦo para o desenvolvimento de programas
Summary(ru):	Файлы для разработки программ взаимодействия с PalmPilot
Summary(uk):	Файли для розробки програм вза╓мод╕╖ з PalmPilot
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the development headers that are used to build
the pilot-link package.

%description devel -l es
Este paquete contiene los archivos de inclusiСn necesarios para crear
aplicaciones Pilot.

%description devel -l pl
Ten pakiet zawiera pliki nagЁСwkowe u©ywane przy budowaniu pakietu
pilot-link.

%description devel -l pt_BR
Este pacote contИm os arquivos de inclusЦo necessАrios para gerar
aplicaГУes Pilot.

%description devel -l ru
Этот пакет содержит файлы заголовков C для построения программ
взаимодействия с PalmPilot.

%description devel -l uk
Цей пакет м╕стить файли заголовк╕в C для побудови програм вза╓мод╕╖ з
PalmPilot.

%package static
Summary:	Pilot link static libraries
Summary(es):	Bibliotecas estАticas necesarias para crear aplicaciones Pilot
Summary(pl):	Statyczne biblioteki pilot-link
Summary(pt_BR):	Bibliotecas estАticas necessАrias para gerar aplicaГУes Pilot
Summary(ru):	Статические библиотеки для разработки программ взаимодействия с PalmPilot
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм вза╓мод╕╖ з PalmPilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Pilot link static libraries.

%description static -l es
Este paquete contiene las bibliotecas estАticas necesarias para crear
aplicaciones Pilot.

%description static -l pl
Statyczne biblioteki pilot-link.

%description static -l pt_BR
Este pacote contИm as bibliotecas estАticas necessАrias para gerar
aplicaГУes Pilot.

%description static -l ru
Этот пакет содержит статические библиотеки для построения программ
взаимодействия с PalmPilot.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки для побудови програм вза╓мод╕╖ з
PalmPilot.

%prep
%setup -q
# %patch0 -p1

%build
#rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

CFLAGS="%{rpmcflags} -I%{_prefix}/X11R6/include"
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure

%{__make} LIBDIR="%{_datadir}" SED=/bin/sed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT SED=/bin/sed

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README* doc/README.usb doc/README.debugging NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pilot-link
%{_mandir}/man[17]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
