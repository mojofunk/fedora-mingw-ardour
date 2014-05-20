%{?mingw_package_header}

%global native_pkg_name portaudio

%global mingw_build_win32 1
%global mingw_build_win64 1

Name:           mingw-%{native_pkg_name}
Version:        2.0
Release:        4%{?dist}
Summary:        Free, cross platform, open-source, audio I/O library
Group:          System Environment/Libraries
License:        MIT
URL:            http://www.portaudio.com/
# package created from svn rev 1928 using waf dist
Source0:        portaudio-2.0.tar.bz2
Source1:        portaudio-2.0-waf
Source2:        portaudio-2.0-wscript

BuildArch:     noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: python
BuildRequires: pkgconfig

#Requires:

%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

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
%setup -q -c %{native_pkg_name}-%{version}

pushd %{native_pkg_name}-%{version}
	cp %{SOURCE1} waf
	cp %{SOURCE2} wscript
popd

for dir in win32 win64; do
	cp -a %{native_pkg_name}-%{version} $dir
done
rm -rf %{native_pkg_name}-%{version}

%build

pushd win32
	export PREFIX=%{mingw32_prefix}

	#%{mingw32_env}
	#export PKG_CONFIG_PREFIX=$MINGW_ROOT
	export PKG_CONFIG_LIBDIR=%{mingw32_libdir}/pkgconfig

	./waf configure --with-directx --with-tests --with-examples

	./waf build %{?_smp_mflags} -v
popd

pushd win64
	export PREFIX=%{mingw64_prefix}

	#%{mingw64_env}
	#export PKG_CONFIG_PREFIX=$MINGW_ROOT
	export PKG_CONFIG_LIBDIR=%{mingw64_libdir}/pkgconfig

	./waf configure --with-directx --with-tests --with-examples

	./waf build %{?_smp_mflags} -v
popd

%install

pushd win32
	./waf --destdir=$RPM_BUILD_ROOT install
	cp -ar LICENSE.txt README.txt ../
	mv $RPM_BUILD_ROOT/%{mingw32_prefix}/bin/*.dll.a $RPM_BUILD_ROOT/%{mingw32_prefix}/lib
popd

pushd win64
	./waf --destdir=$RPM_BUILD_ROOT install
	cp -ar LICENSE.txt README.txt ../
	mv $RPM_BUILD_ROOT/%{mingw64_prefix}/bin/*.dll.a $RPM_BUILD_ROOT/%{mingw64_prefix}/lib
popd

%files -n mingw32-%{native_pkg_name}
%doc LICENSE.txt README.txt
%{mingw32_includedir}/portaudio.h
%{mingw32_includedir}/pa_win_ds.h
%{mingw32_bindir}/portaudio-2.dll
%{mingw32_bindir}/pa_devs.exe
%{mingw32_bindir}/patest1.exe
%{mingw32_bindir}/patest_longsine.exe
%{mingw32_libdir}/libportaudio*dll.a
%{mingw32_libdir}/pkgconfig/portaudio-2.0.pc

%files -n mingw64-%{native_pkg_name}
%doc LICENSE.txt README.txt
%{mingw64_includedir}/portaudio.h
%{mingw64_includedir}/pa_win_ds.h
%{mingw64_bindir}/portaudio-2.dll
%{mingw64_bindir}/pa_devs.exe
%{mingw64_bindir}/patest1.exe
%{mingw64_bindir}/patest_longsine.exe
%{mingw64_libdir}/libportaudio*dll.a
%{mingw64_libdir}/pkgconfig/portaudio-2.0.pc

%changelog
* Thu May 15 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-4
- Add directx backend to build

* Thu May 15 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-3
- Add tests and examples to build

* Thu Apr 24 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-2
- Fix portaudio header install path

* Wed Apr 23 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-1
- Initial mingw package of 2.0(svn@1928) using waf build system
