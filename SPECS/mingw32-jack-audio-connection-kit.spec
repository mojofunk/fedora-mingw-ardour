%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}


Summary:        The Jack Audio Connection Kit
Name:           mingw32-jack-audio-connection-kit
Version:        1.9.9
Release:        3%{?dist}
# The entire source (~500 files) is a mixture of these three licenses
License:        GPLv2 and GPLv2+ and LGPLv2+
Group:          System Environment/Daemons
URL:            http://www.jackaudio.org
Source0:        http://www.grame.fr/~letz/jack-%{version}.tar.bz2
Patch0:         jack-1.9.9-mingw-waf.patch
patch1:         jack-1.9.9-SHGFP_CURRENT_TYPE-mingw.patch
patch2:         jack-1.9.9-portaudio-no-asio.patch
Patch3:         jack-1.9.9-example-clients.patch


BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires:  mingw32-filesystem >= 69-8
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libsamplerate
# for examples
BuildRequires:  mingw32-pthreads
# for regex.h
BuildRequires:  mingw32-libgnurx
BuildRequires:  mingw32-portaudio

BuildRequires:  pkgconfig

BuildArch:      noarch


%{?_mingw32_debug_package}


%description
JACK is a low-latency audio server, written primarily for the Linux
operating system. It can connect a number of different applications to
an audio device, as well as allowing them to share audio between
themselves. Its clients can run in their own processes (i.e. as a
normal application), or can they can run within a JACK server (i.e. a
"plugin").

JACK is different from other audio server efforts in that it has been
designed from the ground up to be suitable for professional audio
work. This means that it focuses on two key areas: synchronous
execution of all clients, and low latency operation.

%package devel
Summary:       Header files for Jack
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description devel
Header files for the Jack Audio Connection Kit.

%package example-clients
Summary:       Example clients that use Jack 
Group:         Applications/Multimedia
Requires:      %{name} = %{version}-%{release}

%description example-clients
Small example clients that use the Jack Audio Connection Kit.

%prep
%setup -q -n jack-%{version}

%patch0 -p1 -b .mingw
%patch1 -p1 -b .shgfp
%patch2 -p1 -b .noasio
%patch3 -p1 -b .examples

# Fix encoding issues
for file in ChangeLog README TODO; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build
export PREFIX=%{_mingw32_prefix}

%{_mingw32_env}
./waf configure --debug --dist-target=mingw \
	--portaudio --winmme


./waf build -v %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT
./waf --destdir=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%doc ChangeLog README README_NETJACK2 TODO
%{_mingw32_bindir}/jackd.exe
#don't really want to package this...bug in mingw32-find-debuginfo?
#%{_mingw32_bindir}/*.debug
%{_mingw32_includedir}/jack/
%{_mingw32_bindir}/jack/*.dll
%{_mingw32_bindir}/jack*.dll
%{_mingw32_bindir}/jack_*.exe
%{_mingw32_libdir}/pkgconfig/jack.pc
%{_mingw32_libdir}/libaudioadapter.dll.a
%{_mingw32_libdir}/libdummy.dll.a
%{_mingw32_libdir}/libjack.dll.a
%{_mingw32_libdir}/libjackserver.dll.a
%{_mingw32_libdir}/libloopback.dll.a
%{_mingw32_libdir}/libnet.dll.a
%{_mingw32_libdir}/libnetmanager.dll.a
%{_mingw32_libdir}/libnetadapter.dll.a
%{_mingw32_libdir}/libprofiler.dll.a
%{_mingw32_libdir}/libinprocess.dll.a
%{_mingw32_libdir}/libjacknet.dll.a
%{_mingw32_libdir}/libnetone.dll.a
# this conflicts from the real portaudio import lib
%exclude %{_mingw32_libdir}/libportaudio.dll.a
%{_mingw32_libdir}/libwinmme.dll.a

%changelog
* Thu May 5 2012 Tim Mayberry <mojofunk@gmail.com> - 1.9.9-3
- Use 1.9.9 pre tarball based on master branch@871bd0851d plus patches

* Sun Apr 29 2012 Tim Mayberry <mojofunk@gmail.com> - 1.9.9-2
- Update to git f82ec715, plus waf patches
- Use smp_flags again with waf now working correctly for smp builds

* Sun Dec 11 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.9-1
- Update to svn@4658 snapshot, plus waf patches
- Use -j1 to avoid waf bug with smp builds

* Sun Dec 11 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.8-7
- Update to svn@4638 snapshot, plus waf patches

* Sat Nov 12 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.8-6
- Add portaudio to BR
- new snapshot
- add --portaudio and --winmme to build flags

* Fri Nov 11 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.8-5
- rebuild using F16 mingw toolchain
- fix generic macros at top of spec to adhere to pkg guidelines 

* Mon Apr 12 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.8-4
- rebuild using F14 mingw toolchain
- Add mingw32-libsamplerate to BuildRequires

* Mon Apr 11 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.8-3
- new tarball with JACK_OPTIONAL_WEAK_EXPORT undefined/defined to nothing
- enable debug build

* Sat Apr 9 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.8-2
- rebuild using mingw64 compiler

- use define instead of global when declaring macros
* Sun Apr 5 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.8-1
- Update to custom version post 1.9.7

* Sun Mar 27 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.7-1
- Update to svn version close to 1.9.7 to get thread type changes 

* Fri Feb 18 2011 Tim Mayberry <mojofunk@gmail.com> - 1.9.6-1
- First build for MinGW based on native spec file
