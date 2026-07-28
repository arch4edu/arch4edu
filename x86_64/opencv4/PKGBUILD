# Maintainer: aur.chaotic.cx

_pkgname="opencv4"
pkgname="$_pkgname"
pkgver="4.14.0"
pkgrel=1
pkgdesc="Open Source Computer Vision Library (version 4.x)"
url="https://github.com/opencv/opencv"
license=('Apache-2.0')
arch=('x86_64')

depends=(
  abseil-cpp
  cblas
  ffmpeg
  freetype2
  glib2
  gst-plugins-base
  gst-plugins-base-libs
  gstreamer
  harfbuzz
  lapack
  libdc1394
  libgcc
  libglvnd
  libjpeg-turbo
  libjxl
  libpng
  libstdc++
  libtiff
  libwebp
  openexr
  openjpeg2
  protobuf
  tbb
  verdict
  zlib
)
makedepends=(
  ant
  cmake
  eigen
  fast_float
  fmt
  glew
  hdf5
  java-environment
  lapacke
  mesa
  ninja
  nlohmann-json
  openmpi
  pugixml
  python-numpy
  python-setuptools
  qt6-5compat
  vtk
)
optdepends=(
  'glew: for the viz module'
  'hdf5: for the HDF5 module'
  'java-runtime: Java interface'
  'opencl-icd-loader: For coding with OpenCL'
  'qt6-base: for the HighGUI module'
  'vtk: for the viz module'
)

_pkgsrc="opencv-$pkgver"
_pkgsrc_contrib="opencv_contrib-$pkgver"
_pkgext="tar.gz"
source=(
  "$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/$pkgver.$_pkgext"
  "$_pkgsrc_contrib.$_pkgext"::"${url}_contrib/archive/refs/tags/$pkgver.$_pkgext"
  vtk9.patch
  fix-cuda-flags.patch
  fix-std.patch
)
sha256sums=('ee8fb9b30eb60850431b4656447080e3737b56e45719c92b67f245950609f86e'
            '4f17abd1bc7f88e19c3380c8de7cbf2d863aced5b5ee8d8934cc7902b67d42c9'
            'f35a2d4ea0d6212c7798659e59eda2cb0b5bc858360f7ce9c696c77d3029668e'
            '95472ecfc2693c606f0dd50be2f012b4d683b7b0a313f51484da4537ab8b2bfe'
            'c05fe7572ee5193cf3de7f02a500f446f3457ec20c315590a326bf1bfb5552cc')

# https://gitlab.archlinux.org/archlinux/packaging/packages/kdenlive/-/issues/8
options=('!lto')

prepare() {
  # Don't require all vtk optdepends
  patch -d "$_pkgsrc" -Np1 -F100 -i ../vtk9.patch

  # OpenCV passes all CXXFLAGS to nvcc through -Xcompiler, which does not work for '-Wp,something' flags
  # We remove the -Xcompiler and pass our CXXFLAGS through cmake's CUDAFLAGS
  patch -d "$_pkgsrc" -Np1 -F100 -i ../fix-cuda-flags.patch

  patch -d "$_pkgsrc_contrib" -Np1 -F100 -i ../fix-std.patch
}

build() {
  export JAVA_HOME="/usr/lib/jvm/default"
  local cmake_options=(
    -B build
    -S "$_pkgsrc"
    -G Ninja
    -DCMAKE_BUILD_TYPE=Release
    -DCMAKE_INSTALL_PREFIX=/usr
    -DCMAKE_INSTALL_LIBDIR="lib/$_pkgname"
    -DCMAKE_CXX_STANDARD=17
    -Wno-dev

    -DBUILD_EXAMPLES=OFF
    -DINSTALL_C_EXAMPLES=OFF
    -DINSTALL_PYTHON_EXAMPLES=OFF

    -DWITH_OPENCL=ON
    -DWITH_OPENGL=ON
    -DOpenGL_GL_PREFERENCE=LEGACY
    -DWITH_TBB=ON
    -DWITH_VULKAN=ON
    -DWITH_QT=ON
    -DWITH_JPEGXL=ON
    -DBUILD_TESTS=OFF
    -DBUILD_PERF_TESTS=OFF
    -DBUILD_PROTOBUF=OFF
    -DPROTOBUF_UPDATE_FILES=ON
    -DCPU_BASELINE_DISABLE=SSE3
    -DCPU_BASELINE_REQUIRE=SSE2
    -DOPENCV_EXTRA_MODULES_PATH="$srcdir/$_pkgsrc_contrib/modules"
    -DOPENCV_SKIP_PYTHON_LOADER=ON
    # cmake's FindLAPACK doesn't add cblas to LAPACK_LIBRARIES, so we need to specify them manually
    -DLAPACK_LIBRARIES="/usr/lib/liblapack.so;/usr/lib/libblas.so;/usr/lib/libcblas.so"
    -DLAPACK_CBLAS_H=/usr/include/cblas.h
    -DLAPACK_LAPACKE_H=/usr/include/lapacke.h
    -DOPENCV_GENERATE_PKGCONFIG=ON
    -DOPENCV_ENABLE_NONFREE=ON
    -DOPENCV_JNI_INSTALL_PATH=lib
    -DOPENCV_GENERATE_SETUPVARS=OFF
    -DEIGEN_INCLUDE_PATH=/usr/include/eigen3
    -Dprotobuf_MODULE_COMPATIBLE=ON
    -DHDF5_NO_FIND_PACKAGE_CONFIG_FILE=ON

    -DBUILD_WITH_DEBUG_INFO=ON
  )

  cmake ${cmake_options[@]}
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  local _lib
  for _lib in "$pkgdir/usr/lib/$_pkgname"/libopencv*.so.[0-9]*; do
    ln -sf "$_pkgname/${_lib##*/}" "$pkgdir/usr/lib/${_lib##*/}"
  done

  mv "$pkgdir/usr/lib/$_pkgname/cmake" "$pkgdir/usr/lib/"
  mv "$pkgdir/usr/lib/$_pkgname/pkgconfig" "$pkgdir/usr/lib/"

  rm -r "$pkgdir"/usr/bin/
  rm -r "$pkgdir"/usr/lib/python3*
}
