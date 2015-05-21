%{?mingw_package_header}

%global native_pkg_name midifilter.lv2

Name:         mingw-%{native_pkg_name}
Version:      0.3.2
Release:      1%{?dist}
Summary:      LV2 plugins to filter midi events
License:      GPLv2+
Group:        System Environment/Libraries
URL:          https://github.com/x42/midifilter.lv2
#             This is version 68d3859f826d1
Source0:      https://github.com/x42/midifilter.lv2/archive/midifilter.lv2-0.3.2.zip

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


%{?mingw_debug_package}


%prep
%setup -q -c %{native_pkg_name}-%{version}

# now copy
for dir in win32 win64; do
	cp -a %{native_pkg_name}-%{version} $dir
done

rm -rf %{native_pkg_name}-%{version}

%build
pushd win32
	export XWIN=%{mingw32_host}
	%{mingw32_make}
popd

pushd win64
	export XWIN=%{mingw64_host}
	%{mingw64_make}
popd

%install
pushd win32
	export PREFIX=%{mingw32_prefix}
	export XWIN=%{mingw32_host}
	make install DESTDIR=$RPM_BUILD_ROOT
	cp -a AUTHORS ChangeLog README.md COPYING ../
popd

pushd win64
	export PREFIX=%{mingw64_prefix}
	export XWIN=%{mingw64_host}
	make install DESTDIR=$RPM_BUILD_ROOT
popd


%files -n mingw32-%{native_pkg_name}
%doc AUTHORS ChangeLog COPYING README.md
%{mingw32_libdir}/lv2/midifilter.lv2/midifilter.dll
%{mingw32_libdir}/lv2/midifilter.lv2/manifest.ttl
%{mingw32_libdir}/lv2/midifilter.lv2/midifilter.ttl
%{mingw32_libdir}/lv2/midifilter.lv2/presets.ttl

%files -n mingw64-%{native_pkg_name}
%doc AUTHORS ChangeLog COPYING README.md
%{mingw64_libdir}/lv2/midifilter.lv2/midifilter.dll
%{mingw64_libdir}/lv2/midifilter.lv2/manifest.ttl
%{mingw64_libdir}/lv2/midifilter.lv2/midifilter.ttl
%{mingw64_libdir}/lv2/midifilter.lv2/presets.ttl

%changelog
* Thu May 21 2015 Tim Mayberry <mojofunk@gmail.com> - 0.3.2-1
- Initial mingw version for Fedora 21
