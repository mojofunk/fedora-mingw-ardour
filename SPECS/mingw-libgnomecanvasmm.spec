%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 0

%global mingw_pkg_name libgnomecanvasmm26

Name:           mingw-libgnomecanvasmm26
Version:        2.26.0
Release:        2%{?dist}

Summary:        C++ interface for Gnome libs (a GUI library for X)

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgnomecanvasmm/2.22/libgnomecanvasmm-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires: mingw32-filesystem >= 82
BuildRequires: mingw64-filesystem >= 82
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: mingw32-gtkmm24
BuildRequires: mingw64-gtkmm24
BuildRequires: mingw32-libgnomecanvas
BuildRequires: mingw64-libgnomecanvas
BuildRequires: pkgconfig

Requires:      pkgconfig


%description
This package provides a C++ interface for GnomeCanvas. Highlights 
include typesafe callbacks, widgets extensible via inheritance and 
a comprehensive set of canvas widget classes that can be freely 
combined to quickly create complex user interfaces.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
This package provides a C++ interface for GnomeCanvas. Highlights 
include typesafe callbacks, widgets extensible via inheritance and 
a comprehensive set of canvas widget classes that can be freely 
combined to quickly create complex user interfaces.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
This package provides a C++ interface for GnomeCanvas. Highlights 
include typesafe callbacks, widgets extensible via inheritance and 
a comprehensive set of canvas widget classes that can be freely 
combined to quickly create complex user interfaces.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the gnomecanvasmm library
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static cross compiled version of the gnomecanvasmm library.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the gnomecanvasmm library
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static cross compiled version of the gnomecanvasmm library.


%{?mingw_debug_package}


%prep
%setup -q -n libgnomecanvasmm-%{version}


%build
%mingw_configure --enable-static --enable-shared
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=${RPM_BUILD_ROOT}

# no .la, please
find $RPM_BUILD_ROOT%{mingw32_libdir} -name '*.la' -delete
#find $RPM_BUILD_ROOT%{mingw64_libdir} -name '*.la' -delete


%files -n mingw32-%{mingw_pkg_name}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{mingw32_bindir}/libgnomecanvasmm-*.dll
%{mingw32_libdir}/libgnomecanvasmm-2.6.dll.a
%{mingw32_libdir}/libgnomecanvasmm-2.6
%{mingw32_libdir}/pkgconfig/*.pc
%{mingw32_includedir}/libgnomecanvasmm-2.6

#%files -n mingw64-%{mingw_pkg_name}
#%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
#%{mingw64_bindir}/libgnomecanvasmm-*.dll
#%{mingw64_libdir}/libgnomecanvasmm-2.6.dll.a
#%{mingw64_libdir}/libgnomecanvasmm-2.6
#%{mingw64_libdir}/pkgconfig/*.pc
#%{mingw64_includedir}/libgnomecanvasmm-2.6

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libgnomecanvasmm-2.6.a

#%files -n mingw64-%{mingw_pkg_name}-static
#%{mingw64_libdir}/libgnomecanvasmm-2.6.a


%changelog
* Sat Jun 30 2012 Tim Mayberry <mojofunk@gmail.com> - 2.26.0-2
- Update spec to Fedora 17 MinGW package guidelines
- Disable 64 bit build due to link errors

* Thu Dec 15 2011 Tim Mayberry <mojofunk@gmail.com> - 2.26.0-1
- Initial mingw-w64 package
