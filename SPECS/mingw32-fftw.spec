%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

Name:           mingw32-fftw
Version:        3.2.2
Release:        3%{?dist}
Summary:        A Fast Fourier Transform library
Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.fftw.org
Source0:        http://www.fftw.org/fftw-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

# For check phase
BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  gcc-gfortran

BuildRequires:  pkgconfig

%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.


%package        static
Summary:        Static version of FFTW library for MinGW
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    static
The fftw-static package contains the statically linkable version of
the FFTW fast Fourier transform library.

%package        doc
Summary:        FFTW library manual
Group:          Documentation
BuildArch:      noarch

%description doc
This package contains the manual for the FFTW fast Fourier transform
library.


%prep
%setup -q -c %{name}-%{version}
for dir in single double long; do
  cp -a fftw-%{version} $dir
done
rm -rf fftw-%{version}


%build
# Configure uses g77 by default, if present on system
export F77=gfortran

CONFIG_FLAGS="--enable-shared --disable-dependency-tracking"
pushd double
        %{_mingw32_configure} $CONFIG_FLAGS
#        sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#        sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
        make %{?_smp_mflags}
popd
pushd single
        %{_mingw32_configure} $CONFIG_FLAGS --enable-single
#        sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#        sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
        make %{?_smp_mflags}
popd
pushd long
        %{_mingw32_configure} $CONFIG_FLAGS --enable-long-double
#        sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#        sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
        make %{?_smp_mflags}
popd


%install
rm -rf ${RPM_BUILD_ROOT}
pushd double
        make install DESTDIR=${RPM_BUILD_ROOT}
        cp -a AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO ../
        cp -a doc/ ../
popd
pushd single
        make install DESTDIR=${RPM_BUILD_ROOT}
popd
pushd long
        make install DESTDIR=${RPM_BUILD_ROOT}
popd
rm -f ${RPM_BUILD_ROOT}%{_mingw32_infodir}/dir
rm -f ${RPM_BUILD_ROOT}%{_mingw32_libdir}/*.la

#%check
#bdir=`pwd`
#export LD_LIBRARY_PATH=$bdir/single/.libs:$bdir/single/threads/.libs:$bdir/double/.libs:$bdir/double/threads/.libs:$bdir/long/.libs:$bdir/long/threads/.libs
#make -C single check
#make -C double check
#make -C long check

%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
#%doc doc/FAQ/fftw-faq.html/
%doc %{_mingw32_infodir}/fftw3.info*
%doc %{_mingw32_mandir}/man1/fftw*.1*
%{_mingw32_bindir}/fftw*-wisdom*
%{_mingw32_bindir}/libfftw*dll*
%{_mingw32_libdir}/libfftw3*
%{_mingw32_includedir}/fftw3.*
%{_mingw32_libdir}/pkgconfig/fftw3*.pc

%files doc
%defattr(-,root,root,-)
%doc doc/*.pdf doc/html/

%files static
%defattr(-,root,root,-)
#%{_mingw32_libdir}/libfftw3*.a


%changelog
* Fri Nov 11 2011 Tim Mayberry <mojofunk@gmail.com> 3.2.2-3
- Rebuild for F16

* Sun Feb 20 2011 Tim Mayberry <mojofunk@gmail.com> 3.2.2-2
- Add gcc-gfortran to BuildRequires

* Sun Feb 20 2011 Tim Mayberry <mojofunk@gmail.com> 3.2.2-2
- Add gcc-gfortran to BuildRequires

* Sun Feb 20 2011 Tim Mayberry <mojofunk@gmail.com> 3.2.2-1
- Initial MinGW build
- disable threads

* Sat Jan 9 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.2.2-4
- Get rid of rpath.

* Sat Jan 9 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.2.2-3
- Branch out developers' manual to -doc.

* Sat Jan 2 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.2.2-2
- Add check phase.
- Cosmetic changes to spec file (unified changelog format, removed unnecessary
  space).
- Use rm instead of find -delete, as latter is not present on EPEL-4.
- Generalize obsoletes of fftw3 packages. Add Obsoletes: fftw3-static.

* Fri Jan 1 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2.
- Make file listings more explicit.
- Don't use file dependencies for info.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Conrad Meyer <konrad@tylerc.org> - 3.2.1-1
- Bump to 3.2.1.

* Thu Dec 4 2008 Conrad Meyer <konrad@tylerc.org> - 3.2-1
- Bump to 3.2.

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.1.2-7
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1.2-6
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Quentin Spencer <qspencer@users.sf.net> 3.1.2-5
- Rebuild for F8.

* Fri Jul 27 2007 Quentin Spencer <qspencer@users.sf.net> 3.1.2-4
- Split static libs into separate package (bug 249686).

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 3.1.2-3
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Quentin Spencer <qspencer@users.sf.net> 3.1.2-2
- BuildRequires: pkgconfig for -devel (bug 206444).

* Fri Sep  8 2006 Quentin Spencer <qspencer@users.sf.net> 3.1.2-1
- New release.

* Fri Jun  2 2006 Quentin Spencer <qspencer@users.sf.net> 3.1.1-1
- New upstream release.

* Fri Feb 24 2006 Quentin Spencer <qspencer@users.sf.net> 3.1-4
- Re-enable static libs (bug 181897).
- Build long-double version of libraries (bug 182587).

* Mon Feb 13 2006 Quentin Spencer <qspencer@users.sf.net> 3.1-3
- Add Obsoletes and Provides.

* Mon Feb 13 2006 Quentin Spencer <qspencer@users.sf.net> 3.1-2
- Rebuild for Fedora Extras 5.
- Disable static libs.
- Remove obsolete configure options.

* Wed Feb  1 2006 Quentin Spencer <qspencer@users.sf.net> 3.1-1
- Upgrade to the 3.x branch, incorporating changes from the fftw3 spec file.
- Add dist tag.

* Mon May 23 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.1.5-8
- BuildReq gcc-gfortran (#156490).

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.1.5-7
- rebuild on all arches
- buildrequire compat-gcc-32-g77

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 2.1.5-5
- Bump release to provide Extras upgrade path.

* Tue Apr 06 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.5-0.fdr.4
- BuildReq gcc-g77.

* Mon Sep 22 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.5-0.fdr.3
- Dropped post/preun scripts for info.

* Wed Sep 17 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.5-0.fdr.2
- Remove aesthetic comments.
- buildroot -> RPM_BUILD_ROOT.
- post/preun for info files.

* Mon Apr 07 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.5-0.fdr.1
- Updated to 2.1.5.

* Tue Apr 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.4-0.fdr.2
- Added Epoch:0.
- Added ldconfig to post and postun.

* Sun Mar 22 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 2.1.4-0.fdr.1
- Updated to 2.1.4.

* Fri Mar 14 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 2.1.3-0.fdr.1
- Fedorafied.

* Mon Oct 21 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
