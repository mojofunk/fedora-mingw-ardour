%{?mingw_package_header}

%global native_pkg_name aubio

Name:           mingw-%{native_pkg_name}
Version:        0.4.2
Release:        1%{?dist}
Summary:        An API for audio analysis and extracting annotations from audio signals

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://aubio.org/
Source0:        http://aubio.org/pub/aubio-%{version}.tar.bz2

BuildRequires:  mingw32-libsndfile
BuildRequires:  mingw64-libsndfile

BuildRequires:  mingw32-libsamplerate
BuildRequires:  mingw64-libsamplerate

# must be some others missing here?

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: wine
BuildRequires: python
BuildRequires: pkgconfig

BuildArch:     noarch


%description
aubio is a library for audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch
detection, tapping the beat and producing midi streams from live
audio. The name aubio comes from 'audio' with a typo: several
transcription errors are likely to be found in the results too.

The aim of this project is to provide these automatic labelling
features to other audio softwares. Functions can be used offline in
sound editors and software samplers, or online in audio effects and
virtual instruments.

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

	./waf configure --disable-jack --with-target-platform=win32

	./waf build %{?_smp_mflags} -v
popd

pushd win64
	export PREFIX=%{mingw64_prefix}

	#%{mingw64_env}
	#export PKG_CONFIG_PREFIX=$MINGW_ROOT
	export PKG_CONFIG_LIBDIR=%{mingw64_libdir}/pkgconfig

	./waf configure --disable-jack --with-target-platform=win64

	./waf build %{?_smp_mflags} -v
popd

%install

pushd win32
	./waf --destdir=$RPM_BUILD_ROOT install
	cp -ar COPYING README.md ../
popd

rm -rf ${RPM_BUILD_ROOT}/%{mingw32_docdir}

pushd win64
	./waf --destdir=$RPM_BUILD_ROOT install
	cp -ar COPYING README.md ../
popd

rm -rf ${RPM_BUILD_ROOT}/%{mingw64_docdir}

%files -n mingw32-%{native_pkg_name}
%doc COPYING README.md
%{mingw32_bindir}/aubiomfcc.exe
%{mingw32_bindir}/aubionotes.exe
%{mingw32_bindir}/aubioonset.exe
%{mingw32_bindir}/aubiopitch.exe
%{mingw32_bindir}/aubioquiet.exe
%{mingw32_bindir}/aubiotrack.exe
%{mingw32_bindir}/libaubio-4.dll
%{mingw32_includedir}/aubio
%{mingw32_libdir}/libaubio*dll.a
%{mingw32_libdir}/pkgconfig/aubio.pc

%files -n mingw64-%{native_pkg_name}
%doc COPYING README.md
%{mingw64_bindir}/aubiomfcc.exe
%{mingw64_bindir}/aubionotes.exe
%{mingw64_bindir}/aubioonset.exe
%{mingw64_bindir}/aubiopitch.exe
%{mingw64_bindir}/aubioquiet.exe
%{mingw64_bindir}/aubiotrack.exe
%{mingw64_bindir}/libaubio-4.dll
%{mingw64_includedir}/aubio
%{mingw64_libdir}/libaubio*dll.a
%{mingw64_libdir}/pkgconfig/aubio.pc

%changelog
* Sat Aug 6 2016 Tim Mayberry <mojofunk@gmail.com> - 0.4.2-1
- Update to version 0.4.2
- No longer need to move dll into bin after waf update/upgrade
- Build now seems to require wine, not just wine-core to execute tests?

* Thu May 8 2014 Tim Mayberry <mojofunk@gmail.com> - 0.4.1-2
- Disable support for jack as causes build failure
- Add missing mingw-libsamplerate dependences
- Add wine-core dependency needed to run unit tests
- use _smp_mflags

* Wed Apr 23 2014 Tim Mayberry <mojofunk@gmail.com> - 0.4.1-1
- Initial mingw package of Aubio 0.4.1
