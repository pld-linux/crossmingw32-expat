%define		realname		expat
Summary:	XML 1.0 parser
Summary(pl):	Parser XML 1.0
Summary(pt_BR):	Biblioteca XML expat
Summary(ru):	Переносимая библиотека разбора XML (expat)
Summary(uk):	Переносима б╕бл╕отека розбору XML (expat)
Name:		crossmingw32-%{realname}
Version:	1.95.6
Release:	4
Epoch:		1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/expat/%{realname}-%{version}.tar.gz
# Source0-md5: ca78d94e83e9f077b5da2bfe28ba986a
Source1:	%{realname}.m4
Patch0:		%{realname}-DESTDIR.patch
Patch1:		%{realname}-gcc3-c++.patch
Patch2:		%{realname}-ac_fixes.patch
URL:		http://expat.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{realname}-%{version}-root-%(id -u -n)
Obsoletes:	libexpat1_95

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%description -l pl
Expat to parser XML napisany w jЙzyku C.

%description -l pt_BR
Esta И a biblioteca, em C, XML expat, de James Clark. и um analisador
orientado a fluxo de informaГУes que pede o uso de handlers para lidar
com a estrutura que o analisador encontrar no documento.

%description -l ru
Expat -- парсер XML 1.0, написанный на C. Он предназначен для того,
чтобы быть полностью совместимым. В настоящее время это не проверяющий
("not a validating") XML парсер.

%description -l uk
Expat -- парсер XML 1.0, написаний на C. Розрахований на те, щоб бути
повн╕стю сум╕сним. Нараз╕ це не перев╕ряючий ("not a validating") XML
парсер.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CC=%{target}-gcc ; export CC
CXX=%{target}-g++ ; export CXX
LD=%{target}-ld ; export LD
AR=%{target}-ar ; export AR
AS=%{target}-as ; export AS
CROSS_COMPILE=1 ; export CROSS_COMPILE
CPPFLAGS="-I%{arch}/include" ; export CPPFLAGS
RANLIB=%{target}-ranlib ; export RANLIB

%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--target=%{target} \
	--host=%{target_platform} \
	--prefix=%{arch} \
	--disable-static \
	--bindir=%{arch}/bin \
	--libdir=%{arch}/lib \
	--includedir=%{arch}/include
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_aclocaldir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{arch}
