%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

Name:           mingw32-flac
Version:        1.2.1
Release:        1%{?dist}
Summary:        Free Lossless Audio Codec Library

License:        BSD 3-Clause
URL:            http://flac.sourceforge.net
Source0:        http://dl.sourceforge.net/sourceforge/flac/flac-%{version}.tar.gz
#Source1000:     %{name}-%{version}-rpmlintrc
Patch0:         flac-1.2.1-no_undefined.patch
Patch1:         flac-1.2.1-asm.patch
Patch2:         flac-1.2.1-gcc43.patch
Patch3:         flac-1.2.1-hidesyms.patch
Patch4:         flac-1.2.1-tests.patch
Patch5:         flac-1.2.1-cflags.patch
Patch6:         flac-1.2.1-bitreader.patch
Patch7:         flac-1.2.1-automake-1.8.patch
#Patch1:         flac-1.2.1-wsocklibs.patch
Group:          Development/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 68
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libogg
BuildRequires:  mingw32-win-iconv
#BuildRequires:  mingw32-gettext
BuildRequires:  libtool, autoconf, automake

BuildRequires:  gettext-devel


%description
FLAC is an open source lossless audio codec developed by Josh Coalson.


%description -n mingw32-flac
This package contains the library for FLAC (Free Lossless Audio Codec)
developed by Josh Coalson.


%package -n mingw32-flac++
Summary:        Free Lossless Audio Codec C++ Library
Group:          Development/Libraries

%description -n mingw32-flac++
This package contains the C++ library for FLAC (Free Lossless Audio
Codec) developed by Josh Coalson.


%{_mingw32_debug_package}


%prep
%setup -q -n flac-%{version}

%patch0 -p1 -b .no_undefined
#%patch1 -p1 -b .asm
#%patch2 -p1 -b .gcc43
#%patch3 -p1 -b .hidesyms
# reduce number of tests
%patch4 -p1 -b .tests
%patch5 -p1 -b .cflags
%patch7 -p0 -b .automake-1.8
#%patch6 -p0 -b .bitreader

#%patch1 -p1 -b .wsocklibs


%build
./autogen.sh -V
%{_mingw32_configure} \
	--enable-shared --disable-static
%{_mingw32_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

%{_mingw32_make} DESTDIR=$RPM_BUILD_ROOT install

# Don't want the *.la files.
find $RPM_BUILD_ROOT -name '*.la' -delete

%clean
rm -rf $RPM_BUILD_ROOT


%files -n mingw32-flac
%{_mingw32_bindir}/metaflac.exe
%{_mingw32_bindir}/flac.exe
%{_mingw32_mandir}/man1/metaflac.1*
%{_mingw32_mandir}/man1/flac.1*
%{_mingw32_bindir}/libFLAC-8.dll
%{_mingw32_includedir}/FLAC
%{_mingw32_libdir}/libFLAC.dll.a
%{_mingw32_libdir}/pkgconfig/flac.pc
%{_mingw32_datadir}/aclocal/libFLAC.m4
%{_mingw32_datadir}/doc/flac-%{version}

%files -n mingw32-flac++
%defattr(-,root,root)
%{_mingw32_bindir}/libFLAC++-6.dll
%{_mingw32_libdir}/libFLAC++.dll.a
%{_mingw32_includedir}/FLAC++
%{_mingw32_libdir}/pkgconfig/flac++.pc
%{_mingw32_datadir}/aclocal/libFLAC++.m4


%changelog
* Wed Nov 9 2011 Tim Mayberry <mojofunk@gmail.com> - 1.2.1-1
- Initial RPM release
- patch situation needs cleanup
