%{?mingw_package_header}

%global native_pkg_name libltc

%global mingw_build_win32 1
%global mingw_build_win64 1

Name:       mingw-%{native_pkg_name}
Version:    1.1.4
Release:    1%{?dist}
Summary:    Linear/Longitudinal Time Code (LTC) Library

Group:      System Environment/Libraries
License:    LGPLv3+
URL:        http://x42.github.io/libltc/
Source0:    https://github.com/x42/%{name}/releases/download/v%{version}/libltc-%{version}.tar.gz

BuildArch:     noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: python
BuildRequires: pkgconfig

%description
Linear (or Longitudinal) Timecode (LTC) is an encoding of time code data as a
Manchester-Biphase encoded audio signal. The audio signal is commonly recorded
on a VTR track or other storage media.

libltc provides functionality to encode and decode LTC from/to time code,
including SMPTE date support.

%package -n mingw32-%{native_pkg_name}
Summary:        Development files for %{name}
Group:          Development/Libraries

%description -n mingw32-%{native_pkg_name}
The %{name} package contains libraries and header files for
developing applications that use %{name}.

%package -n mingw64-%{native_pkg_name}
Summary:        Development files for %{name}
Group:          Development/Libraries

%description -n mingw64-%{native_pkg_name}
The %{name} package contains libraries and header files for
developing applications that use %{name}.


%{?mingw_debug_package}


%prep
%setup -q -n %{native_pkg_name}-%{version}


%build
%mingw_configure --disable-static --disable-doxygen

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Remove the .la files
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# Don't duplicate docs in the native package
rm -rf ${RPM_BUILD_ROOT}%{mingw32_mandir}
rm -rf ${RPM_BUILD_ROOT}%{mingw64_mandir}


%files -n mingw32-%{native_pkg_name}
%doc AUTHORS ChangeLog COPYING README.md
%{mingw32_bindir}/libltc-11.dll
%{mingw32_includedir}/ltc.h
%{mingw32_libdir}/libltc.dll.a
%{mingw32_libdir}/pkgconfig/ltc.pc

%files -n mingw64-%{native_pkg_name}
%doc AUTHORS ChangeLog COPYING README.md
%{mingw64_bindir}/libltc-11.dll
%{mingw64_includedir}/ltc.h
%{mingw64_libdir}/libltc.dll.a
%{mingw64_libdir}/pkgconfig/ltc.pc

%changelog
* Thu Feb 19 2015 Tim Mayberry <mojofunk@gmail.com> - 1.1.4-1
- Initial mingw-w64 package
