%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

%define gettext_package libgnomecanvas-2.0
		
Summary:        GnomeCanvas widget
Name:           mingw32-libgnomecanvas
Version:        2.30.3
Release:        2%{?dist}
URL:            http://www.gnome.org/
Source0:        http://download.gnome.org/sources/libgnomecanvas/2.30/libgnomecanvas-%{version}.tar.bz2
License:        LGPLv2+
Group:          System Environment/Libraries

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw32-gtk2
BuildRequires:  mingw32-libart_lgpl
BuildRequires:  mingw32-libglade2
BuildRequires:  pkgconfig
BuildRequires:  intltool

# for glib-genmarshal
BuildRequires:  glib2-devel

Requires: pkgconfig


%description
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%package static
Summary:        Static version of the MinGW libgnomecanvas
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the MinGW libgnomecanvas library.


%{?_mingw32_debug_package}


%prep
%setup -q -n libgnomecanvas-%{version}

%build
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw32_cache}
%{_mingw32_configure} --disable-gtk-doc --enable-shared --enable-static
%{_mingw32_make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%{_mingw32_makeinstall}

rm -f $RPM_BUILD_ROOT%{_mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_mingw32_libdir}/libglade/2.0/*.la

%find_lang %{gettext_package}

%clean
rm -rf $PRM_BUILD_ROOT

%files -f %{gettext_package}.lang
%defattr(-,root,root,-)
%doc COPYING.LIB AUTHORS NEWS README
%{_mingw32_bindir}/libgnomecanvas-2-0.dll
%{_mingw32_libdir}/libgnomecanvas-2.dll.a
%{_mingw32_libdir}/pkgconfig/libgnomecanvas-2.0.pc
%{_mingw32_datadir}/gtk-doc/html/libgnomecanvas
%{_mingw32_includedir}/libgnomecanvas-2.0/libgnomecanvas

%files static
%defattr(-,root,root,-)
%{_mingw32_libdir}/libgnomecanvas-2.a

%changelog
* Wed Nov 9 2011 Tim Mayberry <mojofunk@gmail.com> 2.30.3-2
- Add missing BR glib2-devel

* Wed Nov 9 2011 Tim Mayberry <mojofunk@gmail.com> 2.30.3-1
- Update to 2.30.3

* Wed Feb 24 2011 Tim Mayberry <mojofunk@gmail.com> 2.30.2-1
- First version of MinGW libgnomecanvas package
