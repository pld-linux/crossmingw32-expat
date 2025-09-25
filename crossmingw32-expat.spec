Summary:	XML 1.0 parser - Ming32 cross version
Summary(pl.UTF-8):	Analizator składni XML-a 1.0 - wersja skrośna dla Ming32
%define		realname		expat
Name:		crossmingw32-%{realname}
Version:	2.7.3
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://downloads.sourceforge.net/expat/%{realname}-%{version}.tar.xz
# Source0-md5:	423975a2a775ff32f12c53635b463a91
URL:		http://www.libexpat.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	crossmingw32-gcc >= 1:3.2
BuildRequires:	libtool >= 2:2.4
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1
%define		_enable_debug_packages	0

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_docdir			%{_sysprefix}/share/doc
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++
%define		__pkgconfig_provides	%{nil}
%define		__pkgconfig_requires	%{nil}

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
%endif
# -z options are invalid for mingw linker
%define		filterout_ld	-Wl,-z,.*
%define		filterout_c	-f[-a-z0-9=]*
%define		filterout_cxx	-f[-a-z0-9=]*

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

This package contains the cross version for Win32.

%description -l pl.UTF-8
Expat to napisany w języku C analizator składni XML-a. Dąży do pełnej
zgodności ze specyfikacją. Aktualnie nie jest analizatorem, który
potwiedzał by zgodność ze specyfikacją.

Ten pakiet zawiera wersję skrośną dla Win32.

%package static
Summary:	Static expat library (cross mingw32 version)
Summary(pl.UTF-8):	Statyczna biblioteka expat (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static expat library (cross mingw32 version).

%description static -l pl.UTF-8
Statyczna biblioteka expat (wersja skrośna mingw32).

%package dll
Summary:	DLL expat library for Windows
Summary(pl.UTF-8):	Biblioteka DLL expat dla Windows
Group:		Applications/Emulators
Requires:	wine

%description dll
DLL expat library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL expat dla Windows.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# remove SIZEOF_VOID_P define, see buildconf.sh
%{__sed} -i -e '/^\/\* The size of `void \*/,/^$/ d' expat_config.h.in
%configure \
	--build=i686-pc-linux-gnu \
	--host=%{target} \
	--target=%{target} \
	--without-docbook \
	--without-xmlwf

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
%{__mv} $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/cmake

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING Changes README.md
%{_libdir}/libexpat.dll.a
%{_libdir}/libexpat.la
%{_includedir}/expat*.h
%{_pkgconfigdir}/expat.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libexpat.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libexpat-1.dll
