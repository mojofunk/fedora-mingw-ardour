What follows are instructions to build all the necessary library dependencies
for a Windows version of Ardour on Fedora 24 using using a gcc/mingw64
cross-compiler toolchain.

The packages contained in this repository are all the packages that
have not yet been included in Fedora but most already are thankfully.

## Getting the Sources

The Sources for these packages are not included in this repository
and have to be downloaded separately and put in the SOURCES directory
of the rpmbuild root.

These packages should use where possible the versions that are in the native
Fedora packages so an easy way to download the correct sources is with
yumdownloader and then extract the source from the package

e.g `$yumdownloader --source flac`

or in more recent Fedora versions

`$dnf download --source flac`

## Building Packages

Put the source for a package in the SOURCES directory, then from within the
SPEC directory use rpmbuild to build the RPM package

e.g `$rpmbuild -ba mingw-libsndfile.spec`

If there were no errors the packages will be placed in RPMS/noarch and need to
be installed

e.g `$dnf install mingw*libsndfile`

## A custom RPM build directory

You may also want to use a ~/.rpmmacros file to set(perhaps temporarily) the
path to the rpmbuild root dir to use to build rpm packages, rather than the
default ~/rpmbuild

## Packages to Install or Build and Install in order.

`$dnf/yum group install 'Development Tools'`
`$dnf/yum group install 'RPM Development Tools'`

Wine is needed to needed to run some tests during the configure process of some
packages

`$dnf install wine`

`$dnf install mingw*gcc mingw*gcc-c++ mingw*libogg`

`$dnf install mingw*pkg-config mingw*flac mingw*libvorbis`

`build/install mingw-libsndfile`
`build/install mingw-libsamplerate`

Install all the Gtk+ related mingw packages

`$dnf install mingw*gtkmm24`

I think Intltool is required to build gtk2-engines?

`$dnf install intltool`

`$dnf install mingw*libxml2`

build/install mingw-gtk2-engines <- provides clearlooks

Clone the portaudio repository at https://github.com/mojofunk/portaudio so that
it is located in the same directory as the fedora-mingw-ardour repo, checkout
the "waf" branch and run the "update-fedora-mingw-rpm.sh" script.

build/install mingw-portaudio

To build with ASIO support place the ASIO2SDK in the rpm SOURCES directory and
build using --with asio

e.g $rpmbuild -ba mingw-portaudio.spec --with asio

It is no longer necessary to build a pthreads implementation with Fedora>19 as
gcc/mingw includes the winpthreads library.

`$dnf install mingw*libgnurx`

If you choose to build with support for JACK then an unreleased version is
required from:

https://github.com/jackaudio/jack2.git

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

# Other Optional Packages

build/install mingw*cppunit, if tests enabled
install mingw*gdb, for debugging
