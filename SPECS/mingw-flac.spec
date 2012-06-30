%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name flac

Name:           mingw-flac
Version:        1.2.1
Release:        2%{?dist}
Summary:        Free Lossless Audio Codec Library

License:        BSD 3-Clause
URL:            http://flac.sourceforge.net
Source0:        http://dl.sourceforge.net/sourceforge/flac/flac-%{version}.tar.gz
Patch0:         flac-1.2.1-no_undefined.patch
#Patch1:         flac-1.2.1-asm.patch
#Patch2:         flac-1.2.1-gcc43.patch
#Patch3:         flac-1.2.1-hidesyms.patch
Patch4:         flac-1.2.1-tests.patch
Patch5:         flac-1.2.1-cflags.patch
#Patch6:         flac-1.2.1-bitreader.patch
Patch7:         flac-1.2.1-automake-1.8.patch
Patch8:         flac-1.2.1-nodocs.patch
#Patch1:         flac-1.2.1-wsocklibs.patch
Group:          Development/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-libogg
BuildRequires:  mingw64-libogg
#BuildRequires:  mingw32-win_iconv
#BuildRequires:  mingw64-win_iconv
BuildRequires:  libtool, autoconf, automake

Requires: pkgconfig


%description
FLAC is an open source lossless audio codec developed by Josh Coalson.

%package -n mingw32-%{mingw_pkg_name}
Summary:        Free Lossless Audio Codec Library
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
This package contains the library for FLAC (Free Lossless Audio Codec)
developed by Josh Coalson.


%package -n mingw32-flac++
Summary:        Free Lossless Audio Codec C++ Library
Group:          Development/Libraries

%description -n mingw32-flac++
This package contains the C++ library for FLAC (Free Lossless Audio
Codec) developed by Josh Coalson.

%package -n mingw64-%{mingw_pkg_name}
Summary:        Free Lossless Audio Codec Library
Group:          Development/Libraries


%description -n mingw64-%{mingw_pkg_name}
This package contains the library for FLAC (Free Lossless Audio Codec)
developed by Josh Coalson.


%package -n mingw64-flac++
Summary:        Free Lossless Audio Codec C++ Library
Group:          Development/Libraries

%description -n mingw64-flac++
This package contains the C++ library for FLAC (Free Lossless Audio
Codec) developed by Josh Coalson.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the FLAC library
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static cross compiled version of the FLAC library.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the FLAC library
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static cross compiled version of the FLAC library.

%package -n mingw32-%{mingw_pkg_name}++-static
Summary:        Static cross compiled version of the FLAC C++ library
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}++-static
Static cross compiled version of the FLAC C++ library.

%package -n mingw64-%{mingw_pkg_name}++-static
Summary:        Static cross compiled version of the FLAC C++ library
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}++-static
Static cross compiled version of the FLAC C++ library.


%{?mingw_debug_package}


%prep
%setup -q -n flac-%{version}

%patch0 -p1 -b .no_undefined
##%patch1 -p1 -b .asm
##%patch2 -p1 -b .gcc43
##%patch3 -p1 -b .hidesyms
# reduce number of tests
%patch4 -p1 -b .tests
%patch5 -p1 -b .cflags
%patch7 -p0 -b .automake-1.8
%patch8 -p0 -b .nodocs
##%patch6 -p0 -b .bitreader

#%patch1 -p1 -b .wsocklibs


%build
./autogen.sh -V
%mingw_configure --enable-shared --enable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Remove manpages which duplicate those in Fedora native.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# Don't want the *.la files.
find $RPM_BUILD_ROOT -name '*.la' -delete


%files -n mingw32-%{mingw_pkg_name}
%doc COPYING.FDL COPYING.GPL COPYING.LGPL COPYING.Xiph
%{mingw32_bindir}/metaflac.exe
%{mingw32_bindir}/flac.exe
%{mingw32_bindir}/libFLAC-8.dll
%{mingw32_includedir}/FLAC
%{mingw32_libdir}/libFLAC.dll.a
%{mingw32_libdir}/pkgconfig/flac.pc
%{mingw32_datadir}/aclocal/libFLAC.m4 

%files -n mingw32-flac++
%{mingw32_bindir}/libFLAC++-6.dll
%{mingw32_libdir}/libFLAC++.dll.a
%{mingw32_includedir}/FLAC++
%{mingw32_libdir}/pkgconfig/flac++.pc
%{mingw32_datadir}/aclocal/libFLAC++.m4 

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libFLAC.a

%files -n mingw32-%{mingw_pkg_name}++-static
%{mingw32_libdir}/libFLAC++.a

%files -n mingw64-%{mingw_pkg_name}
%doc COPYING.FDL COPYING.GPL COPYING.LGPL COPYING.Xiph
%{mingw64_bindir}/metaflac.exe
%{mingw64_bindir}/flac.exe
%{mingw64_bindir}/libFLAC-8.dll
%{mingw64_includedir}/FLAC
%{mingw64_libdir}/libFLAC.dll.a
%{mingw64_libdir}/pkgconfig/flac.pc
%{mingw64_datadir}/aclocal/libFLAC.m4 

%files -n mingw64-flac++
%{mingw64_bindir}/libFLAC++-6.dll
%{mingw64_libdir}/libFLAC++.dll.a
%{mingw64_includedir}/FLAC++
%{mingw64_libdir}/pkgconfig/flac++.pc
%{mingw64_datadir}/aclocal/libFLAC++.m4 

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libFLAC.a

%files -n mingw64-%{mingw_pkg_name}++-static
%{mingw64_libdir}/libFLAC++.a


%changelog
* Sat Jun 30 2012 Tim Mayberry <mojofunk@gmail.com> - 1.2.1-2
- Update spec file to F17 MinGW package guidelines

* Tue Dec 13 2011 Tim Mayberry <mojofunk@gmail.com> - 1.2.1-1
- Initial mingw-w64 package
- patch situation needs cleanup
