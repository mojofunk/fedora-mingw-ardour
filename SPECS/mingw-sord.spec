%{?mingw_package_header}

#%global mingw_build_win32 1
#%global mingw_build_win64 1

%global native_pkg_name sord

%global maj 0

Name:       mingw-%{native_pkg_name}
Version:    0.14.0
Release:    1%{?dist}
Summary:    A lightweight Resource Description Framework (RDF) C library

Group:      System Environment/Libraries
License:    ISC
URL:        http://drobilla.net/software/sord/
Source0:    http://download.drobilla.net/sord-%{version}.tar.bz2

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils
BuildRequires: mingw32-pcre
BuildRequires: mingw64-pcre
BuildRequires: mingw32-serd >= 0.22.0
BuildRequires: mingw64-serd >= 0.22.0

#BuildRequires: boost-devel
#BuildRequires: doxygen
#BuildRequires: graphviz
#BuildRequires: glib2-devel
BuildRequires: python

BuildRequires:  pkgconfig

BuildArch: noarch


%description
%{name} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory. %{name} and parent library serd form 
a lightweight RDF tool-set for resource limited or performance critical 
applications.

%package -n mingw32-%{native_pkg_name}
Summary:    Development libraries and headers for %{name}
Group:      Development/Libraries

%description -n mingw32-%{native_pkg_name}
%{name} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory.

This package contains the headers and development libraries for %{name}.

%package -n mingw64-%{native_pkg_name}
Summary:    Development libraries and headers for %{name}
Group:      Development/Libraries

%description -n mingw64-%{native_pkg_name}
%{name} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory.

This package contains the headers and development libraries for %{name}.


%{?mingw_debug_package}


%prep
%setup -q -c sord-%{version}

for dir in win32 win64; do
	cp -a sord-%{version} $dir
done
rm -rf sord-%{version}

%build

pushd win32
	export PREFIX=%{mingw32_prefix}
	%{mingw32_env}
	export PKG_CONFIG_LIBDIR=%{mingw32_libdir}/pkgconfig
	./waf configure
	./waf build -v %{?_smp_mflags}
popd

pushd win64
	export PREFIX=%{mingw64_prefix}
	%{mingw64_env}
	export PKG_CONFIG_LIBDIR=%{mingw32_libdir}/pkgconfig
	./waf configure
	./waf build -v %{?_smp_mflags}
popd

%install

pushd win32
	DESTDIR=%{buildroot} ./waf install
	cp -a AUTHORS NEWS README COPYING ../
popd

pushd win64
	DESTDIR=%{buildroot} ./waf install
popd

# Move dll's to bin directory

mv %{buildroot}%{mingw32_libdir}/sord*.dll %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw64_libdir}/sord*.dll %{buildroot}%{mingw64_bindir}

# Delete man page

rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

%files -n mingw32-%{native_pkg_name}
%doc AUTHORS NEWS README COPYING
%{mingw32_bindir}/sord-%{maj}.dll
%{mingw32_bindir}/sordi.exe
%{mingw32_bindir}/sord_validate.exe
%{mingw32_libdir}/libsord-%{maj}.dll.a
%{mingw32_libdir}/pkgconfig/sord*.pc
%{mingw32_includedir}/sord-%{maj}/

%files -n mingw64-%{native_pkg_name}
%doc AUTHORS NEWS README COPYING
%{mingw64_bindir}/sord-%{maj}.dll
%{mingw64_bindir}/sordi.exe
%{mingw64_bindir}/sord_validate.exe
%{mingw64_libdir}/libsord-%{maj}.dll.a
%{mingw64_libdir}/pkgconfig/sord*.pc
%{mingw64_includedir}/sord-%{maj}/

%changelog
* Fri Oct 23 2015 Tim Mayberry <mojofunk@gmail.com> - 0.14.0-1
- Update to version 0.14.0
- Added pcre to BuildRequires to build sord_validate utility

* Wed Oct 23 2013 Tim Mayberry <mojofunk@gmail.com> - 0.12.0-1
- Initial mingw-w64 package
