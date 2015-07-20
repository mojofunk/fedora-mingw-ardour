#!/usr/bin/env python

import os

from waflib import Options

APPNAME = 'portaudio'
VERSION = '2.0'

out = 'waf-build'

def options(opt):
    opt.load('compiler_c')
    opt.load('compiler_cxx')

    opt.add_option('--platform', type='string', default='auto',
                   help='Specify the target for cross-compiling [auto,mingw]')

    opt.add_option('--enable-static', action='store_true', default=False, dest='enable_static',
                   help='Build a static version of Portaudio library')

    opt.add_option('--with-tests', action='store_true', default=False, dest='with_tests',
                   help='Build Portaudio tests')

    opt.add_option('--with-examples', action='store_true', default=False, dest='with_examples',
                   help='Build Portaudio example programs')

    opt.add_option('--with-wmme', action='store_true', default=False, dest='with_wmme',
                   help='Build WMME support')

    opt.add_option('--with-directx', action='store_true', default=False, dest='with_directx',
                   help='Build DirectX support')

    opt.add_option('--with-directsound-full-duplex-create', action='store_true',
                   default=False, dest='with_directsound_full_duplex',
                   help='Use DirectSound full duplex create')

    opt.add_option('--with-wdmks', action='store_true', default=False, dest='with_wdmks',
                   help='Build with WDM/KS API support')

    opt.add_option('--with-wdmks-device-info', action='store_true', default=False, dest='with_wdmks_device_info',
                   help='Use WDM/KS API for defice info')

    opt.add_option('--with-wasapi', action='store_true', default=False, dest='with_wasapi',
                   help='Build with WASAPI API support')

    opt.add_option('--with-asio', action='store_true', default=False, dest='with_asio',
                   help='Build with ASIO API support')

    # Unicode option?
    # asio sdk path option


def configure(conf):
    conf.load('compiler_c')

    conf.check(compiler='c',
               lib='ole32',
               mandatory=True,
               uselib_store='OLE')

    conf.check(compiler='c',
               lib='winmm',
               mandatory=True,
               uselib_store='WINMM')

    conf.env.ENABLE_STATIC = Options.options.enable_static

    conf.env.WITH_TESTS = Options.options.with_tests

    conf.env.WITH_EXAMPLES = Options.options.with_examples

    conf.env.WITH_WMME = Options.options.with_wmme

    conf.env.WITH_DIRECTX = Options.options.with_directx

    conf.env.WITH_DSOUND_FULL_DUPLEX = Options.options.with_directsound_full_duplex

    conf.env.WITH_WDMKS = Options.options.with_wdmks

    conf.env.WITH_WDMKS_DEVICE_INFO = Options.options.with_wdmks_device_info

    conf.env.WITH_WASAPI = Options.options.with_wasapi

    conf.env.WITH_ASIO = Options.options.with_asio

    if conf.env.WITH_WDMKS:
        conf.check(compiler='c',
                   lib='setupapi',
                   mandatory=True,
                   uselib_store='SETUPAPI')

        conf.check(compiler='c',
                   lib='ksuser',
                   mandatory=True,
                   uselib_store='KSUSER')

    if conf.env.WITH_WDMKS or conf.env.WITH_WDMKS_DEVICE_INFO or conf.env.WITH_WASAPI:
        conf.check(compiler='c',
                   lib='uuid',
                   mandatory=True,
                   uselib_store='UUID')

    if conf.env.WITH_ASIO:
        conf.load('compiler_cxx')


def build(bld):

    use_defines = []
    uselib_extra = []
    asio_includes = []

    common_includes = '''
	src/common/pa_allocation.h
	src/common/pa_converters.h
	src/common/pa_cpuload.h
	src/common/pa_debugprint.h
	src/common/pa_dither.h
	src/common/pa_endianness.h
	src/common/pa_hostapi.h
	src/common/pa_memorybarrier.h
	src/common/pa_process.h
	src/common/pa_ringbuffer.h
	src/common/pa_stream.h
	src/common/pa_trace.h
	src/common/pa_types.h
	src/common/pa_util.h
	'''

    common_sources = '''
	src/common/pa_allocation.c
	src/common/pa_converters.c
	src/common/pa_cpuload.c
	src/common/pa_debugprint.c
	src/common/pa_dither.c
	src/common/pa_front.c
	src/common/pa_process.c
	src/common/pa_ringbuffer.c
	src/common/pa_stream.c
	src/common/pa_trace.c
	'''

    windows_sources = '''
	src/os/win/pa_win_hostapis.c
	src/os/win/pa_win_util.c
	src/os/win/pa_win_waveformat.c
	src/os/win/pa_win_coinitialize.c
	src/os/win/pa_x86_plain_converters.c
	'''

    wmme_includes = '''
	include/pa_win_wmme.h
	'''

    wmme_sources = '''
	src/hostapi/wmme/pa_win_wmme.c
	'''

    dsound_includes = '''
	include/pa_win_ds.h
	src/hostapi/dsound/pa_win_ds_dynlink.h
	'''

    dsound_sources = '''
    src/hostapi/dsound/pa_win_ds.c
    src/hostapi/dsound/pa_win_ds_dynlink.c
	'''

    wdmks_includes = '''
    include/pa_win_wdmks.h
	'''

    wdmks_sources = '''
    src/hostapi/wdmks/pa_win_wdmks.c
	'''

    wdmks_device_info_sources = '''
    src/os/win/pa_win_wdmks_utils.c
	'''

    wasapi_sources = '''
	src/hostapi/wasapi/pa_win_wasapi.c
	'''

    asio_sources = '''
    src/hostapi/asio/pa_asio.cpp
    src/hostapi/asio/iasiothiscallresolver.cpp
	'''

    asio_sdk_sources = '''
    ../ASIOSDK2/common/asio.cpp
    ../ASIOSDK2/host/pc/asiolist.cpp
    ../ASIOSDK2/host/asiodrivers.cpp
	'''

    if bld.env.WITH_WMME:
        windows_sources += wmme_sources
        use_defines += ['PA_USE_WMME=1']

    if bld.env.WITH_DIRECTX:
        windows_sources += dsound_sources
        use_defines += ['PA_USE_DS=1']
        if bld.env.WITH_DSOUND_FULL_DUPLEX:
            use_defines += ['PAWIN_USE_DIRECTSOUNDFULLDUPLEXCREATE']

    # relevant for WMME and DSOUND
    if bld.env.WITH_WDMKS_DEVICE_INFO:
        use_defines += ['PAWIN_USE_WDMKS_DEVICE_INFO']
        windows_sources += wdmks_device_info_sources
        uselib_extra += ['UUID']

    if bld.env.WITH_WDMKS:
        windows_sources += wdmks_sources
        use_defines += ['PA_USE_WDMKS=1']
        uselib_extra += ['SETUPAPI']
        uselib_extra += ['KSUSER']
        uselib_extra += ['UUID']

    if bld.env.WITH_WASAPI:
        windows_sources += wasapi_sources
        use_defines += ['PA_USE_WASAPI=1']
        uselib_extra += ['UUID']

    if bld.env.WITH_ASIO:
        windows_sources += asio_sources
        windows_sources += asio_sdk_sources
        use_defines += ['PA_USE_ASIO=1']
        asio_includes = [
            '../ASIOSDK2/common',
            '../ASIOSDK2/host',
            '../ASIOSDK2/host/pc']

    bld.shlib(
        includes=['include', 'src/common', 'src/os/win'] + asio_includes,
        source=common_sources + windows_sources,
        uselib=['OLE', 'WINMM'] + uselib_extra,
        defines=use_defines,
        target='portaudio',
        name='portaudio',
        vnum='2.0.0'
    )

    if bld.env.ENABLE_STATIC:
        bld.stlib(
            includes=['include', 'src/common', 'src/os/win'] + asio_includes,
            source=common_sources + windows_sources,
            uselib=['OLE', 'WINMM'] + uselib_extra,
            defines=use_defines,
            target='portaudio',
            name='portaudio-static',
            vnum='2.0.0'
        )

    if bld.env.WITH_TESTS:
        test_sources = '''
			test/pa_minlat.c
			test/patest1.c
			test/patest_buffer.c
			test/patest_callbackstop.c
			test/patest_clip.c
			test/patest_converters.c
			test/patest_dither.c
			test/patest_hang.c
			test/patest_in_overflow.c
			test/patest_latency.c
			test/patest_leftright.c
			test/patest_longsine.c
			test/patest_many.c
			test/patest_maxsines.c
			test/patest_mono.c
			test/patest_multi_sine.c
			test/patest_out_underflow.c
			test/patest_prime.c
			test/patest_read_record.c
			test/patest_ringmix.c
			test/patest_sine8.c
			test/patest_sine_channelmaps.c
			test/patest_sine_formats.c
			test/patest_sine_srate.c
			test/patest_sine_time.c
			test/patest_start_stop.c
			test/patest_stop.c
			test/patest_stop_playout.c
			test/patest_suggested_vs_streaminfo_latency.c
			test/patest_sync.c
			test/patest_timing.c
			test/patest_toomanysines.c
			test/patest_two_rates.c
			test/patest_underflow.c
			test/patest_wire.c
			test/patest_write_stop.c
			'''.split()

        wmme_test_sources = '''
			test/patest_wmme_find_best_latency_params.c
			test/patest_wmme_low_level_latency_params.c
			'''.split()

        if bld.env.WITH_WMME:
            test_sources += wmme_test_sources

        dsound_test_sources = '''
			test/patest_dsound_find_best_latency_params.c
			test/patest_dsound_low_level_latency_params.c
			test/patest_dsound_surround.c
			'''.split()

        if bld.env.WITH_DIRECTX:
            test_sources += dsound_test_sources

        for test_src in test_sources:

            bld.program(
                includes=['include', 'src/common', 'src/os/win'],
                use=['portaudio'],
                source=test_src,
                uselib=['OLE', 'WINMM'],
                target=os.path.splitext(test_src)[0]
            )

    if bld.env.WITH_EXAMPLES:
        example_sources = '''
			examples/pa_devs.c
			'''.split()

        for example_src in example_sources:

            bld.program(
                includes=['include', 'src/common', 'src/os/win'],
                use=['portaudio'],
                source=example_src,
                uselib=['OLE', 'WINMM'],
                target=os.path.splitext(example_src)[0]
            )

    # install headers

    bld.install_files('${PREFIX}/include', 'include/portaudio.h')

    if bld.env.WITH_WMME:
        bld.install_files('${PREFIX}/include', 'include/pa_win_wmme.h')

    if bld.env.WITH_DIRECTX:
        bld.install_files('${PREFIX}/include', 'include/pa_win_ds.h')

    if bld.env.WITH_WDMKS:
        bld.install_files('${PREFIX}/include', 'include/pa_win_wdmks.h')

    if bld.env.WITH_WASAPI:
        bld.install_files('${PREFIX}/include', 'include/pa_win_wasapi.h')

    if bld.env.WITH_ASIO:
        bld.install_files('${PREFIX}/include', 'include/pa_asio.h')

    # build pkgconfig file

    bld(
        features='subst',
        source='portaudio-2.0.pc.in',
        target='portaudio-2.0.pc',
        install_path='${PREFIX}/lib/pkgconfig',
        dict={'PREFIX': bld.env.PREFIX}
    )
