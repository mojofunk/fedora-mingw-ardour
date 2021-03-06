%{?mingw_package_header}

%global native_pkg_name lilv

%global maj 0

Name:           mingw-%{native_pkg_name}
Version:        0.24.0
Release:        1%{?dist}
Summary:        An LV2 Resource Description Framework Library

Group:          System Environment/Libraries
License:        MIT
URL:            http://drobilla.net/software/lilv/
Source0:        http://download.drobilla.net/lilv-%{version}.tar.bz2

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils
BuildRequires: mingw32-lv2
BuildRequires: mingw64-lv2
BuildRequires: mingw32-sord
BuildRequires: mingw64-sord
BuildRequires: mingw32-sratom
BuildRequires: mingw64-sratom

#BuildRequires:  doxygen
#BuildRequires:  graphviz
#BuildRequires:  glib2-devel
BuildRequires:  python

BuildRequires:  pkgconfig

BuildArch: noarch


%description
%{name} is a library to make the use of LV2 plugins as simple as possible 
for applications. Lilv is the successor to SLV2, rewritten to be significantly 
faster and have minimal dependencies. 

%package -n mingw32-%{native_pkg_name}
Summary:        Development libraries and headers for %{name}
Group:          Development/Libraries

%description -n mingw32-%{native_pkg_name}
%{name} is a library to make the use of LV2 plugins as simple as possible 
for applications.

This package contains the headers and development libraries for %{name}.

%package -n mingw64-%{native_pkg_name}
Summary:        Development libraries and headers for %{name}
Group:          Development/Libraries

%description -n mingw64-%{native_pkg_name}
%{name} is a library to make the use of LV2 plugins as simple as possible 
for applications.

This package contains the headers and development libraries for %{name}.


%{?mingw_debug_package}


%prep
%setup -q -c lilv-%{version}

for dir in win32 win64; do
	cp -a lilv-%{version} $dir
done
rm -rf lilv-%{version}

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
	export PKG_CONFIG_LIBDIR=%{mingw64_libdir}/pkgconfig
	./waf configure
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

# Move dll's to bin directory

mv %{buildroot}%{mingw32_libdir}/lilv*.dll* %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw64_libdir}/lilv*.dll* %{buildroot}%{mingw64_bindir}

# Remove manpages which duplicate those in Fedora native.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# Remove bash completion config
rm -rf $RPM_BUILD_ROOT%{mingw32_sysconfdir}
rm -rf $RPM_BUILD_ROOT%{mingw64_sysconfdir}


%files -n mingw32-%{native_pkg_name}
%doc NEWS README COPYING
%{mingw32_bindir}/lilv-%{maj}.dll
%{mingw32_bindir}/lilv-bench.exe
%{mingw32_bindir}/lv2apply.exe
%{mingw32_bindir}/lv2info.exe
%{mingw32_bindir}/lv2ls.exe
%{mingw32_includedir}/lilv-%{maj}/
%{mingw32_libdir}/liblilv-%{maj}.dll.a
%{mingw32_libdir}/pkgconfig/lilv-%{maj}.pc

%files -n mingw64-%{native_pkg_name}
%doc NEWS README COPYING
%{mingw64_bindir}/lilv-%{maj}.dll
%{mingw64_bindir}/lilv-bench.exe
%{mingw64_bindir}/lv2apply.exe
%{mingw64_bindir}/lv2info.exe
%{mingw64_bindir}/lv2ls.exe
%{mingw64_includedir}/lilv-%{maj}/
%{mingw64_libdir}/liblilv-%{maj}.dll.a
%{mingw64_libdir}/pkgconfig/lilv-%{maj}.pc

%changelog
* Mon Oct 10 2016 Tim Mayberry <mojofunk@gmail.com> - 0.24.0-1
- Update to version 0.24.0
- Add new lv2apply utility to package

* Sun Aug 6 2016 Tim Mayberry <mojofunk@gmail.com> - 0.22.0-2
- Rebuild for Fedora 24

* Fri Oct 23 2015 Tim Mayberry <mojofunk@gmail.com> - 0.22.0-1
- Update to version 0.22.0
- drop patches, both issues fixed

* Sun May 4 2014 Tim Mayberry <mojofunk@gmail.com> - 0.18.0-1
- Initial mingw-w64 package
