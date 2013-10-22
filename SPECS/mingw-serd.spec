%{?mingw_package_header}

#%global mingw_build_win32 1
#%global mingw_build_win64 1

%global mingw_pkg_name serd

%global maj 0

Name:           mingw-serd
Version:        0.18.2
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

%package -n mingw32-%{mingw_pkg_name}
Summary:        Development libraries and headers for %{name}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
%{name} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle and NTriples.

This package contains the headers and development libraries for %{name}.

%package -n mingw64-%{mingw_pkg_name}
Summary:        Development libraries and headers for %{name}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
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
	#%{mingw32_env}
	./waf configure
	./waf build -v %{?_smp_mflags}
popd

pushd win64
	export PREFIX=%{mingw64_prefix}
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


%files -n mingw32-%{mingw_pkg_name}
%doc AUTHORS NEWS README COPYING
%{mingw32_bindir}/serd-%{maj}-0.dll
%{mingw32_bindir}/serdi.exe
%{mingw32_libdir}/libserd-%{maj}.dll.a
%{mingw32_libdir}/pkgconfig/serd*.pc
%{mingw32_includedir}/serd-%{maj}/

%files -n mingw64-%{mingw_pkg_name}
%doc AUTHORS NEWS README COPYING
%{mingw64_bindir}/serd-%{maj}-0.dll
%{mingw64_bindir}/serdi.exe
%{mingw64_libdir}/libserd-%{maj}.dll.a
%{mingw64_libdir}/pkgconfig/serd*.pc
%{mingw64_includedir}/serd-%{maj}/

%changelog
* Tue Oct 22 2013 Tim Mayberry <mojofunk@gmail.com> - 0.18.2-1
- Initial mingw-w64 package
