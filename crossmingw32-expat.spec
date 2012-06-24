%define		realname		expat
Summary:	XML 1.0 parser
Summary(pl):	Analizator sk�adni XML 1.0
Summary(pt_BR):	Biblioteca XML expat
Summary(ru):	����������� ���������� ������� XML (expat)
Summary(uk):	���������� ¦�̦����� ������� XML (expat)
Name:		crossmingw32-%{realname}
Version:	1.95.7
Release:	1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/expat/%{realname}-%{version}.tar.gz
# Source0-md5:	2ff59c2a5cbdd21a285c5f343e214fa9
Patch0:		%{realname}-DESTDIR.patch
Patch1:		%{realname}-ac_fixes.patch
URL:		http://expat.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	crossmingw32-gcc
BuildRequires:	libtool
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}

%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%description -l pl
Expat to napisany w j�zyku C analizator sk�adni XML. D��y do pe�nej
zgodno�ci ze specyfikacj�. Aktualnie nie jest analizatorem, kt�ry
potwiedza�by zgodno�� ze specyfikacj�.

%description -l pt_BR
Esta � a biblioteca, em C, XML expat, de James Clark. � um analisador
orientado a fluxo de informa��es que pede o uso de handlers para lidar
com a estrutura que o analisador encontrar no documento.

%description -l ru
Expat -- ������ XML 1.0, ���������� �� C. �� ������������ ��� ����,
����� ���� ��������� �����������. � ��������� ����� ��� �� �����������
("not a validating") XML ������.

%description -l uk
Expat -- ������ XML 1.0, ��������� �� C. ������������ �� ��, ��� ����
���Φ��� ��ͦ����. ����ڦ �� �� ����צ������ ("not a validating") XML
������.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--target=%{target} \
	--host=%{target_platform} \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_bindir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libexpat-0.dll
%{_libdir}/libexpat.dll.a
%{_libdir}/libexpat.la
%{_includedir}/expat.h
