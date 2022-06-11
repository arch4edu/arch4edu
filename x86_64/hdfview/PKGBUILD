# Maintainer  : Chris Billington <chrisjbillington>
# Maintainer  : Martin Diehl <MartinDiehl>
# Maintainer  : Georgios Eleftheriou <eleftg>
# Contributor : Martin Wimpress <code@flexion.org>
# Contributor : Nick Pope
# Contributor : Bryce Nordgren <bnordgren at gmail dot com>

pkgname=hdfview
_pkgname=HDFView
pkgver=3.1.0
_pkgver=${pkgver::-2}
pkgrel=1
pkgdesc="a GUI browser for reading hdf5 files"
arch=('x86_64')
url="https://www.hdfgroup.org/downloads/hdfview/"
license=('custom')
depends=('hdf5-java' 'hdf4')
replaces=('hdfview-beta')
conflicts=('hdfview-beta')
makedepends=('ant' 'java-environment')
options=(!strip)
source=("https://support.hdfgroup.org/ftp/HDF5/releases/HDF-JAVA/${pkgname}-${_pkgver}/src/${pkgname}-${pkgver}.tar.gz"
        build.patch
        ${_pkgname}.desktop
        HDF_logo.svg)
sha512sums=(
    'ae9b180c0da2b4b9a39189a7e42068435e29802469488b5880c4eea6e9cc4a63ad19b5c90529e55cbd62e4085379259782d404105b85ec52b837196fd43701a0'
    '18a20af53ea2c075a26e22dbab6d7cecb67bead97db49569963e60d589c59f183ad97e796f0a2b67b59cdd311ff2831a134d69ee560a50c2ff8e821472ac82cb'
    'c92d8cd4818feabb996b43c81e4e554e16f8120c80c73a5b7cc8bb2c4c4a59bdd47d42b19ec7a3454f855155ba17b65631e7016f891f29ef4ee8fd4ee45caf90'
    '649eb81f33a3b38a7ae2ee9a7f286ffa489d0bd7a9f37a0face64fe7956863dcab2131be3792c45dc03b1a6955fda2b37d168698922e938b73c90d24fee7a8c4')

prepare() {
    cd "${pkgname}-${pkgver}"
    patch --forward --strip=1 --input="${srcdir}/build.patch"
}

build() {
    # workaround for java exception thrown @ build.xml:838
    # [...] error=7 chmod  [...] argument list too long
    # when building with java 10
    ulimit -s unlimited

    cd "${pkgname}-${pkgver}"
    HDFLIBS=/opt/hdf4 HDF5LIBS=/usr ant package
}

package() {
    cd "${pkgname}-${pkgver}"
    mkdir "${pkgdir}/opt"
    cp -a "build/dist/${_pkgname}-${pkgver}-Linux.sh" "${pkgdir}/opt"
    cd "${pkgdir}/opt"

    # Make extraction non interactive
    sed -i 's/interactive=TRUE/interactive=FALSE/' ${_pkgname}-${pkgver}-Linux.sh
    sed -i 's/cpack_skip_license=FALSE/cpack_skip_license=TRUE/' ${_pkgname}-${pkgver}-Linux.sh

    ./${_pkgname}-${pkgver}-Linux.sh
    rm "${_pkgname}-${pkgver}-Linux.sh"

    # use default java
    rm -rf ${pkgdir}/opt/${_pkgname}/${pkgver}/jre
    sed -i 's:export JAVABIN=$INSTALLDIR/jre/bin:export JAVABIN=/usr/lib/jvm/default-runtime/bin:' ${pkgdir}/opt/${_pkgname}/${pkgver}/hdfview.sh

    mkdir -p "${pkgdir}/usr/bin"

    # Desktop files, icons, wrappers and license
    echo "#!/usr/bin/env bash" > "${pkgdir}/usr/bin/hdfview"
    echo "/opt/HDFView/${pkgver}/hdfview.sh "'-root $PWD "$@"' >> "${pkgdir}/usr/bin/hdfview"
    chmod 755 "${pkgdir}/usr/bin/hdfview"
    install -D -m 644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
    install -D -m 644 "${srcdir}/HDF_logo.svg" "${pkgdir}/usr/share/pixmaps/HDF_logo.svg"
    install -D -m 644 "${srcdir}/${pkgname}-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
