%{?mingw_package_header}

%global native_pkg_name midifilter.lv2

Name:         mingw-%{native_pkg_name}
Version:      0.4.4
Release:      1%{?dist}
Summary:      LV2 plugins to filter midi events
License:      GPLv2+
Group:        System Environment/Libraries
URL:          https://github.com/x42/midifilter.lv2
Source:       https://github.com/x42/midifilter.lv2/archive/midifilter.lv2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

%description
A collection of MIDI data filters in LV2 plugin format by Robin Gareus

%package -n mingw32-%{native_pkg_name}
Summary:        LV2 filters for MIDI data
Group:          Development/Libraries

%description -n mingw32-%{native_pkg_name}
A collection of MIDI data filters in LV2 plugin format by Robin Gareus

%package -n mingw64-%{native_pkg_name}
Summary:        LV2 filters for MIDI data
Group:          Development/Libraries

%description -n mingw64-%{native_pkg_name}
A collection of MIDI data filters in LV2 plugin format by Robin Gareus


# RPM>=4.13 in Fedora>=23 doesn't like an empty debug files list
%global %{?mingw_debug_package} %{nil}


%prep
%setup -q -c %{native_pkg_name}-%{version}

# now copy
for dir in win32 win64; do
	cp -a %{native_pkg_name}-%{version} $dir
done

rm -rf %{native_pkg_name}-%{version}

%build
pushd win32
	export PREFIX=%{mingw32_prefix}
	export XWIN=%{mingw32_host}
	#%{mingw32_env}
	export PKG_CONFIG_LIBDIR=%{mingw32_libdir}/pkgconfig
	%{mingw32_make}
popd

pushd win64
	export PREFIX=%{mingw64_prefix}
	export XWIN=%{mingw64_host}
	#%{mingw64_env}
	export PKG_CONFIG_LIBDIR=%{mingw64_libdir}/pkgconfig
	%{mingw64_make}
popd

%install
pushd win32
	export PREFIX=%{mingw32_prefix}
	export XWIN=%{mingw32_host}
	#%{mingw32_env}
	export PKG_CONFIG_LIBDIR=%{mingw32_libdir}/pkgconfig
	make install DESTDIR=$RPM_BUILD_ROOT
	cp -a AUTHORS README.md COPYING ../
popd

pushd win64
	export PREFIX=%{mingw64_prefix}
	export XWIN=%{mingw64_host}
	#%{mingw64_env}
	export PKG_CONFIG_LIBDIR=%{mingw64_libdir}/pkgconfig
	make install DESTDIR=$RPM_BUILD_ROOT
popd


%files -n mingw32-%{native_pkg_name}
%doc AUTHORS COPYING README.md
%{mingw32_libdir}/lv2/midifilter.lv2/midifilter.dll
%{mingw32_libdir}/lv2/midifilter.lv2/manifest.ttl
%{mingw32_libdir}/lv2/midifilter.lv2/midifilter.ttl
%{mingw32_libdir}/lv2/midifilter.lv2/presets.ttl

%files -n mingw64-%{native_pkg_name}
%doc AUTHORS COPYING README.md
%{mingw64_libdir}/lv2/midifilter.lv2/midifilter.dll
%{mingw64_libdir}/lv2/midifilter.lv2/manifest.ttl
%{mingw64_libdir}/lv2/midifilter.lv2/midifilter.ttl
%{mingw64_libdir}/lv2/midifilter.lv2/presets.ttl

%changelog
* Mon Aug 8 2016 Tim Mayberry <mojofunk@gmail.com> - 0.4.4-1
- Update to version 0.4.4
- Rebuild for Fedora 24

* Thu May 21 2015 Tim Mayberry <mojofunk@gmail.com> - 0.3.2-1
- Initial mingw version for Fedora 21
