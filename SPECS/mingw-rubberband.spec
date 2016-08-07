%{?mingw_package_header}

%global native_pkg_name rubberband

%global mingw_build_win32 1
%global mingw_build_win64 1

Name:           mingw-%{native_pkg_name}
Version:        1.8.1
Release:        2%{?dist}
Summary:        Audio time-stretching and pitch-shifting library

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.breakfastquay.com/rubberband/
Source0:        http://code.breakfastquay.com/attachments/download/34/rubberband-1.8.1.tar.bz2
Source1:        rubberband-waf
Source2:        rubberband-wscript

BuildArch:      noarch

BuildRequires:  mingw32-fftw
BuildRequires:  mingw64-fftw

BuildRequires:  mingw32-libsndfile
BuildRequires:  mingw64-libsndfile

BuildRequires:  mingw32-libsamplerate
BuildRequires:  mingw64-libsamplerate

BuildRequires:  mingw32-vamp-plugin-sdk
BuildRequires:  mingw64-vamp-plugin-sdk

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  python
BuildRequires:  pkgconfig

#Requires:

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another. 

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

	./waf configure

	./waf build -j1 -v
popd

pushd win64
	export PREFIX=%{mingw64_prefix}

	#%{mingw64_env}
	#export PKG_CONFIG_PREFIX=$MINGW_ROOT
	export PKG_CONFIG_LIBDIR=%{mingw64_libdir}/pkgconfig

	./waf configure

	./waf build -j1 -v
popd

%install

pushd win32
	./waf --destdir=$RPM_BUILD_ROOT install
	cp -ar COPYING README.txt ../
	mv $RPM_BUILD_ROOT/%{mingw32_prefix}/bin/*.dll.a $RPM_BUILD_ROOT/%{mingw32_prefix}/lib
popd

pushd win64
	./waf --destdir=$RPM_BUILD_ROOT install
	cp -ar COPYING README.txt ../
	mv $RPM_BUILD_ROOT/%{mingw64_prefix}/bin/*.dll.a $RPM_BUILD_ROOT/%{mingw64_prefix}/lib
popd

%files -n mingw32-%{native_pkg_name}
%doc COPYING README.txt
%{mingw32_includedir}/rubberband/*.h
%{mingw32_bindir}/rubberband-2.dll
%{mingw32_libdir}/librubberband*dll.a
%{mingw32_libdir}/pkgconfig/rubberband.pc

%files -n mingw64-%{native_pkg_name}
%doc COPYING README.txt
%{mingw64_includedir}/rubberband/*.h
%{mingw64_bindir}/rubberband-2.dll
%{mingw64_libdir}/librubberband*dll.a
%{mingw64_libdir}/pkgconfig/rubberband.pc

%changelog
* Sat Aug 6 2016 Tim Mayberry <mojofunk@gmail.com> - 1.8.1-2
- Rebuild for Fedora 24

* Wed Apr 23 2014 Tim Mayberry <mojofunk@gmail.com> - 1.8.1-1
- Initial mingw package of 1.8.1 using waf build system
