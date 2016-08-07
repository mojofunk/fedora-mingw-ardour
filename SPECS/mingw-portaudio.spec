%{?mingw_package_header}

%global native_pkg_name portaudio

%bcond_with asio

Name:           mingw-%{native_pkg_name}
Version:        2.0
Release:        10%{?dist}
Summary:        Free, cross platform, open-source, audio I/O library
Group:          System Environment/Libraries
License:        MIT
URL:            http://www.portaudio.com/
# package created from svn rev 1928 using waf dist
Source0:        portaudio-2.0.tar.bz2
Source1:        portaudio-2.0-waf
Source2:        portaudio-2.0-wscript
%if %{with asio}
Source3:        ASIOSDK2
%endif

BuildArch:     noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

BuildRequires: python
BuildRequires: pkgconfig

#Requires:

%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

%package -n mingw32-%{native_pkg_name}
Summary:        Development files for %{name}
Group:          Development/Libraries

%description -n mingw32-%{native_pkg_name}
The %{name} package contains libraries and header files for
developing applications that use %{name}.

%package -n mingw32-%{native_pkg_name}-tests
Summary:        Test executables for %{name}
Group:          Development/Libraries

%description -n mingw32-%{native_pkg_name}-tests
The package contains tests for for %{name}.


%package -n mingw64-%{native_pkg_name}
Summary:        Development files for %{name}
Group:          Development/Libraries

%description -n mingw64-%{native_pkg_name}
The %{name} package contains libraries and header files for
developing applications that use %{name}.

%package -n mingw64-%{native_pkg_name}-tests
Summary:        Test executables for %{name}
Group:          Development/Libraries

%description -n mingw64-%{native_pkg_name}-tests
The package contains tests for for %{name}.


%{?mingw_debug_package}


%prep
%setup -q -c %{native_pkg_name}-%{version}

%if %{with asio}
cp -r %{SOURCE3} ASIOSDK2
%endif

pushd %{native_pkg_name}-%{version}
	cp %{SOURCE1} waf
	cp %{SOURCE2} wscript
popd

for dir in win32 win64; do
	cp -a %{native_pkg_name}-%{version} $dir
done
rm -rf %{native_pkg_name}-%{version}

%build

pushd win32
	export PREFIX=%{mingw32_prefix}

	#%{mingw32_env}
	#export PKG_CONFIG_PREFIX=$MINGW_ROOT
	export PKG_CONFIG_LIBDIR=%{mingw32_libdir}/pkgconfig

	./waf configure --with-wmme --with-directx --with-wasapi \
	                %{?_with_asio} --with-tests --with-examples

	./waf build %{?_smp_mflags} -v
popd

pushd win64
	export PREFIX=%{mingw64_prefix}

	#%{mingw64_env}
	#export PKG_CONFIG_PREFIX=$MINGW_ROOT
	export PKG_CONFIG_LIBDIR=%{mingw64_libdir}/pkgconfig

	./waf configure --with-wmme --with-directx --with-wasapi \
	                %{?_with_asio} --with-tests --with-examples

	./waf build %{?_smp_mflags} -v
popd

%install

pushd win32
	./waf --destdir=$RPM_BUILD_ROOT install
	cp -ar LICENSE.txt README.txt ../
	mv $RPM_BUILD_ROOT/%{mingw32_prefix}/bin/*.dll.a $RPM_BUILD_ROOT/%{mingw32_prefix}/lib
popd

pushd win64
	./waf --destdir=$RPM_BUILD_ROOT install
	cp -ar LICENSE.txt README.txt ../
	mv $RPM_BUILD_ROOT/%{mingw64_prefix}/bin/*.dll.a $RPM_BUILD_ROOT/%{mingw64_prefix}/lib
popd

%files -n mingw32-%{native_pkg_name}
%doc LICENSE.txt README.txt
%{mingw32_includedir}/portaudio.h
%{mingw32_includedir}/pa_win_wmme.h
%{mingw32_includedir}/pa_win_ds.h
%{mingw32_includedir}/pa_win_wasapi.h
%if %{with asio}
%{mingw32_includedir}/pa_asio.h
%endif
%{mingw32_bindir}/portaudio-2.dll
%{mingw32_bindir}/pa_devs.exe
%{mingw32_libdir}/libportaudio*dll.a
%{mingw32_libdir}/pkgconfig/portaudio-2.0.pc

%files -n mingw32-%{native_pkg_name}-tests
%{mingw32_bindir}/pa_minlat.exe
%{mingw32_bindir}/patest1.exe
%{mingw32_bindir}/patest_buffer.exe
%{mingw32_bindir}/patest_callbackstop.exe
%{mingw32_bindir}/patest_clip.exe
%{mingw32_bindir}/patest_converters.exe
%{mingw32_bindir}/patest_dither.exe
%{mingw32_bindir}/patest_dsound_find_best_latency_params.exe
%{mingw32_bindir}/patest_dsound_low_level_latency_params.exe
%{mingw32_bindir}/patest_dsound_surround.exe
%{mingw32_bindir}/patest_hang.exe
%{mingw32_bindir}/patest_in_overflow.exe
%{mingw32_bindir}/patest_latency.exe
%{mingw32_bindir}/patest_leftright.exe
%{mingw32_bindir}/patest_longsine.exe
%{mingw32_bindir}/patest_many.exe
%{mingw32_bindir}/patest_maxsines.exe
%{mingw32_bindir}/patest_mono.exe
%{mingw32_bindir}/patest_multi_sine.exe
%{mingw32_bindir}/patest_out_underflow.exe
%{mingw32_bindir}/patest_prime.exe
%{mingw32_bindir}/patest_read_record.exe
%{mingw32_bindir}/patest_ringmix.exe
%{mingw32_bindir}/patest_sine8.exe
%{mingw32_bindir}/patest_sine_channelmaps.exe
%{mingw32_bindir}/patest_sine_formats.exe
%{mingw32_bindir}/patest_sine_srate.exe
%{mingw32_bindir}/patest_sine_time.exe
%{mingw32_bindir}/patest_start_stop.exe
%{mingw32_bindir}/patest_stop.exe
%{mingw32_bindir}/patest_stop_playout.exe
%{mingw32_bindir}/patest_suggested_vs_streaminfo_latency.exe
%{mingw32_bindir}/patest_sync.exe
%{mingw32_bindir}/patest_timing.exe
%{mingw32_bindir}/patest_toomanysines.exe
%{mingw32_bindir}/patest_two_rates.exe
%{mingw32_bindir}/patest_underflow.exe
%{mingw32_bindir}/patest_wire.exe
%{mingw32_bindir}/patest_wmme_find_best_latency_params.exe
%{mingw32_bindir}/patest_wmme_low_level_latency_params.exe
%{mingw32_bindir}/patest_write_stop.exe

%files -n mingw64-%{native_pkg_name}
%doc LICENSE.txt README.txt
%{mingw64_includedir}/portaudio.h
%{mingw64_includedir}/pa_win_wmme.h
%{mingw64_includedir}/pa_win_ds.h
%{mingw64_includedir}/pa_win_wasapi.h
%if %{with asio}
%{mingw64_includedir}/pa_asio.h
%endif
%{mingw64_bindir}/portaudio-2.dll
%{mingw64_bindir}/pa_devs.exe
%{mingw64_libdir}/libportaudio*dll.a
%{mingw64_libdir}/pkgconfig/portaudio-2.0.pc

%files -n mingw64-%{native_pkg_name}-tests
%{mingw64_bindir}/pa_minlat.exe
%{mingw64_bindir}/patest1.exe
%{mingw64_bindir}/patest_buffer.exe
%{mingw64_bindir}/patest_callbackstop.exe
%{mingw64_bindir}/patest_clip.exe
%{mingw64_bindir}/patest_converters.exe
%{mingw64_bindir}/patest_dither.exe
%{mingw64_bindir}/patest_dsound_find_best_latency_params.exe
%{mingw64_bindir}/patest_dsound_low_level_latency_params.exe
%{mingw64_bindir}/patest_dsound_surround.exe
%{mingw64_bindir}/patest_hang.exe
%{mingw64_bindir}/patest_in_overflow.exe
%{mingw64_bindir}/patest_latency.exe
%{mingw64_bindir}/patest_leftright.exe
%{mingw64_bindir}/patest_longsine.exe
%{mingw64_bindir}/patest_many.exe
%{mingw64_bindir}/patest_maxsines.exe
%{mingw64_bindir}/patest_mono.exe
%{mingw64_bindir}/patest_multi_sine.exe
%{mingw64_bindir}/patest_out_underflow.exe
%{mingw64_bindir}/patest_prime.exe
%{mingw64_bindir}/patest_read_record.exe
%{mingw64_bindir}/patest_ringmix.exe
%{mingw64_bindir}/patest_sine8.exe
%{mingw64_bindir}/patest_sine_channelmaps.exe
%{mingw64_bindir}/patest_sine_formats.exe
%{mingw64_bindir}/patest_sine_srate.exe
%{mingw64_bindir}/patest_sine_time.exe
%{mingw64_bindir}/patest_start_stop.exe
%{mingw64_bindir}/patest_stop.exe
%{mingw64_bindir}/patest_stop_playout.exe
%{mingw64_bindir}/patest_suggested_vs_streaminfo_latency.exe
%{mingw64_bindir}/patest_sync.exe
%{mingw64_bindir}/patest_timing.exe
%{mingw64_bindir}/patest_toomanysines.exe
%{mingw64_bindir}/patest_two_rates.exe
%{mingw64_bindir}/patest_underflow.exe
%{mingw64_bindir}/patest_wire.exe
%{mingw64_bindir}/patest_wmme_find_best_latency_params.exe
%{mingw64_bindir}/patest_wmme_low_level_latency_params.exe
%{mingw64_bindir}/patest_write_stop.exe

%changelog
* Sun Aug 7 2016 Tim Mayberry <mojofunk@gmail.com> - 2.0-10
- Rebuild for Fedora 24
- Updates to waf version and wscript

* Wed Oct 28 2015 Tim Mayberry <mojofunk@gmail.com> - 2.0-9
- Update to upstream version svn@1963 for wasapi fixes

* Mon Jul 20 2015 Tim Mayberry <mojofunk@gmail.com> - 2.0-8
- Add conditional ASIO option to build with ASIOSDK
- Update waf build files to support ASIO

* Tue Apr 28 2015 Tim Mayberry <mojofunk@gmail.com> - 2.0-7
- Add --with-wasapi option and use it instead of wdmks

* Thu Mar 19 2015 Tim Mayberry <mojofunk@gmail.com> - 2.0-6
- Add --with-wmme option
- Added x86 plain converters to build
- Add tests sub package with all the tests

* Thu May 15 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-5
- Add wdmks backend to build

* Thu May 15 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-4
- Add directx backend to build

* Thu May 15 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-3
- Add tests and examples to build

* Thu Apr 24 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-2
- Fix portaudio header install path

* Wed Apr 23 2014 Tim Mayberry <mojofunk@gmail.com> - 2.0-1
- Initial mingw package of 2.0(svn@1928) using waf build system
