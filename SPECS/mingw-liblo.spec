%{?mingw_package_header}

%global mingw_pkg_name liblo

Name:         mingw-liblo
Version:      0.27
Release:      1%{?dist}
Summary:      Open Sound Control library
License:      LGPLv2+
Group:        System Environment/Libraries
URL:          http://liblo.sourceforge.net
Source0:      http://download.sf.net/sourceforge/liblo/liblo-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires: doxygen

%description
liblo is an implementation of the Open Sound Control protocol for
POSIX systems developed by Steve Harris.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Summary:        Libraries, includes, etc to develop liblo applications
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
liblo is an implementation of the Open Sound Control protocol for
POSIX systems developed by Steve Harris.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the Liblo library
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static cross compiled version of the Liblo library.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Summary:        Libraries, includes, etc to develop liblo applications
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
liblo is an implementation of the Open Sound Control protocol for
POSIX systems developed by Steve Harris.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the Liblo library
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static cross compiled version of the Liblo library.


%{?mingw_debug_package}


%prep
%setup -q -n liblo-%{version}


%build
%mingw_configure --enable-shared --enable-static

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# remove libtool archives
find $RPM_BUILD_ROOT%{mingw32_libdir} -name '*.la' -delete
find $RPM_BUILD_ROOT%{mingw64_libdir} -name '*.la' -delete


%files -n mingw32-%{mingw_pkg_name}
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{mingw32_bindir}/liblo-7.dll
%{mingw32_bindir}/oscdump.exe
%{mingw32_bindir}/oscsend.exe
%{mingw32_includedir}/lo
%{mingw32_libdir}/liblo.dll.a
%{mingw32_libdir}/pkgconfig/liblo.pc

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/liblo.a

%files -n mingw64-%{mingw_pkg_name}
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{mingw64_bindir}/liblo-7.dll
%{mingw64_bindir}/oscdump.exe
%{mingw64_bindir}/oscsend.exe
%{mingw64_includedir}/lo
%{mingw64_libdir}/liblo.dll.a
%{mingw64_libdir}/pkgconfig/liblo.pc

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/liblo.a

%changelog
* Wed Jul 17 2013 Tim Mayberry <mojofunk@gmail.com> - 0.27-1
- Initial MinGW version for Fedora 19