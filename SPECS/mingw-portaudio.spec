%{?mingw_package_header}
	
%global mingw_build_win32 1
%global mingw_build_win64 0

%global mingw_pkg_name portaudio

Summary:       Free, cross platform, open-source, audio I/O library
Name:          mingw-portaudio
Version:       19
Release:       2%{?dist}
License:       MIT
Group:         System Environment/Libraries
URL:           http://www.portaudio.com/
# This is http://www.portaudio.com/archives/pa_snapshot.tgz from 27-03-2011
Source:        pa_snapshot.tgz
Patch1:        portaudio-doxynodate.patch
Patch2:        portaudio-pkgconfig-alsa.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:     noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: pkgconfig

Requires:      pkgconfig


%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the portaudio library
Requires:       mingw32-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-%{mingw_pkg_name}-static
Static cross compiled version of the portaudio library.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Static cross compiled version of the portaudio library
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-%{mingw_pkg_name}-static
Static cross compiled version of the portaudio library.


%{?mingw_debug_package}


%prep
%setup -q -n portaudio
%patch1 -p1
#%patch2 -p1


%build
# can't build static lib....?
%mingw_configure --enable-shared --disable-static --with-winapi=wmme,directx
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# no .la, please
find $RPM_BUILD_ROOT%{mingw32_libdir} -name '*.la' -delete
#find $RPM_BUILD_ROOT%{mingw64_libdir} -name '*.la' -delete


%files -n mingw32-%{mingw_pkg_name}
%doc LICENSE.txt README.txt
%{mingw32_includedir}/portaudio.h
%{mingw32_libdir}/pkgconfig/*.pc
%{mingw32_bindir}/libportaudio-2.dll
%{mingw32_libdir}/libportaudio.dll.a

#%files -n mingw64-%{mingw_pkg_name}
#%doc LICENSE.txt README.txt
#%{mingw64_includedir}/portaudio.h
#%{mingw64_libdir}/pkgconfig/*.pc
#%{mingw64_bindir}/libportaudio-2.dll
#%{mingw64_libdir}/libportaudio.dll.a

%files -n mingw32-%{mingw_pkg_name}-static
#%{mingw32_libdir}/libportaudio.a

#%files -n mingw64-%{mingw_pkg_name}-static
#%{mingw64_libdir}/libportaudio.a

%changelog
* Sun Jul 1 2012 Tim Mayberry <mojofunk@gmail.com> - 19-2
- Update spec to Fedora 17 package guidelines
- Disable 64 bit build due to link errors

* Wed Dec 14 2011 Tim Mayberry <mojofunk@gmail.com> - 19-1
- Initial mingw-w64 package, no static lib and no wdkms or wasapi support
