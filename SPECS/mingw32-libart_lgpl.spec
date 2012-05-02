%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

Summary: Library of graphics routines used by libgnomecanvas
Name: mingw32-libart_lgpl
Version: 2.3.21
Release: 4%{?dist}
URL: http://www.gnome.org/
Source0: http://ftp.gnome.org/pub/gnome/sources/libart_lgpl/2.3/libart_lgpl-%{version}.tar.bz2
Patch0: libart-multilib.patch
License: LGPLv2+
Group: System Environment/Libraries 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 


BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  pkgconfig

Requires:       pkgconfig
%description

Graphics routines used by the GnomeCanvas widget and some other 
applications. libart renders vector paths and the like.

%package static
Summary:        Static version of the MinGW libart_lgpl
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static

Static version of the MinGW libart_lgpl


%{?_mingw32_debug_package}

%prep
%setup -q -n libart_lgpl-%{version}
%patch0 -p1 -b .multilib


%build
%{_mingw32_configure} --enable-shared --enable-static
%{_mingw32_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

%{_mingw32_make} DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_mingw32_libdir}/*.la


%clean
rm -rf $RPM_BUILD_ROOT


#%post -p /sbin/ldconfig

#%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_mingw32_bindir}/libart_lgpl_2-2.dll
%{_mingw32_bindir}/libart2-config
%{_mingw32_libdir}/libart_lgpl_2.dll.a
%{_mingw32_libdir}/pkgconfig/libart-2.0.pc
%{_mingw32_includedir}/libart-2.0/libart_lgpl

%files static
%defattr(-,root,root,-)
%{_mingw32_libdir}/libart_lgpl_2.a

%changelog
* Fri Nov 11 2011 Tim Mayberry <mojofunk@gmail.com> - 2.3.21-4
- Use mingw32_make macro instead of make

* Wed Nov 9 2011 Tim Mayberry <mojofunk@gmail.com> - 2.3.21-3
- Rebuild for Fedora 16

* Wed Feb 24 2011 Tim Mayberry <mojofunk@gmail.com> - 2.3.21-2
- Remove fix for multilib issue from native package

* Wed Feb 24 2011 Tim Mayberry <mojofunk@gmail.com> - 2.3.21-1
- First MinGW package based on native Fedora package

* Wed Jul  7 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.3.21-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Caolán McNamara <caolanm@redhat.com> - 2.3.20-3
- rebuild to get provides pkgconfig(libart-2.0)

* Mon May 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.3.20-2
- add sparc64 for multilib

* Wed Jan 30 2008 Matthias Clasen <mclasen@redhat.com> - 2.3.20-1
- Update to 2.3.20
- Drop upstreamed patch
- Correct license field

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 2.3.19-3
- Rebuild for build ID

* Thu Mar 01 2007 Behdad Esfahbod <besfahbo@edhat.com> - 2.3.19-2
- Add upstreamed patch libart-2.3.19-header.patch
- Resolves: #230571

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.3.19-1
- Update to 2.3.19

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.3.18-1
- Update to 2.3.18

* Mon Jul 31 2006 Jesse Keating <jkeating@redhat.com> - 2.3.17-4
- Fix typo in header name

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.3.17-3
- Fix multilib conflicts
- Don't ship static libraries

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.3.17-2.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.3.17-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.3.17-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> 2.3.17-2
- Rebuild with gcc4

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> 2.3.17-1
- update to 2.3.17

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Oct  6 2003 Alexander Larsson <alexl@redhat.com> 2.3.16-1
- 2.3.16

* Tue Aug 12 2003 Alexander Larsson <alexl@redhat.com> 2.3.14-1
- 2.3.14

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec  9 2002 Alexander Larsson <alexl@redhat.com> 2.3.11
- Update to 2.3.11

* Tue Dec 03 2002 Elliot Lee <sopwith@redhat.com> 2.3.10-2
- Remove unpackaged file

* Sat Jul 27 2002 Havoc Pennington <hp@redhat.com>
- 2.3.10, required by nautilus 2.0.2 for some reason

* Mon Jun 24 2002 Havoc Pennington <hp@redhat.com>
- 2.3.9, should give gdm login screen a kick in the ass

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Apr 24 2002 Havoc Pennington <hp@redhat.com>
 - rebuild in different environment

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- rebuild

* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- actually increase version to 2.3.8

* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- upgrade to 2.3.8 so header files don't break eel2

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 2.3.7.91 snap

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- cvs snap, rebuild with new glib

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- 2.3.6

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- new CVS snap with upstream changes merged

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- Initial build.


