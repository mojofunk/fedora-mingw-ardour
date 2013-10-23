%{?mingw_package_header}

%global _basename taglib

%bcond_without tests
%bcond_with doc
%global apidocdir __api-doc_fedora

Name:       mingw-%{_basename}	
Summary:    Audio Meta-Data Library
Version:    1.9.1
Release:    1%{?dist}

License:    LGPLv2 and MPL
#URL:       http://launchpad.net/taglib
URL:        http://taglib.github.com/
%if 0%{?snap:1}
Source0:    %{_basename}-%{version}-%{snap}.tar.gz
%else
Source0:    https://github.com/downloads/taglib/taglib/%{_basename}-%{version}%{?pre}.tar.gz
%endif
# The snapshot tarballs generated with the following script:
Source1:    taglib-snapshot.sh
Patch0:     taglib-mingw.patch

# http://bugzilla.redhat.com/343241
# try 1, use pkg-config
Patch1:     taglib-1.5b1-multilib.patch 
# try 2, kiss omit -L%_libdir
Patch2:     taglib-1.5rc1-multilib.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-zlib

BuildRequires: cmake
BuildRequires: pkgconfig
%if %{with tests}
#BuildRequires: cppunit-devel
%endif
%if %{with doc}
BuildRequires: doxygen
BuildRequires: graphviz
%endif

%description
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags.

%package -n mingw32-%{_basename}
Summary: MinGW Windows version of TagLib for the win32 target
%description -n mingw32-%{_basename}
TagLib is a library for reading and editing the meta-data of several
popular audio formats.
This is the MinGW version, built for the win32 target.

%package -n mingw64-%{_basename}
Summary: MinGW Windows version of TagLib for the win64 target
%description -n mingw64-%{_basename}
TagLib is a library for reading and editing the meta-data of several
popular audio formats.
This is the MinGW version, built for the win64 target.

%{?mingw_debug_package}

%prep
%setup -q -n %{_basename}-%{version}%{?pre}
%patch0 -p1

# patch1 not applied
## omit for now
%patch2 -p1 -b .multilib


%build
%{mingw_cmake} \
  #%{?with_tests:-DBUILD_TESTS:BOOL=ON} \
  #..

%{mingw_make} %{?_smp_mflags}

%if %{with doc}
%{mingw_make} docs
%endif


%install
%{mingw_make} install/fast DESTDIR=%{buildroot}

%if %{with doc}
rm -fr %{apidocdir} ; mkdir %{apidocdir}
cp -a build_win32/doc/html/ %{apidocdir}/
ln -s html/index.html %{apidocdir}
find %{apidocdir} -name '*.md5' | xargs rm -fv
%endif


%files -n mingw32-%{_basename}
%doc AUTHORS COPYING.LGPL NEWS
%{mingw32_bindir}/libtag.dll
%{mingw32_bindir}/libtag_c.dll
%doc examples
%{mingw32_bindir}/taglib-config.cmd
%{mingw32_includedir}/taglib/
%{mingw32_libdir}/libtag.dll.a
%{mingw32_libdir}/libtag_c.dll.a
%{mingw32_libdir}/pkgconfig/taglib.pc
%{mingw32_libdir}/pkgconfig/taglib_c.pc
%if %{with doc}
%doc %{apidocdir}/*
%endif

%files -n mingw64-%{_basename}
#%doc AUTHORS COPYING.LGPL NEWS
%{mingw64_bindir}/libtag.dll
%{mingw64_bindir}/libtag_c.dll
%doc examples
%{mingw64_bindir}/taglib-config.cmd
%{mingw64_includedir}/taglib/
%{mingw64_libdir}/libtag.dll.a
%{mingw64_libdir}/libtag_c.dll.a
%{mingw64_libdir}/pkgconfig/taglib.pc
%{mingw64_libdir}/pkgconfig/taglib_c.pc
%if %{with doc}
%doc %{apidocdir}/*
%endif


%changelog
* Wed Oct 23 2013 Tim Mayberry <mojofunk@gmail.com> 1.9.1-1
- Update to version 1.9.1
- License: +MPL

* Fri Aug 2 2013 Tim Mayberry <mojofunk@gmail.com> 1.8-3.20130218git
- Updated to version in Fedora 19

* Fri May 17 2013 Steven Boswell <ulatekh@yahoo.com> 1.8-3.20121215git
- Ported Fedora package to MinGW
