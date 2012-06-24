Summary:	File transfer utilities between Linux and PalmPilots
Summary(es):	Bibliotecas est�ticas necesarias para generar aplicaciones Pilot
Summary(pl):	Narz�dzia do przesy�ania plik�w mi�dzy Linuksem a PalmPilotami
Summary(pt_BR):	Utilit�rios de transfer�ncia de dados entre Unix e o Pilot
Summary(ru):	������� ��������� ������ ����� Linux � PalmPilot
Summary(uk):	���̦�� ��������� ���̦� ͦ� Linux �� PalmPilot
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
Bibliotecas est�ticas necesarias para generar aplicaciones Pilot.

%description -l pl
Ten zestaw narz�dzi pozwala na przesy�anie program�w i plik�w z danymi
pomi�dzy maszyn� linuksow�/uniksow� a PalmPilotem. Ma kilka
dodatkowych narz�dzi pozwalaj�cych na synchronizacj� kalendarza
PalmPilota z programem Ical. Aby u�ywa� interfejsu do Pythona, Tcl lub
Perla, mo�e by� potrzeba zajrzenia do �r�de� pilot-linka.

Obecna wersja dzia�a r�wnie� z urz�dzeniami z PalmOS wyposa�onymi w
port USB (Sony CLIE, Palm m5xx, Handspring Visor).

%description -l pt_BR
Este conjunto de ferramentas permite transferir programas e dados
entre m�quinas *nix e o Palm Pilot. Alguns utilit�rios extras permitem
coisas como sincronizar dados entre o calend�rio do Pilot e o Ical.

%description -l uk
��� ��¦� ���������Ԧ� ������Ѥ ��� ���������� �������� �� ����� �����
ͦ� ��������� Linux �� PalmPilot. ��� ��� ����� ˦���� ����������
���̦�, �˦ ������������ ��˦ ��ަ �� ����������æ� ���������
PalmPilot �� Ical.

%description -l ru
���� ����� ������������ ��������� ��� ���������� ��������� � �����
������ ����� ��������� Linux � PalmPilot. �� ����� ����� ���������
�������������� ������, �������������� ����� ���� ��� �������������
��������� PalmPilot � Ical.

%package devel
Summary:	Pilot development header files
Summary(es):	Archivos de inclusi�n para el desarrollo de programas
Summary(pl):	Pliki nag��wkowe do biblioteki pilot-link
Summary(pt_BR):	Arquivos de inclus�o para o desenvolvimento de programas
Summary(ru):	����� ��� ���������� �������� �������������� � PalmPilot
Summary(uk):	����� ��� �������� ������� ������Ħ� � PalmPilot
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the development headers that are used to build
the pilot-link package.

%description devel -l es
Este paquete contiene los archivos de inclusi�n necesarios para crear
aplicaciones Pilot.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe u�ywane przy budowaniu pakietu
pilot-link.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o necess�rios para gerar
aplica��es Pilot.

%description devel -l ru
���� ����� �������� ����� ���������� C ��� ���������� ��������
�������������� � PalmPilot.

%description devel -l uk
��� ����� ͦ����� ����� �������˦� C ��� �������� ������� ������Ħ� �
PalmPilot.

%package static
Summary:	Pilot link static libraries
Summary(es):	Bibliotecas est�ticas necesarias para crear aplicaciones Pilot
Summary(pl):	Statyczne biblioteki pilot-link
Summary(pt_BR):	Bibliotecas est�ticas necess�rias para gerar aplica��es Pilot
Summary(ru):	����������� ���������� ��� ���������� �������� �������������� � PalmPilot
Summary(uk):	������Φ ¦�̦����� ��� �������� ������� ������Ħ� � PalmPilot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Pilot link static libraries.

%description static -l es
Este paquete contiene las bibliotecas est�ticas necesarias para crear
aplicaciones Pilot.

%description static -l pl
Statyczne biblioteki pilot-link.

%description static -l pt_BR
Este pacote cont�m as bibliotecas est�ticas necess�rias para gerar
aplica��es Pilot.

%description static -l ru
���� ����� �������� ����������� ���������� ��� ���������� ��������
�������������� � PalmPilot.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦����� ��� �������� ������� ������Ħ� �
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
