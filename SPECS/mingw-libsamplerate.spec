%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name libsamplerate

Summary:	MinGW Windows Sample rate conversion library for audio data
Name:		mingw-libsamplerate
Version:	0.1.8
Release:	3%{?dist}
License:	GPLv2+
Group:		System Environment/Libraries
URL:		http://www.mega-nerd.com/SRC/
Source0:	http://www.mega-nerd.com/SRC/libsamplerate-%{version}.tar.gz
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

BuildRequires: mingw32-libsndfile >= 1.0.25
BuildRequires: mingw64-libsndfile >= 1.0.25
BuildRequires: pkgconfig

Requires:      pkgconfig


%description
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static MinGW Windows Samplerate library
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static cross compiled version of the libsndfile library.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static MinGW Windows Samplerate library
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static cross compiled version of the libsndfile library.


%{?mingw_debug_package}


%prep
%setup -q -n %{mingw_pkg_name}-%{version}


%build
%mingw_configure --disable-dependency-tracking --disable-fftw --enable-static

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
%doc AUTHORS COPYING README
%{mingw32_bindir}/*sndfile-resample*.exe
%{mingw32_bindir}/libsamplerate-0.dll
%exclude %{mingw32_libdir}/libsamplerate.la
%{mingw32_libdir}/libsamplerate.dll.a
%{mingw32_includedir}/samplerate.h
%{mingw32_libdir}/pkgconfig/samplerate.pc

%files -n mingw64-%{mingw_pkg_name}
%doc AUTHORS COPYING README
%{mingw64_bindir}/*sndfile-resample*.exe
%{mingw64_bindir}/libsamplerate-0.dll
%exclude %{mingw64_libdir}/libsamplerate.la
%{mingw64_libdir}/libsamplerate.dll.a
%{mingw64_includedir}/samplerate.h
%{mingw64_libdir}/pkgconfig/samplerate.pc

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libsamplerate.a

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libsamplerate.a

%changelog
* Wed Apr 23 2014 Tim Mayberry <mojofunk@gmail.com> - 0.1.8-3
- Rebuild for Fedora 20

* Sat Jun 30 2012 Tim Mayberry <mojofunk@gmail.com> - 0.1.8-2
- Update spec for F17 MinGW package guidelines

* Wed Dec 14 2011 Tim Mayberry <mojofunk@gmail.com> - 0.1.8-1
- Initial mingw-w64 package
