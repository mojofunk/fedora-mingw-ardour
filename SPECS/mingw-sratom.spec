%{?mingw_package_header}

%global native_pkg_name sratom

%global maj 0

Name:           mingw-%{native_pkg_name}
Version:        0.4.6
Release:        1%{?dist}
Summary:        A C library for serializing LV2 plugins

Group:          System Environment/Libraries
License:        MIT
URL:            http://drobilla.net/software/sratom/
Source0:        http://download.drobilla.net/sratom-%{version}.tar.bz2

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils
BuildRequires: mingw32-lv2 >= 0.12.0
BuildRequires: mingw64-lv2 >= 0.12.0
BuildRequires: mingw32-sord
BuildRequires: mingw64-sord

#BuildRequires:  doxygen
#BuildRequires:  graphviz
#BuildRequires:  glib2-devel
BuildRequires:  python

BuildRequires:  pkgconfig

BuildArch: noarch


%description
%{name} is a new C library for serializing LV2 atoms to/from Turtle. It is 
intended to be a full serialization solution for LV2 atoms, allowing 
implementations to serialize binary atoms to strings and read them back again. 
This is particularly useful for saving plugin state, or implementing plugin 
control with network transparency.

%package -n mingw32-%{native_pkg_name}
Summary:        Development libraries and headers for %{name}
Group:          Development/Libraries

%description -n mingw32-%{native_pkg_name}
%{name} is a new C library for serializing LV2 atoms to/from Turtle.

This package contains the headers and development libraries for %{name}.

%package -n mingw64-%{native_pkg_name}
Summary:        Development libraries and headers for %{name}
Group:          Development/Libraries

%description -n mingw64-%{native_pkg_name}
%{name} is a new C library for serializing LV2 atoms to/from Turtle.

This package contains the headers and development libraries for %{name}.


%{?mingw_debug_package}


%prep
%setup -q -c sratom-%{version}

for dir in win32 win64; do
	cp -a sratom-%{version} $dir
done
rm -rf sratom-%{version}

%build

pushd win32
	export PREFIX=%{mingw32_prefix}
	%{mingw32_env}
	./waf configure
	./waf build -v %{?_smp_mflags}
popd

pushd win64
	export PREFIX=%{mingw64_prefix}
	%{mingw64_env}
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

mkdir %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw32_libdir}/sratom*.dll* %{buildroot}%{mingw32_bindir}
mkdir %{buildroot}%{mingw64_bindir}
mv %{buildroot}%{mingw64_libdir}/sratom*.dll* %{buildroot}%{mingw64_bindir}


%files -n mingw32-%{native_pkg_name}
%doc NEWS README COPYING
%{mingw32_bindir}/sratom-%{maj}-0.dll
%{mingw32_libdir}/libsratom-%{maj}.dll.a
%{mingw32_libdir}/pkgconfig/sratom*.pc
%{mingw32_includedir}/sratom-%{maj}/

%files -n mingw64-%{native_pkg_name}
%doc NEWS README COPYING
%{mingw64_bindir}/sratom-%{maj}-0.dll
%{mingw64_libdir}/libsratom-%{maj}.dll.a
%{mingw64_libdir}/pkgconfig/sratom*.pc
%{mingw64_includedir}/sratom-%{maj}/

%changelog
* Fri Oct 23 2015 Tim Mayberry <mojofunk@gmail.com> - 0.4.6-1
- Update to version 0.4.6

* Sun May 4 2014 Tim Mayberry <mojofunk@gmail.com> - 0.4.4-1
- Initial mingw-w64 package
