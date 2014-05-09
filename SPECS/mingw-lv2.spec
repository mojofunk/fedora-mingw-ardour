%{?mingw_package_header}

%global native_pkg_name lv2

%global maj 0

Name:           mingw-%{native_pkg_name}
Version:        1.8.0
Release:        1%{?dist}
Summary:        A lightweight C library for RDF syntax

# lv2specgen template.html is CC-AT-SA
Group:          System Environment/Libraries
License:        ISC
URL:            http://lv2plug.in
Source:         http://lv2plug.in/spec/lv2-%{version}.tar.bz2

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

#BuildRequires:  doxygen
#BuildRequires:  graphviz
#BuildRequires:  glib2-devel
BuildRequires:  python

BuildRequires:  pkgconfig

BuildArch: noarch


%description
LV2 is a standard for plugins and matching host applications, mainly
targeted at audio processing and generation.  

There are a large number of open source and free software synthesis
packages in use or development at this time. This API ('LV2') attempts
to give programmers the ability to write simple 'plugin' audio
processors in C/C++ and link them dynamically ('plug') into a range of
these packages ('hosts').  It should be possible for any host and any
plugin to communicate completely through this interface.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many hosts have outgrown.


%package -n mingw32-%{native_pkg_name}
Summary:        API for the LV2 Audio Plugin Standard
Group:          Development/Libraries

%description -n mingw32-%{native_pkg_name}
lv2 contains the lv2.h header file and headers for all of the
LV@ specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.


%package -n mingw64-%{native_pkg_name}
Summary:        API for the LV2 Audio Plugin Standard
Group:          Development/Libraries

%description -n mingw64-%{native_pkg_name}
lv2 contains the lv2.h header file and headers for all of the
LV@ specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.


%{?mingw_debug_package}


%prep
%setup -q -c lv2-%{version}

for dir in win32 win64; do
	cp -a lv2-%{version} $dir
done
rm -rf lv2-%{version}

%build

pushd win32
	export PREFIX=%{mingw32_prefix}
	%{mingw32_env}
	./waf configure --no-plugins --copy-headers
	./waf build -v %{?_smp_mflags}
popd

pushd win64
	export PREFIX=%{mingw64_prefix}
	%{mingw64_env}
	./waf configure --no-plugins --copy-headers
	./waf build -v %{?_smp_mflags}
popd

%install
pushd win32
	DESTDIR=%{buildroot} ./waf install
	cp -a NEWS README COPYING ../
popd

pushd win64
	DESTDIR=%{buildroot} ./waf install
popd


%files -n mingw32-%{native_pkg_name}
%doc NEWS README COPYING
%{mingw32_bindir}/lv2specgen.py
%{mingw32_datadir}/lv2specgen
%{mingw32_includedir}/lv2.h
%{mingw32_includedir}/lv2/
%{mingw32_libdir}/lv2/*/*.[hc]
%{mingw32_libdir}/lv2/*/*.ttl
%{mingw32_libdir}/pkgconfig/lv2core.pc
%{mingw32_libdir}/pkgconfig/lv2.pc

%files -n mingw64-%{native_pkg_name}
%doc NEWS README COPYING
%{mingw64_bindir}/lv2specgen.py
%{mingw64_datadir}/lv2specgen
%{mingw64_includedir}/lv2.h
%{mingw64_includedir}/lv2/
%{mingw64_libdir}/lv2/*/*.[hc]
%{mingw64_libdir}/lv2/*/*.ttl
%{mingw64_libdir}/pkgconfig/lv2core.pc
%{mingw64_libdir}/pkgconfig/lv2.pc

%changelog
* Sun May 4 2014 Tim Mayberry <mojofunk@gmail.com> - 1.8.0-1
- Initial mingw version of lv2 
