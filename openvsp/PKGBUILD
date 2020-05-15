# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=openvsp
pkgver=3.21.1
pkgrel=1
pkgdesc='OpenVSP allows the user to create a 3D model of an aircraft defined by
         common engineering parameters.'
arch=('i686' 'x86_64')
url='http://www.openvsp.org'
license=('NASA OPEN SOURCE AGREEMENT VERSION 1.3')
depends=('cblas'
         'cminpack'
         'code-eli'
         'cpptest'
         'eigen'
         'fltk'
         'freeglut'
         'gcc'
         'glew'
         'glm'
         'libxml2')
optdepends=('doxygen: generate documentation'
            'graphviz: generate documentation'
            'python: python API module'
            'swig: build interface to APIs')
makedepends=('cmake')
provides=('openvsp')
_name=OpenVSP-OpenVSP_${pkgver}
source=("https://github.com/OpenVSP/OpenVSP/archive/OpenVSP_${pkgver}.tar.gz")
sha256sums=('3065e4cd32d4f2f0c7bee40cd9866ee68cd60ae1f64d39ee754902399b340b6e')

prepare() {

  # Add -lcblas to cmake flags
  sed -i -e 's/X_FLAGS} -fPIC/X_FLAGS} -lcblas -fPIC/g' ${srcdir}/${_name}/SuperProject/CMakeLists.txt

}

_buildtype="Release"

build() {

  # Create a build directory
  mkdir -p "${srcdir}/${_name}/SuperProject/build"
  cd "${srcdir}/${_name}/SuperProject/build"

  msg "Starting CMake (build type: ${_buildtype})"

  cmake .. \
        -DCMAKE_BUILD_TYPE=${_buildtype} \
        -DCMAKE_PREFIX_PATH='/usr' \
        -DVSP_USE_SYSTEM_CPPTEST=true \
        -DVSP_USE_SYSTEM_LIBXML2=true \
        -DVSP_USE_SYSTEM_EIGEN=true \
        -DVSP_USE_SYSTEM_CODEELI=true \
        -DVSP_USE_SYSTEM_FLTK=true \
        -DVSP_USE_SYSTEM_GLM=true \
        -DVSP_USE_SYSTEM_GLEW=true \
        -DVSP_USE_SYSTEM_CMINPACK=true

  msg "Building the project"
  make || return 0
}

package() {
  cd "${srcdir}/${_name}/SuperProject/build/OpenVSP-prefix/src/OpenVSP-build/_CPack_Packages/Linux/ZIP/OpenVSP-${pkgver}-Linux"

  msg "Installing files"

  # binary
  mkdir -p ${pkgdir}/usr/bin
  cp vsp vspaero vspscript vspslicer vspviewer ${pkgdir}/usr/bin/

  # misc
  mkdir -p ${pkgdir}/usr/share/${pkgname}
  cp README.md ${pkgdir}/usr/share/${pkgname}
  cp LICENSE ${pkgdir}/usr/share/${pkgname}
  cp -r CustomScripts ${pkgdir}/usr/share/${pkgname}
  cp -r airfoil ${pkgdir}/usr/share/${pkgname}
  cp -r matlab ${pkgdir}/usr/share/${pkgname}
  cp -r scripts ${pkgdir}/usr/share/${pkgname}
  cp -r textures ${pkgdir}/usr/share/${pkgname}

}
