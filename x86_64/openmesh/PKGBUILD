# Maintainer: Chirantan Ekbote <chirantan.ekbote at gmail.com>
# Contributor: Brian Schubert <bewschubert@gmail.com>

_build_doc=OFF
_build_apps=ON
_pkgname=OpenMesh
pkgname=openmesh
pkgver=11.0.0
pkgrel=1
pkgdesc="A generic and efficient data structure for representing and manipulating polygonal meshes"
arch=('i686' 'x86_64')
url="http://www.openmesh.org"
license=('BSD-3-Clause')
depends=(
	'gcc-libs'
	'glibc'
	'libglvnd'
	'qt5-base'
)
source=("${pkgname}-${pkgver}.tar.bz2::https://www.graphics.rwth-aachen.de/media/${pkgname}_static/Releases/${pkgver%.*}/${_pkgname}-${pkgver}.tar.bz2"
    doc-install.patch)

b2sums=(
	'5f4eb34365cfeedab8e5de818db955ed1a5ab42d2289e9ab686efda0f3057462848bdee0b53af0f81ddc6ea388ef64eecde923f468beb2078a77f2dff5c04753'
	'02336dbec8dddce14fdd6aba042ff356ca3cc5d783269bb8cf9b1f2ab75c8a525fd43fb44e61341db210cdbcb048f6771a3c8c8fd86ed6e46de74c8e0dc60d4a'
)

if [[ "${_build_doc}" == "ON" && "${_build_apps}" == "ON" ]]; then
    makedepends=('cmake' 'qt5-base' 'graphviz' 'doxygen')
elif [[ "${_build_doc}" == "ON" ]]; then
    makedepends=('cmake' 'graphviz' 'doxygen')
elif [[ "${_build_apps}" == "ON" ]]; then
    makedepends=('cmake' 'qt5-base')
else
    makedepends=('cmake')
fi

prepare() {
  cd "${srcdir}/OpenMesh-${pkgver}" || exit 1
    if [[ "${_build_doc}" == "ON" ]]; then
	patch -Np1 -i "${srcdir}"/doc-install.patch
    fi
}

build() {
    cd "${srcdir}/OpenMesh-${pkgver}" || exit 1
    mkdir -p build && cd build || exit 1
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_APPS=${_build_apps} \
        ..
    make

    if [[ "${_build_doc}" == "ON" ]]; then
	make doc
    fi
}

package() {
    cd "${srcdir}"/OpenMesh-${pkgver}/build || exit 1
    make DESTDIR="${pkgdir}" install

    # install licenses
    mkdir -p "${pkgdir}"/usr/share/licenses/openmesh/
    install -D -m644 ../LICENSE \
        "${pkgdir}"/usr/share/licenses/openmesh/
}
