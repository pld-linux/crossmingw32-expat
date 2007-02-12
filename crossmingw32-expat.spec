%define		realname		expat
Summary:	XML 1.0 parser - Ming32 cross version
Summary(pl.UTF-8):   Analizator składni XML-a 1.0 - wersja skrośna dla Ming32
Summary(pt_BR.UTF-8):   Biblioteca XML expat
Summary(ru.UTF-8):   Переносимая библиотека разбора XML (expat)
Summary(uk.UTF-8):   Переносима бібліотека розбору XML (expat)
Name:		crossmingw32-%{realname}
Version:	2.0.0
Release:	1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/expat/%{realname}-%{version}.tar.gz
# Source0-md5:	d945df7f1c0868c5c73cf66ba9596f3f
Patch0:		%{realname}-ac_fixes.patch
Patch1:		%{realname}-soname.patch
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

%ifarch alpha sparc sparc64 sparcv9
# alpha's -mieee and sparc's -mtune=* are not valid for target's gcc
%define		optflags	-O2
%endif

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

This package contains the cross version for Win32.

%description -l pl.UTF-8
Expat to napisany w języku C analizator składni XML-a. Dąży do pełnej
zgodności ze specyfikacją. Aktualnie nie jest analizatorem, który
potwiedzał by zgodność ze specyfikacją.

Ten pakiet zawiera wersję skrośną dla Win32.

%description -l pt_BR.UTF-8
Esta é a biblioteca, em C, XML expat, de James Clark. É um analisador
orientado a fluxo de informações que pede o uso de handlers para lidar
com a estrutura que o analisador encontrar no documento.

%description -l ru.UTF-8
Expat -- парсер XML 1.0, написанный на C. Он предназначен для того,
чтобы быть полностью совместимым. В настоящее время это не проверяющий
("not a validating") XML парсер.

%description -l uk.UTF-8
Expat -- парсер XML 1.0, написаний на C. Розрахований на те, щоб бути
повністю сумісним. Наразі це не перевіряючий ("not a validating") XML
парсер.

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
%{_bindir}/libexpat-0.dll
%{_libdir}/libexpat.dll.a
%{_libdir}/libexpat.la
%{_includedir}/expat*.h
