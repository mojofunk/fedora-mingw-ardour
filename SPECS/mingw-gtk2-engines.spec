%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 0

%global mingw_pkg_name gtk2-engines

Summary:        Theme engines for GTK+ 2.0
Name:           mingw-gtk2-engines
Version:        2.20.2
Release:        4%{?dist}
# for details on which engines are GPL vs LGPL, see COPYING
License:        LGPLv2+
Group:          System Environment/Libraries
URL:            http://download.gnome.org/sources/gtk-engines
#VCS: git:git://git.gnome.org/gtk-engines
Source:         http://download.gnome.org/sources/gtk-engines/2.20/gtk-engines-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: mingw32-gtk2
BuildRequires: mingw64-gtk2
BuildRequires: pkgconfig 

BuildRequires: intltool
BuildRequires: gettext

Requires:      pkgconfig


# Fedora-specific tweaks
# http://bugzilla.gnome.org/show_bug.cgi?id=593030
Patch0: gtk-engines-2.18.2-change-bullet.patch
# turn on new tooltips look
Patch1: tooltips.patch
# enable automatic mnemonics
Patch2: auto-mnemonics.patch
# allow dragging on empty areas in menubars
Patch3: window-dragging.patch


%description
The gtk2-engines package contains shared objects and configuration
files that implement a number of GTK+ theme engines. Theme engines
provide different looks for GTK+, some of which resemble other
toolkits or operating systems.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
The gtk2-engines package contains shared objects and configuration
files that implement a number of GTK+ theme engines. Theme engines
provide different looks for GTK+, some of which resemble other
toolkits or operating systems.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
The gtk2-engines package contains shared objects and configuration
files that implement a number of GTK+ theme engines. Theme engines
provide different looks for GTK+, some of which resemble other
toolkits or operating systems.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the libsndfile libraries
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static cross compiled version of the gtk2-engines library.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the libsndfile libraries
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static cross compiled version of the gtk2-engines library.


%{?mingw_debug_package}


%prep
%setup -q -n gtk-engines-%{version}

%patch0 -p1 -b .bullet
%patch1 -p1 -b .tooltips
%patch2 -p1 -b .mnemonics
%patch3 -p1 -b .window-dragging

%build
%mingw_configure --enable-static

%mingw_make %{?_smp_mflags}

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# no .la, please
find $RPM_BUILD_ROOT%{mingw32_libdir} -name '*.la' -delete
#find $RPM_BUILD_ROOT%{mingw64_libdir} -name '*.la' -delete

# sanitize permissions
find $RPM_BUILD_ROOT%{mingw32_datadir}/themes -type d -exec chmod 755 {} \;
find $RPM_BUILD_ROOT%{mingw32_datadir}/themes -type f -name "*.png" -exec chmod 644 {} \;
find $RPM_BUILD_ROOT%{mingw32_datadir}/themes -name "gtkrc*" -perm /111 -exec chmod 644 {} \;

#find $RPM_BUILD_ROOT%{mingw64_datadir}/themes -type d -exec chmod 755 {} \;
#find $RPM_BUILD_ROOT%{mingw64_datadir}/themes -type f -name "*.png" -exec chmod 644 {} \;
#find $RPM_BUILD_ROOT%{mingw64_datadir}/themes -name "gtkrc*" -perm /111 -exec chmod 644 {} \;

%mingw_find_lang %{name} --all-name


%files -n mingw32-%{mingw_pkg_name} -f mingw32-%{name}.lang 
%doc README AUTHORS NEWS COPYING
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libclearlooks.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libclearlooks.dll.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libcrux-engine.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libcrux-engine.dll.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libglide.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libglide.dll.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libhcengine.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libhcengine.dll.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libindustrial.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libindustrial.dll.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libmist.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libmist.dll.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libredmond95.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libredmond95.dll.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libthinice.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libthinice.dll.a
%{mingw32_datadir}/themes/*
%{mingw32_datadir}/gtk-engines
%{mingw32_libdir}/pkgconfig/gtk-engines-2.pc

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libclearlooks.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libcrux-engine.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libglide.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libhcengine.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libindustrial.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libmist.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libredmond95.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libthinice.a

%changelog
* Wed Apr 23 2014 Tim Mayberry <mojofunk@gmail.com> - 2.20.2-4
- Rebuild for F20

* Fri Jul 26 2013 Tim Mayberry <mojofunk@gmail.com> - 2.20.2-3
- Fix command used to reset perms for F19

* Sat Jun 30 2012 Tim Mayberry <mojofunk@gmail.com> - 2.20.2-2
- Update to Fedora 17 MinGW package guidelines
- disable 64 bit build, due to libtool issue

* Wed Dec 14 2011 Tim Mayberry <mojofunk@gmail.com> - 2.20.2-1
- Initial mingw-w64 package based on native Fedora package
