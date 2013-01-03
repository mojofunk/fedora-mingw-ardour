%global __strip %{mingw32_strip}
%global __objdump %{mingw32_objdump}

Name:           mingw-cppunit
Version:        1.12.1
Release:        10%{?dist}
Summary:        MinGW Windows C++ unit testing framework

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://cppunit.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cppunit/cppunit-%{version}.tar.gz
Patch0:         mingw-cppunit-1.12.1-no-secure-lib.patch
BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 23
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
Requires: pkgconfig

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for supervised 
tests.

MinGW Windows C++ unit testing framework.


%package -n mingw32-cppunit
Summary:        MinGW Windows C++ unit testing framework

%description -n mingw32-cppunit
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for supervised
tests.

MinGW Windows C++ unit testing framework.


%prep
%setup -q -n cppunit-%{version}
%patch0 -p0 -b no-secure-lib

for file in THANKS ChangeLog NEWS; do
   iconv -f latin1 -t utf8 < $file > ${file}.utf8
   touch -c -r $file ${file}.utf8
   mv ${file}.utf8 $file
done

%build
%mingw32_configure --disable-static --disable-doxygen

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
# Remove the .la files
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la


%files -n mingw32-cppunit
%doc AUTHORS COPYING NEWS README THANKS ChangeLog TODO BUGS doc/FAQ
%{mingw32_bindir}/cppunit-config
%{mingw32_bindir}/DllPlugInTester.exe
%{mingw32_includedir}/cppunit/
%{mingw32_bindir}/libcppunit-*.dll
%{mingw32_libdir}/pkgconfig/cppunit.pc
%{mingw32_libdir}/libcppunit.dll.a
%{mingw32_datadir}/aclocal/cppunit.m4
%exclude %{mingw32_mandir}/man1/cppunit-config.1


%changelog
* Fri Jul 31 2012 Tim Mayberry <mojofunk@gmail.com> - 1.12.1-10
- Add no-secure-lib patch to avoid sprintf_s usage

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 1.12.1-9
- Remove the .la files

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.1-8
- Renamed the source package to mingw-cppunit (RHBZ #800853)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.1-7
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 1.12.1-5
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct  4 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.12.1-3
- Rebuild for MinGW debuginfo breakage

* Mon Aug 17 2009 Nicolas Chauvet <kwizart@gmail.com> - 1.12.1-2
- Fix BR mingw32-gcc-c++
- Update description
- Disable duplicated docs with native package.

* Mon Jan  5 2009 Nicolas Chauvet <kwizart@gmail.com> - 1.12.1-1
- Initial package based on original cppunit.spec

