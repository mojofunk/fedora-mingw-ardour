%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

Name:		mingw32-libsndfile
Version:	1.0.25
Release:	1%{?dist}
Summary:	Library for reading and writing sound files
License:	LGPLv2+
Group:		System Environment/Libraries
URL:		http://www.mega-nerd.com/libsndfile/
Source0:	http://www.mega-nerd.com/libsndfile/libsndfile-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)

BuildRequires: mingw32-filesystem >= 23
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-libvorbis
BuildRequires: mingw32-libogg
BuildRequires: mingw32-flac
BuildRequires: pkgconfig 

Requires: pkgconfig

BuildArch:      noarch


%{?_mingw32_debug_package}


%description
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface. It can
currently read/write 8, 16, 24 and 32-bit PCM files as well as 32 and
64-bit floating point WAV files and a number of compressed formats. It
compiles and runs on *nix, MacOS, and Win32.

%package static
Summary:        Static cross compiled version of the libsndfile libraries
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static cross compiled version of the libsndfile library.


%prep
%setup -q -n libsndfile-%{version}

%build
%{_mingw32_configure}  \
	--enable-static \
	--disable-dependency-tracking \
	--disable-alsa \
	--disable-sqlite \
	--disable-shave

make %{?_smp_mflags}


%install
rm -rf %{buildroot} __docs
make install DESTDIR=%{buildroot}
cp -pR %{buildroot}%{_mingw32_docdir}/libsndfile1-dev/html __docs
rm -rf %{buildroot}%{_mingw32_docdir}/libsndfile1-dev

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README NEWS ChangeLog __docs/*
%{_mingw32_bindir}/*sndfile*.exe
%{_mingw32_mandir}/man1/*.1
%{_mingw32_bindir}/libsndfile-1.dll
%exclude %{_mingw32_libdir}/libsndfile.la
%{_mingw32_includedir}/sndfile.h
%{_mingw32_includedir}/sndfile.hh
%{_mingw32_libdir}/libsndfile.dll.a
%{_mingw32_libdir}/libsndfile.dll.a
%{_mingw32_libdir}/pkgconfig/sndfile.pc

%files static
%defattr(-,root,root,-)
%{_mingw32_libdir}/libsndfile.a


%changelog
* Tue May 1 2012 Tim Mayberry <mojofunk@gmail.com> - 1.0.25-1
- Update to 1.0.25

* Wed Nov 9 2011 Tim Mayberry <mojofunk@gmail.com> - 1.0.23-4
- enable external libs, depends on flac, ogg, vorbis
- use global in macros instead of define

* Sat Apr 9 2011 Tim Mayberry <mojofunk@gmail.com> - 1.0.23-3
- remove separate devel package
- add static library package

* Sat Apr 9 2011 Tim Mayberry <mojofunk@gmail.com> - 1.0.23-2
- rebuild using mingw64 compiler
- add __debug_install_post macro

* Wed Nov 3 2010 Tim Mayberry <mojofunk@gmail.com> - 1.0.23-1
- update to latest release
- added --disable-shave to configure options to allow build to succeed
* Sun Nov 30 2008 Tim Mayberry <mojofunk@gmail.com> - 1.0.18pre24h-1
- Initial MinGW build of pre-release version
