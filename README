What follows are instructions to build all the necessary library dependencies
for a Windows version of Ardour on Fedora 24 using using a gcc/mingw64
cross-compiler toolchain.

The packages contained in this repository are all the packages that
have not yet been included in Fedora but most already are thankfully.

The Sources for these packages are not included in this repository
and have to be downloaded separately and put in the SOURCES directory
of the rpmbuild root.

These packages should use where possible the versions that are in the native
Fedora packages so an easy way to download the correct sources is with
yumdownloader and then extract the source from the package

e.g $yumdownloader --source flac

or in more recent Fedora versions

$dnf download --source flac

You may also want to use a ~/.rpmmacros file to set(perhaps temporarily) the
path to the rpmbuild root dir to use to build rpm packages, rather than the
default ~/rpmbuild

If you choose to build with support for JACK then an unreleased version is
required from:
	
https://github.com/jackaudio/jack2.git

These packages should be built and or installed in this order:

install wine, needed to run some tests during the configure process

install mingw*gcc

install mingw*gcc-c++

install mingw*libogg

yum group install 'Development Tools'
yum group install 'RPM Development Tools'

install mingw*pkg-config

install mingw*flac <- requires libogg

install mingw*libvorbis

build/install mingw-libsndfile <- requires flac, vorbis
build/install mingw-libsamplerate <- requires sndfile for examples?

install mingw*gtkmm24, this will pull in all the gtk+ deps etc

install intltool

install mingw*libxml2

build/install mingw-gtk2-engines <- provides clearlooks

Clone the portaudio repository at https://github.com/mojofunk/portaudio so that
it is located in the same directory as the fedora-mingw-ardour repo, checkout
the "waf" branch and run the "update-fedora-mingw-rpm.sh" script.

build/install mingw-portaudio

To build with ASIO support place the ASIO2SDK in the rpm SOURCES directory and
build using --with asio

e.g $rpmbuild -ba mingw-portaudio.spec --with asio

# no longer necessary with Fedora>19 as gcc/mingw includes the winpthreads
library

#install mingw*pthreads

install mingw*libgnurx

If building with support for JACK backend

build/install mingw-jack-audio-connection-kit

install mingw*fftw

build/install mingw-liblo

install mingw*boost

install mingw*curl

install cmake

install mingw*taglib

build/install mingw-vamp-plugin-sdk

build/install mingw-rubberband

build/install mingw-aubio

build/install mingw-serd

build/install mingw-sord

build/install mingw-lv2

build/install mingw-sratom

build/install mingw-lilv

build/install mingw-libltc

Optional

build/install mingw*cppunit, if tests enabled
install mingw*gdb, for debugging
