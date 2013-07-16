%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name flac

Name:           mingw-flac
Version:        1.3.0
Release:        1%{?dist}
Summary:        Free Lossless Audio Codec Library

License: BSD and GPLv2+ and GFDL
Source0: http://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz
URL: http://www.xiph.org/flac/
Patch8:         flac-1.3.0-nodocs.patch
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

%patch8 -p0 -b .nodocs


%build
./autogen.sh -V
%mingw_configure --enable-shared --enable-static \
    --disable-xmms-plugin \
    --disable-silent-rules \
    --disable-thorough-tests \
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
* Tue Jul 16 2013 Tim Mayberry <mojofunk@gmail.com> - 1.3.0-1
- Update to flac version in F19

* Sat Jun 30 2012 Tim Mayberry <mojofunk@gmail.com> - 1.2.1-2
- Update spec file to F17 MinGW package guidelines

* Tue Dec 13 2011 Tim Mayberry <mojofunk@gmail.com> - 1.2.1-1
- Initial mingw-w64 package
- patch situation needs cleanup
