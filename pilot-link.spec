Summary:	File transfer utilities between Linux and PalmPilots
Summary(es):	Bibliotecas est�ticas necesarias para generar aplicaciones Pilot
Summary(pt_BR):	Utilit�rios de transfer�ncia de dados entre Unix e o Pilot
Name:		pilot-link
Version:	0.9.5
Release:	11
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ryeham.ee.ryerson.ca/pub/PalmOS/%{name}-%{version}.tar.bz2
Patch0:		%{name}-pixdir.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-misc.patch
Patch3:		%{name}-ack.patch
Patch4:		%{name}-gcc3.patch
Patch5:		%{name}-ac_fixes.patch
URL:		http://www.gnu-designs.com/pilot-link/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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

%description -l es
Bibliotecas est�ticas necesarias para generar aplicaciones Pilot.

%description -l pt_BR
Este conjunto de ferramentas permite transferir programas e dados
entre m�quinas
- *nix e o Palm Pilot. Alguns utilit�rios extras permitem coisas como
  sincronizar dados entre o calend�rio do Pilot e o Ical.

%package devel
Summary:	Pilot development header files
Summary(es):	Archivos de inclusi�n para el desarrollo de programas
Summary(pt_BR):	Arquivos de inclus�o para o desenvolvimento de programas
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
This package contains the development headers that are used to build
the pilot-link package. It also includes the static libraries
necessary to build static pilot apps.

%description -l es devel
Este paquete contiene los archivos de inclusi�n necesarios para crear
aplicaciones Pilot.

%description -l pt_BR devel
Este pacote cont�m os arquivos de inclus�o necess�rios para gerar
aplica��es Pilot.

%package static
Summary:	Pilot link static libraries
Summary(es):	Bibliotecas est�ticas necesarias para crear aplicaciones Pilot
Summary(pt_BR):	Bibliotecas est�ticas necess�rias para gerar aplica��es Pilot
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Pilot link static libraries.

%description -l es static
Este paquete contiene las bibliotecas est�ticas necesarias para crear
aplicaciones Pilot.

%description -l pt_BR static
Este pacote cont�m as bibliotecas est�ticas necess�rias para gerar
aplica��es Pilot.

%prep 
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
libtoolize --copy --force
aclocal
chmod +w configure
autoconf

CFLAGS="%{rpmcflags} -I%{_prefix}/X11R6/include"
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
