%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name libsndfile

Name:		mingw-libsndfile
Version:	1.0.27
Release:	1%{?dist}
Summary:	Library for reading and writing sound files
License:	LGPLv2+
Group:		System Environment/Libraries
URL:		http://www.mega-nerd.com/libsndfile/
Source0:	http://www.mega-nerd.com/libsndfile/libsndfile-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: mingw32-libvorbis
BuildRequires: mingw64-libvorbis
BuildRequires: mingw32-libogg
BuildRequires: mingw64-libogg
BuildRequires: mingw32-flac
BuildRequires: mingw64-flac
BuildRequires: pkgconfig 

Requires: pkgconfig


%description
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface. It can
currently read/write 8, 16, 24 and 32-bit PCM files as well as 32 and
64-bit floating point WAV files and a number of compressed formats. It
compiles and runs on *nix, MacOS, and Win32.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface. It can
currently read/write 8, 16, 24 and 32-bit PCM files as well as 32 and
64-bit floating point WAV files and a number of compressed formats. It
compiles and runs on *nix, MacOS, and Win32.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface. It can
currently read/write 8, 16, 24 and 32-bit PCM files as well as 32 and
64-bit floating point WAV files and a number of compressed formats. It
compiles and runs on *nix, MacOS, and Win32.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the libsndfile libraries
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static cross compiled version of the libsndfile library.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the libsndfile libraries
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static cross compiled version of the libsndfile library.


%{?mingw_debug_package}


%prep
%setup -q -n %{mingw_pkg_name}-%{version}

%build
%mingw_configure --enable-static --disable-dependency-tracking --disable-alsa --disable-sqlite

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Remove docs which duplicate native package
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}

# Remove manpages which duplicate those in Fedora native.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}


%files -n mingw32-%{mingw_pkg_name}
%doc COPYING AUTHORS README NEWS ChangeLog
%{mingw32_bindir}/*sndfile*.exe
%{mingw32_bindir}/libsndfile-1.dll
%exclude %{mingw32_libdir}/libsndfile.la
%{mingw32_includedir}/sndfile.h
%{mingw32_includedir}/sndfile.hh
%{mingw32_libdir}/libsndfile.dll.a
%{mingw32_libdir}/pkgconfig/sndfile.pc

%files -n mingw64-%{mingw_pkg_name}
%doc COPYING AUTHORS README NEWS ChangeLog
%{mingw64_bindir}/*sndfile*.exe
%{mingw64_bindir}/libsndfile-1.dll
%exclude %{mingw64_libdir}/libsndfile.la
%{mingw64_includedir}/sndfile.h
%{mingw64_includedir}/sndfile.hh
%{mingw64_libdir}/libsndfile.dll.a
%{mingw64_libdir}/pkgconfig/sndfile.pc

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libsndfile.a

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libsndfile.a


%changelog
* Sat Aug 6 2016 Tim Mayberry <mojofunk@gmail.com> - 1.0.27
- Update to version 1.0.27
- Rebuild for F24

* Tue Mar 10 2015 Tim Mayberry <mojofunk@gmail.com> - 1.0.26pre5-1
- new 1.0.26pre5 version
- Rebuild for F21

* Wed Apr 23 2014 Tim Mayberry <mojofunk@gmail.com> - 1.0.25-3
- Rebuild for F20

* Sat Jun 30 2012 Tim Mayberry <mojofunk@gmail.com> - 1.0.25-2
- Update spec file to F17 package guidelines

* Wed Dec 14 2011 Tim Mayberry <mojofunk@gmail.com> - 1.0.25-1
- Initial mingw-w64 package
