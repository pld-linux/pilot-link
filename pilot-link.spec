Summary:	File transfer utilities between Linux and PalmPilots
Summary(es):	Bibliotecas estáticas necesarias para generar aplicaciones Pilot
Summary(pl):	Narzêdzia do przesy³ania plików miêdzy Linuksem a PalmPilotami
Summary(pt_BR):	Utilitários de transferência de dados entre Unix e o Pilot
Name:		pilot-link
Version:	0.10.99
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.pilot-link.org/source/%{name}-%{version}.tar.gz
URL:		http://www.pilot-link.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	readline-devel >= 4.2
BuildRequires:	perl-devel >= 5.6
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
Bibliotecas estáticas necesarias para generar aplicaciones Pilot.

%description -l pl
Ten zestaw narzêdzi pozwala na przesy³anie programów i plików z danymi
pomiêdzy maszyn± linuksow±/uniksow± a PalmPilotem. Ma kilka
dodatkowych narzêdzi pozwalaj±cych na synchronizacjê kalendarza
PalmPilota z programem Ical. Aby u¿ywaæ interfejsu do Pythona, Tcl lub
Perla, mo¿e byæ potrzeba zajrzenia do ¼róde³ pilot-linka.

Obecna wersja dzia³a równie¿ z urz±dzeniami z PalmOS wyposa¿onymi
w port USB (Sony CLIE, Palm m5xx, Handspring Visor).

%description -l pt_BR
Este conjunto de ferramentas permite transferir programas e dados
entre máquinas
- *nix e o Palm Pilot. Alguns utilitários extras permitem coisas como
  sincronizar dados entre o calendário do Pilot e o Ical.

%package devel
Summary:	Pilot development header files
Summary(es):	Archivos de inclusión para el desarrollo de programas
Summary(pl):	Pliki nag³ówkowe do biblioteki pilot-link
Summary(pt_BR):	Arquivos de inclusão para o desenvolvimento de programas
Group:		Development/Libraries
Requires:	%{name} = %{version}

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

%package static
Summary:	Pilot link static libraries
Summary(es):	Bibliotecas estáticas necesarias para crear aplicaciones Pilot
Summary(pl):	Statyczne biblioteki pilot-link
Summary(pt_BR):	Bibliotecas estáticas necessárias para gerar aplicações Pilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

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

%prep
%setup -q

%build
%{__libtoolize}
aclocal
chmod +w configure
%{__autoconf}

CFLAGS="%{rpmcflags} -I%{_prefix}/X11R6/include"
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure

%{__make} LIBDIR="%{_datadir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README*
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
