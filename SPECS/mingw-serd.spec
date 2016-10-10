%{?mingw_package_header}

%global native_pkg_name serd

%global maj 0

Name:           mingw-%{native_pkg_name}
Version:        0.24.0
Release:        1%{?dist}
Summary:        A lightweight C library for RDF syntax

Group:          System Environment/Libraries
License:        ISC
URL:            http://drobilla.net/software/serd/
Source0:        http://download.drobilla.net/serd-%{version}.tar.bz2

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
%{name} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle and NTriples.

Serd is not intended to be a swiss-army knife of RDF syntax, but rather is 
suited to resource limited or performance critical applications (e.g. 
converting many gigabytes of NTriples to Turtle), or situations where a 
simple reader/writer with minimal dependencies is ideal (e.g. in LV2 
implementations or embedded applications).is a library to make the use of 
LV2 plugins as simple as possible for applications. 

%package -n mingw32-%{native_pkg_name}
Summary:        Development libraries and headers for %{name}
Group:          Development/Libraries

%description -n mingw32-%{native_pkg_name}
%{name} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle and NTriples.

This package contains the headers and development libraries for %{name}.

%package -n mingw64-%{native_pkg_name}
Summary:        Development libraries and headers for %{name}
Group:          Development/Libraries

%description -n mingw64-%{native_pkg_name}
%{name} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle and NTriples.

This package contains the headers and development libraries for %{name}.


%{?mingw_debug_package}


%prep
%setup -q -c serd-%{version}

for dir in win32 win64; do
	cp -a serd-%{version} $dir
done
rm -rf serd-%{version}

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
	cp -a AUTHORS NEWS README COPYING ../
popd

pushd win64
	DESTDIR=%{buildroot} ./waf install
popd

# Move dll's to bin directory

mv %{buildroot}%{mingw32_libdir}/serd*.dll %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw64_libdir}/serd*.dll %{buildroot}%{mingw64_bindir}

# Delete man page

rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}


%files -n mingw32-%{native_pkg_name}
%doc AUTHORS NEWS README COPYING
%{mingw32_bindir}/serd-%{maj}.dll
%{mingw32_bindir}/serdi.exe
%{mingw32_libdir}/libserd-%{maj}.dll.a
%{mingw32_libdir}/pkgconfig/serd*.pc
%{mingw32_includedir}/serd-%{maj}/

%files -n mingw64-%{native_pkg_name}
%doc AUTHORS NEWS README COPYING
%{mingw64_bindir}/serd-%{maj}.dll
%{mingw64_bindir}/serdi.exe
%{mingw64_libdir}/libserd-%{maj}.dll.a
%{mingw64_libdir}/pkgconfig/serd*.pc
%{mingw64_includedir}/serd-%{maj}/

%changelog
* Mon Oct 10 2016 Tim Mayberry <mojofunk@gmail.com> - 0.24.0-1
- Update to version 0.24.0

* Fri Oct 23 2015 Tim Mayberry <mojofunk@gmail.com> - 0.22.0-1
- Update to version 0.22.0

* Sun May 4 2014 Tim Mayberry <mojofunk@gmail.com> - 0.18.2-2
- Tweaks to spec file

* Tue Oct 22 2013 Tim Mayberry <mojofunk@gmail.com> - 0.18.2-1
- Initial mingw-w64 package
