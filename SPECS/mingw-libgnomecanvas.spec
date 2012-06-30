%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name libgnomecanvas

%define gettext_package libgnomecanvas-2.0


Summary:       GnomeCanvas widget
Name:          mingw-libgnomecanvas
Version:       2.30.3
Release:       2%{?dist}
URL:           http://www.gnome.org/
Source0:       http://download.gnome.org/sources/libgnomecanvas/2.30/libgnomecanvas-%{version}.tar.bz2
License:       LGPLv2+
Group:         System Environment/Libraries

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: mingw32-gtk2
BuildRequires: mingw64-gtk2
BuildRequires: mingw32-libart_lgpl
BuildRequires: mingw64-libart_lgpl
BuildRequires: mingw32-libglade2
BuildRequires: mingw64-libglade2
#BuildRequires:  intltool
#BuildRequires: gail
#BuildRequires: libtool gettext
BuildRequires:  pkgconfig

Requires: pkgconfig

BuildArch:      noarch


%description
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static version of the MinGW libgnomecanvas
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static version of the MinGW libgnomecanvas library.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static version of the MinGW libgnomecanvas
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static version of the MinGW libgnomecanvas library.


%{?mingw_debug_package}


%prep
%setup -q -n %{mingw_pkg_name}-%{version}

%build
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw32_cache}
%mingw_configure --disable-gtk-doc --enable-shared --enable-static

%mingw_make %{?_smp_mflags}

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# no .la, please
find $RPM_BUILD_ROOT%{mingw32_libdir} -name '*.la' -delete
find $RPM_BUILD_ROOT%{mingw64_libdir} -name '*.la' -delete

%mingw_find_lang %{gettext_package} --all-name


%files -n mingw32-%{mingw_pkg_name} -f mingw32-%{gettext_package}.lang 
%doc COPYING.LIB AUTHORS NEWS README
%{mingw32_bindir}/libgnomecanvas-2-0.dll
%{mingw32_libdir}/libgnomecanvas-2.dll.a
%{mingw32_libdir}/pkgconfig/libgnomecanvas-2.0.pc
%{mingw32_datadir}/gtk-doc/html/libgnomecanvas
%{mingw32_includedir}/libgnomecanvas-2.0/libgnomecanvas

%files -n mingw64-%{mingw_pkg_name} -f mingw64-%{gettext_package}.lang 
%doc COPYING.LIB AUTHORS NEWS README
%{mingw64_bindir}/libgnomecanvas-2-0.dll
%{mingw64_libdir}/libgnomecanvas-2.dll.a
%{mingw64_libdir}/pkgconfig/libgnomecanvas-2.0.pc
%{mingw64_datadir}/gtk-doc/html/libgnomecanvas
%{mingw64_includedir}/libgnomecanvas-2.0/libgnomecanvas

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libgnomecanvas-2.a

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libgnomecanvas-2.a


%changelog
* Sat Jun 30 2012 Tim Mayberry <mojofunk@gmail.com> - 2.20.3-2
- Update spec to Fedora 17 MinGW package guidelines

* Wed Dec 14 2011 Tim Mayberry <mojofunk@gmail.com> - 2.20.3-1
- Initial mingw-w64 package
