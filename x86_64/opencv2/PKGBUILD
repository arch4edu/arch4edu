# Maintainer: Ashok Arora <ashok.maillist@gmail.com>
# Contributor: Johannes Janosovits <johannes@walnutempire.de>
# Contributor: Joshua Schüler <joshua.schueler at gmail dotcom>
# Contributor: Ray Rashif <schiv@archlinux.org>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>


############################################
# Here you have the option to use some CPU
# extensions to speed up opencv
# Only change this if you know what you
# are doing!
############################################

# Use `cat /proc/cpuinfo` to see the extensions your CPU supports

_FORCE_SSE=OFF      # always ON on x64
_FORCE_SSE2=OFF     # always ON on x64

# Set to ON on CPUs newer than approx. 2005
_FORCE_SSE3=OFF

# Set to ON on CPUs since Intel Core 2 or newer/AMD Bulldozer/AMD Fusion
_FORCE_SSSE3=OFF    # also known as SSE4

# Set to ON on CPUs since Intel Core 2 Penryn (older than Nehalem or Sandybridge)
# or on AMDs since K10 (approx. 2009)
_FORCE_SSE41=OFF

# Set to ON on nearly all Intel Core i or AMD since Bulldozer
_FORCE_SSE42=OFF

# Set to ON on Sandybridge or newer/Bulldozer or newer
_FORCE_AVX=OFF

# Set to ON on Haswell or newer
_FORCE_AVX2=OFF

############################################


_pkgbase=opencv
pkgbase=opencv2
pkgname=('opencv2' 'opencv2-samples')
pkgver=2.4.13.6
pkgrel=3
pkgdesc="Open Source Computer Vision Library (Legacy Version)"
arch=('i686' 'x86_64')
license=('BSD')
url="http://opencv.org/"
depends=('intel-tbb' 'openexr' 'xine-lib' 'libdc1394' 'gtkglext')
makedepends=('cmake' 'python2-numpy' 'mesa')
optdepends=('opencv-samples'
            'eigen2'
            'libcl: For coding with OpenCL'
            'python2-numpy: Python 2.x interface')
options=('staticlibs')
source=("$pkgver.zip::https://codeload.github.com/opencv/opencv/zip/$pkgver")
sha256sums=('8fbe6005d2266e4a725a5ef7a27365d763ce4ad5a7f38045288a3cad8a18d759')

_cmakeopts=('-DWITH_CUDA=OFF' # Disable CUDA for now because GCC 6.1.1 and nvcc don't play along yet
            '-DWITH_OPENCL=ON'
            '-DWITH_OPENGL=ON'
            '-DWITH_TBB=ON'
            '-DWITH_XINE=ON'
            '-DWITH_GSTREAMER=OFF'
            '-DBUILD_WITH_DEBUG_INFO=OFF'
            '-DUILD_TESTS=OFF'
            '-DBUILD_PERF_TESTS=OFF'
            '-DBUILD_EXAMPLES=ON'
            '-DINSTALL_C_EXAMPLES=ON'
            '-DINSTALL_PYTHON_EXAMPLES=ON'
            '-DCMAKE_BUILD_TYPE=Release'
            '-DCMAKE_INSTALL_PREFIX=/usr'
            '-DCMAKE_SKIP_RPATH=ON'
            '-DBUILD_JASPER=ON')

# SSE only available from Pentium 3 onwards (i686 is way older)
[[ "$CARCH" = 'i686' ]] && \
  _cmakeopts+=("-DENABLE_SSE=$_FORCE_SSE"
               "-DENABLE_SSE2=$_FORCE_SSE2"
               "-DENABLE_SSE3=$_FORCE_SSE3")

# all x64 CPUs support SSE2 but not SSE3
[[ "$CARCH" = 'x86_64' ]] && \
  _cmakeopts+=("-DENABLE_SSE3=$_FORCE_SSE3"
               "-DENABLE_SSSE4=$_FORCE_SSSE3" #(sic!)
               "-DENABLE_SSE41=$_FORCE_SSE41"
               "-DENABLE_SSE42=$_FORCE_SSE42"
               "-DENABLE_AVX=$_FORCE_AVX"
               "-DENABLE_AVX2=$_FORCE_AVX2")
prepare() {
  cd "$_pkgbase-$pkgver/"
  # https://stackoverflow.com/questions/46884682/error-in-building-opencv-with-ffmpeg
  sed "1i\#define AVFMT_RAWPICTURE 0x0020" -i modules/highgui/src/cap_ffmpeg_impl.hpp
  sed "1i\#define CODEC_FLAG_GLOBAL_HEADER AV_CODEC_FLAG_GLOBAL_HEADER" -i modules/highgui/src/cap_ffmpeg_impl.hpp
  sed "1i\#define AV_CODEC_FLAG_GLOBAL_HEADER (1 << 22)" -i modules/highgui/src/cap_ffmpeg_impl.hpp
  sed "/prototypes/d" -i cmake/OpenCVCompilerOptions.cmake
}

build() {
  export CXXFLAGS+=" -std=c++14 -DTBB_SUPPRESS_DEPRECATED_MESSAGES"
  cmake -S "$srcdir/$_pkgbase-$pkgver" -B build "${_cmakeopts[@]}"
  make -C build
}

package_opencv2() {
  provides=("opencv=$pkgver")
  conflicts=('opencv')

  make -C build DESTDIR="$pkgdir" install

  # install license file
  install -Dm644 "$srcdir/$_pkgbase-$pkgver/LICENSE" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  cd "$pkgdir/usr/share"

  # separate samples package; also be -R friendly
  if [[ -d OpenCV/samples ]]; then
    mv OpenCV/samples "$srcdir/$_pkgbase-samples"
    mv OpenCV $_pkgbase # otherwise folder naming is inconsistent
  elif [[ ! -d OpenCV ]]; then
    warning "Directory naming issue; samples package may not be built!"
  fi
}

package_opencv2-samples() {
  pkgdesc+=" (samples)"
  depends=("opencv2=$pkgver") # sample codes change with lib/API
  unset optdepends
  conflicts=('opencv-samples')

  install -dm755 "$pkgdir/usr/share/$_pkgbase"
  cp -r "$srcdir/opencv-samples" "$pkgdir/usr/share/opencv/samples"

  # install license file
  install -Dm644 "$srcdir/opencv-$pkgver/LICENSE" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
