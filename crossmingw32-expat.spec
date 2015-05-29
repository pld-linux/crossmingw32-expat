Summary:	XML 1.0 parser - Ming32 cross version
Summary(pl.UTF-8):	Analizator składni XML-a 1.0 - wersja skrośna dla Ming32
%define		realname		expat
Name:		crossmingw32-%{realname}
Version:	2.1.0
Release:	1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/expat/%{realname}-%{version}.tar.gz
# Source0-md5:	dd7dab7a5fea97d2a6a43f511449b7cd
Patch0:		%{realname}-ac_fixes.patch
URL:		http://www.libexpat.org/
BuildRequires:	autoconf >= 2.52
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
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--target=%{target} \
	--host=%{target}

%{__make} buildlib

%install
rm -rf $RPM_BUILD_ROOT

%{__make} installlib \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

rm -rf $RPM_BUILD_ROOT%{_datadir}/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
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
