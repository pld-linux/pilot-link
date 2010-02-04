# TODO:
# - perl/python/tcl bindings subpackages
#
# Conditional build:
%bcond_with	tcl	# Tcl/Tk bindings
#
Summary:	File transfer utilities between Linux and PalmPilots
Summary(es.UTF-8):	Bibliotecas estáticas necesarias para generar aplicaciones Pilot
Summary(pl.UTF-8):	Narzędzia do przesyłania plików między Linuksem a PalmPilotami
Summary(pt_BR.UTF-8):	Utilitários de transferência de dados entre Unix e o Pilot
Summary(ru.UTF-8):	Утилита пересылки файлов между Linux и PalmPilot
Summary(uk.UTF-8):	Утиліта пересилки файлів між Linux та PalmPilot
Name:		pilot-link
Version:	0.12.4
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://downloads.pilot-link.org/%{name}-%{version}.tar.bz2
# Source0-md5:	a62baf6fd709c6a3d93077abda936e7a
Patch0:		%{name}-ac.patch
Patch1:		%{name}-open.patch
Patch2:		%{name}-man.patch
Patch3:		%{name}-libpng.patch
URL:		http://www.pilot-link.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bluez-libs-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libusb-compat-devel
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
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

%description -l es.UTF-8
Bibliotecas estáticas necesarias para generar aplicaciones Pilot.

%description -l pl.UTF-8
Ten zestaw narzędzi pozwala na przesyłanie programów i plików z danymi
pomiędzy maszyną linuksową/uniksową a PalmPilotem. Ma kilka
dodatkowych narzędzi pozwalających na synchronizację kalendarza
PalmPilota z programem Ical. Aby używać interfejsu do Pythona, Tcl lub
Perla, może zaistnieć potrzeba zajrzenia do źródeł pilot-linka.

Obecna wersja działa również z urządzeniami z PalmOS wyposażonymi w
port USB (Sony CLIE, Palm m5xx, Handspring Visor).

%description -l pt_BR.UTF-8
Este conjunto de ferramentas permite transferir programas e dados
entre máquinas *nix e o Palm Pilot. Alguns utilitários extras permitem
coisas como sincronizar dados entre o calendário do Pilot e o Ical.

%description -l uk.UTF-8
Цей набір інструментів дозволяє вам переносити програми та файли даних
між системами Linux та PalmPilot. Він має також кілька додаткових
утиліт, які забезпечують такі речі як синхронизація календаря
PalmPilot та Ical.

%description -l ru.UTF-8
Этот набор инструментов позволяет вам переносить программы и файлы
данных между системами Linux и PalmPilot. Он имеет также несколько
дополнительных утилит, обеспечивающих такие вещи как синхронизация
календаря PalmPilot и Ical.

%package devel
Summary:	Pilot development header files
Summary(es.UTF-8):	Archivos de inclusión para el desarrollo de programas
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki pilot-link
Summary(pt_BR.UTF-8):	Arquivos de inclusão para o desenvolvimento de programas
Summary(ru.UTF-8):	Файлы для разработки программ взаимодействия с PalmPilot
Summary(uk.UTF-8):	Файли для розробки програм взаємодії з PalmPilot
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development headers that are used to build
the pilot-link package.

%description devel -l es.UTF-8
Este paquete contiene los archivos de inclusión necesarios para crear
aplicaciones Pilot.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe używane przy budowaniu pakietu
pilot-link.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão necessários para gerar
aplicações Pilot.

%description devel -l ru.UTF-8
Этот пакет содержит файлы заголовков C для построения программ
взаимодействия с PalmPilot.

%description devel -l uk.UTF-8
Цей пакет містить файли заголовків C для побудови програм взаємодії з
PalmPilot.

%package static
Summary:	Pilot link static libraries
Summary(es.UTF-8):	Bibliotecas estáticas necesarias para crear aplicaciones Pilot
Summary(pl.UTF-8):	Statyczne biblioteki pilot-link
Summary(pt_BR.UTF-8):	Bibliotecas estáticas necessárias para gerar aplicações Pilot
Summary(ru.UTF-8):	Статические библиотеки для разработки программ взаимодействия с PalmPilot
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм взаємодії з PalmPilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Pilot link static libraries.

%description static -l es.UTF-8
Este paquete contiene las bibliotecas estáticas necesarias para crear
aplicaciones Pilot.

%description static -l pl.UTF-8
Statyczne biblioteki pilot-link.

%description static -l pt_BR.UTF-8
Este pacote contém as bibliotecas estáticas necessárias para gerar
aplicações Pilot.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для построения программ
взаимодействия с PalmPilot.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки для побудови програм взаємодії з
PalmPilot.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%if "%{_lib}" == "lib64"
%{__sed} -i -e 's#/lib #/lib64 #g' -e 's#/lib/#/lib64/#g' m4/python.m4
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
	--with-bluez \
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
%attr(755,root,root) %ghost %{_libdir}/libpisock.so.9
%attr(755,root,root) %ghost %{_libdir}/libpisync.so.1
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
