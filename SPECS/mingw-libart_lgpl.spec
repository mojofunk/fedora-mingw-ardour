%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name libart_lgpl

Summary:        Library of graphics routines used by libgnomecanvas
Name:           mingw-libart_lgpl
Version:        2.3.21
Release:        2%{?dist}
URL:            http://www.gnome.org/
Source0:        http://ftp.gnome.org/pub/gnome/sources/libart_lgpl/2.3/libart_lgpl-%{version}.tar.bz2
Patch0:         libart-multilib.patch
License:        LGPLv2+
Group:          System Environment/Libraries 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

BuildArch:      noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils
BuildRequires: pkgconfig 

Requires: pkgconfig


%description
Graphics routines used by the GnomeCanvas widget and some other 
applications. libart renders vector paths and the like.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
Graphics routines used by the GnomeCanvas widget and some other 
applications. libart renders vector paths and the like.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
Graphics routines used by the GnomeCanvas widget and some other 
applications. libart renders vector paths and the like.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static version of the MinGW libart_lgpl
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static version of the MinGW libart_lgpl

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static version of the MinGW libart_lgpl
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static version of the MinGW libart_lgpl


%{?mingw_debug_package}


%prep
%setup -q -n libart_lgpl-%{version}
%patch0 -p1 -b .multilib


%build
%mingw_configure --enable-shared --enable-static

# hack, hack, hack
cp -a libart.def build_win32
cp -a libart.def build_win64

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# no .la, please
find $RPM_BUILD_ROOT%{mingw32_libdir} -name '*.la' -delete
find $RPM_BUILD_ROOT%{mingw64_libdir} -name '*.la' -delete


%files -n mingw32-%{mingw_pkg_name} 
%doc AUTHORS COPYING NEWS README
%{mingw32_bindir}/libart_lgpl_2-2.dll
%{mingw32_bindir}/libart2-config
%{mingw32_libdir}/libart_lgpl_2.dll.a
%{mingw32_libdir}/pkgconfig/libart-2.0.pc
%{mingw32_includedir}/libart-2.0/libart_lgpl

%files -n mingw64-%{mingw_pkg_name} 
%doc AUTHORS COPYING NEWS README
%{mingw64_bindir}/libart_lgpl_2-2.dll
%{mingw64_bindir}/libart2-config
%{mingw64_libdir}/libart_lgpl_2.dll.a
%{mingw64_libdir}/pkgconfig/libart-2.0.pc
%{mingw64_includedir}/libart-2.0/libart_lgpl

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libart_lgpl_2.a

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libart_lgpl_2.a


%changelog
* Sat Jun 30 2012 Tim Mayberry <mojofunk@gmail.com> - 2.3.21-2
- Update spec for Fedora 17 MinGW package guidelines

* Wed Dec 14 2011 Tim Mayberry <mojofunk@gmail.com> - 2.3.21-1
- Initial mingw-w64 package based on native Fedora package
