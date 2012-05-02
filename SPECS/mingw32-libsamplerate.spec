%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

Summary:	MinGW Windows Sample rate conversion library for audio data
Name:		mingw32-libsamplerate
Version:	0.1.7
Release:	5%{?dist}
License:	GPLv2+
Group:		System Environment/Libraries
URL:		http://www.mega-nerd.com/SRC/
Source0:	http://www.mega-nerd.com/SRC/libsamplerate-%{version}.tar.gz
#Patch0:         libsamplerate-0.1.7-test.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:	mingw32-libsndfile >= 1.0.23
BuildRequires:  pkgconfig

Requires:       pkgconfig


%{?_mingw32_debug_package}


%description
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.


%package static
Summary:	Static MinGW Windows Samplerate library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static MinGW Windows Samplerate library


%prep
%setup -q -n libsamplerate-%{version}


%build
%{_mingw32_configure} \
  --disable-dependency-tracking \
  --disable-fftw \
  --enable-static
# Don't use rpath!
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT _doc
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_mingw32_libdir}/*samplerate*.la
cp -a doc _doc
rm _doc/Makefile*


%check
#export LD_LIBRARY_PATH=`pwd`/src/.libs
#make check
#unset LD_LIBRARY_PATH


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README _doc/*
%{_mingw32_bindir}/*sndfile-resample*.exe
%{_mingw32_bindir}/libsamplerate-0.dll
%{_mingw32_libdir}/libsamplerate.dll.a
%{_mingw32_includedir}/samplerate.h
%{_mingw32_libdir}/pkgconfig/samplerate.pc

%files static
%defattr(-,root,root,-)
%{_mingw32_libdir}/libsamplerate.a


%changelog
* Wed Nov 9 2011 Tim Mayberry <mojofunk@gmail.com> - 0.1.7-5
- Change define's to globals in macros
- rebuild for Fedora 16

* Sun Apr 12 2011 Tim Mayberry <mojofunk@gmail.com> - 0.1.7-4
- Add mingw32-libsndfile to BuildRequires

* Sun Apr 12 2011 Tim Mayberry <mojofunk@gmail.com> - 0.1.7-3
- rebuild using F14 mingw toolchain

* Sun Apr 10 2011 Tim Mayberry <mojofunk@gmail.com> - 0.1.7-2
- rebuild using mingw64 compiler

* Sat Feb 19 2011 Tim Mayberry <mojofunk@gmail.com> 0.1.7-1
- Mingw package roughly based on fedora spec
