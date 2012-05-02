%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

Name:           mingw32-libgnomecanvasmm26
Version:        2.26.0
Release:        1%{?dist}

Summary:        C++ interface for Gnome libs (a GUI library for X)

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgnomecanvasmm/2.22/libgnomecanvasmm-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gtkmm24
BuildRequires:  mingw32-libgnomecanvas
BuildRequires:  pkgconfig

Requires:       pkgconfig

%description
This package provides a C++ interface for GnomeUI.  It is a subpackage
of the gnomemm project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%description
This package contains the headers that programmers will need to
develop applications which will use libgnomecanvasmm, part of gnomemm
- the C++ interface to the GTK+ GUI library.

%package static
Summary:        Static version of the MinGW Windows libgnomecanvasmm library
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the MinGW Windows libgnomecanvasmm library.


%{?_mingw32_debug_package}


%prep
%setup -q -n libgnomecanvasmm-%{version}


%build
%{_mingw32_configure} --enable-static --enable-shared
%{_mingw32_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%{_mingw32_make} DESTDIR=${RPM_BUILD_ROOT} install

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.m4" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_mingw32_bindir}/libgnomecanvasmm-*.dll
%{_mingw32_libdir}/libgnomecanvasmm-2.6.dll.a
%{_mingw32_libdir}/libgnomecanvasmm-2.6
%{_mingw32_libdir}/pkgconfig/*.pc
%{_mingw32_includedir}/libgnomecanvasmm-2.6

%files static
%defattr(-,root,root,-)
%{_mingw32_libdir}/libgnomecanvasmm-2.6.a

%changelog
* Wed Feb 24 2011 Tim Mayberry <mojofunk@gmail.com>
- Initial MinGW build of libgnomecanvasmm
