%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

Summary:        Free, cross platform, open-source, audio I/O library
Name:           mingw32-portaudio
Version:        19
Release:        2%{?dist}
License:        MIT
Group:          System Environment/Libraries
URL:            http://www.portaudio.com/
# This is http://www.portaudio.com/archives/pa_snapshot.tgz from 27-03-2011
Source:         pa_snapshot.tgz
Patch1:         portaudio-doxynodate.patch
Patch2:         portaudio-pkgconfig-alsa.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  pkgconfig

Requires:       pkgconfig

%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

%package static
Summary: Static development files for the portaudio audio I/O library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description static

Static development files for the portaudio audio I/O library


%{?_mingw32_debug_package}


%prep
%setup -q -n portaudio
%patch1 -p1


%build
# can't build shared and static lib at same time
%{_mingw32_configure} --enable-shared --disable-static \
	--with-winapi=wmme

%{_mingw32_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%{_mingw32_make} DESTDIR=$RPM_BUILD_ROOT install

find $RPM_BUILD_ROOT -name '*.la' -delete


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt
%{_mingw32_includedir}/portaudio.h
%{_mingw32_libdir}/pkgconfig/*.pc
%{_mingw32_bindir}/libportaudio-2.dll
%{_mingw32_libdir}/libportaudio.dll.a

%changelog
* Mon Dec 12 2011 Tim Mayberry <mojofunk[at]gmail.com> - 19-2
- use _smp_mflags, seems to build ok

* Fri Nov 11 2011 Tim Mayberry <mojofunk[at]gmail.com> - 19-1
- Initial mingw package for Fedora
