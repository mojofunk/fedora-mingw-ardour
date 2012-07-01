%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name fftw

Name:           mingw-fftw
Version:        3.2.2
Release:        2%{?dist}
Summary:        A Fast Fourier Transform library
Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.fftw.org
Source0:        http://www.fftw.org/fftw-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

# For check phase
BuildRequires:  gcc-gfortran

BuildRequires:  pkgconfig

BuildArch: noarch


%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the FFTW library
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static cross compiled version of the FFTW library.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the FFTW library
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static cross compiled version of the FFTW library.


%{?mingw_debug_package}


%prep
%setup -q -c %{name}-%{version}
for dir in single double long; do
  cp -a fftw-%{version} $dir
done
rm -rf fftw-%{version}


%build
# Configure uses g77 by default, if present on system
export F77=gfortran

CONFIG_FLAGS="--enable-shared --enable-static --disable-dependency-tracking"
pushd double
        %mingw_configure $CONFIG_FLAGS
#        sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#        sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
        %mingw_make %{?_smp_mflags}
popd
pushd single
        %mingw_configure $CONFIG_FLAGS "--enable-single"
#        sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#        sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
        %mingw_make %{?_smp_mflags}
popd
pushd long
        %mingw_configure $CONFIG_FLAGS "--enable-long-double"
#        sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#        sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
        %mingw_make %{?_smp_mflags}
popd


%install

pushd double
        %mingw_make_install DESTDIR=${RPM_BUILD_ROOT}
        cp -a AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO ../
        cp -a doc/ ../
popd
pushd single
        %mingw_make_install DESTDIR=${RPM_BUILD_ROOT}
popd
pushd long
        %mingw_make_install DESTDIR=${RPM_BUILD_ROOT}
popd

# no .la, please
find $RPM_BUILD_ROOT%{mingw32_libdir} -name '*.la' -delete
find $RPM_BUILD_ROOT%{mingw64_libdir} -name '*.la' -delete

# Don't duplicate docs in the native package
rm -rf ${RPM_BUILD_ROOT}%{mingw32_infodir}
rm -rf ${RPM_BUILD_ROOT}%{mingw64_infodir}
rm -rf ${RPM_BUILD_ROOT}%{mingw32_mandir}
rm -rf ${RPM_BUILD_ROOT}%{mingw64_mandir}

%files -n mingw32-%{mingw_pkg_name}
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{mingw32_bindir}/fftw-wisdom-to-conf
%{mingw32_bindir}/fftw-wisdom.exe
%{mingw32_bindir}/fftwf-wisdom.exe
%{mingw32_bindir}/fftwl-wisdom.exe
%{mingw32_bindir}/libfftw3-3.dll
%{mingw32_bindir}/libfftw3f-3.dll
%{mingw32_bindir}/libfftw3l-3.dll
%{mingw32_includedir}/fftw3.f
%{mingw32_includedir}/fftw3.h
%{mingw32_libdir}/libfftw3.dll.a
%{mingw32_libdir}/libfftw3f.dll.a
%{mingw32_libdir}/libfftw3l.dll.a
%{mingw32_libdir}/pkgconfig/fftw3.pc
%{mingw32_libdir}/pkgconfig/fftw3f.pc
%{mingw32_libdir}/pkgconfig/fftw3l.pc

%files -n mingw64-%{mingw_pkg_name}
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{mingw64_bindir}/fftw-wisdom-to-conf
%{mingw64_bindir}/fftw-wisdom.exe
%{mingw64_bindir}/fftwf-wisdom.exe
%{mingw64_bindir}/fftwl-wisdom.exe
%{mingw64_bindir}/libfftw3-3.dll
%{mingw64_bindir}/libfftw3f-3.dll
%{mingw64_bindir}/libfftw3l-3.dll
%{mingw64_includedir}/fftw3.f
%{mingw64_includedir}/fftw3.h
%{mingw64_libdir}/libfftw3.dll.a
%{mingw64_libdir}/libfftw3f.dll.a
%{mingw64_libdir}/libfftw3l.dll.a
%{mingw64_libdir}/pkgconfig/fftw3.pc
%{mingw64_libdir}/pkgconfig/fftw3f.pc
%{mingw64_libdir}/pkgconfig/fftw3l.pc

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libfftw3.a
%{mingw32_libdir}/libfftw3f.a
%{mingw32_libdir}/libfftw3l.a

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libfftw3.a
%{mingw64_libdir}/libfftw3f.a
%{mingw64_libdir}/libfftw3l.a


%changelog
* Sun Jul 1 2012 Tim Mayberry <mojofunk@gmail.com> - 3.2.2-2
- Update to Fedora 17 MinGW package guidelines

* Wed Dec 14 2011 Tim Mayberry <mojofunk@gmail.com> - 3.2.2-1
- Initial mingw-w64 package
