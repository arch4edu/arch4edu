# Maintainer: fromtheeast710 <theeast710@proton.me>
# Contributor: physkets <physkets // at // tutanota dot com>
# Contributor: xpt <user.xpt@gmail.com>
# Contributor: yuhldr <yuhldr@qq.com>

pkgname=lammps
pkgver=20250722
_pkgver="stable_22Jul2025"
pkgrel=1
pkgdesc="Public development project of the LAMMPS MD software package"
url="https://lammps.org"
arch=('x86_64')
license=('GPL')
depends=('fftw' 'openmpi' 'ffmpeg' 'libpng' 'python')
makedepends=('cmake>=3.1' 'python-pip' 'python-build')
conflicts=('lammps-git')
provides=('lammps')
source=("https://github.com/${pkgname}/${pkgname}/archive/refs/tags/${_pkgver}.tar.gz")
sha256sums=('38d7ab508433f33a53e11f0502aa0253945ce45d5595baf69665961c0a76da26')
optdepends=('clang' 'python-mpi4py')

prepare() {
    cd "${pkgname}-${_pkgver}"

    rm -rf build
    mkdir -p build
}

build() {
    cd ${pkgname}-${_pkgver}/build

    cmake \
        -D PKG_MOLECULE=on \
        -D PKG_PYTHON=on \
        -D PKG_PHONON=on \
        -D PKG_KSPACE=on \
        -D PKG_MANYBODY=on \
        -D LAMMPS_EXCEPTIONS=on \
        -D BUILD_LIB=on \
        -D BUILD_SHARED_LIBS=on \
        -D CMAKE_BUILD_TYPE=Release \
        -D CMAKE_INSTALL_PREFIX="/usr" \
        -D CMAKE_INSTALL_LIBDIR="lib" \
        -D CMAKE_INSTALL_LIBEXECDIR="/usr/lib" \
    ../cmake

    # -D BUILD_LAMMPS_GUI=on \

    cmake --build . -j $(($(nproc) - 1))

    # python lib
    cd ../python/
    rm -rf dist
    python -m build


    # phana
    # cd ../tools/phonon/
    # cmake -S . -B build
    # cmake --build build
}

package() {
    cd ${pkgname}-${_pkgver}/build
    make DESTDIR="${pkgdir}" install

    # mkdir -p "${pkgdir}/usr/share/examples/lammps"
    # cp -r "../examples/." "${pkgdir}/usr/share/examples/lammps/"
    # cp -r "../python/examples" "${pkgdir}/usr/share/examples/lammps/python/more"
    # find "${pkgdir}/usr/share/examples/lammps/" -type f -exec chmod 644 '{}' +

    install -Dm644 "../tools/vim/lammps.vim" "${pkgdir}/usr/share/vim/vimfiles/syntax/lammps.vim"
    install -Dm644 "../tools/vim/filetype.vim" "${pkgdir}/usr/share/vim/vimfiles/ftdetect/lammps.vim"

    # install -Dm755 "../tools/phonon/build/phana" "${pkgdir}/usr/bin/phana"

    # python lib
    PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps ../python/dist/*.whl

    # 遍历以 lib 开头的文件
    # for file in "${pkgdir}/usr/lib/lib"*; do
    #     # 如果文件不是 liblammps，则删除
    #     [[ "$(basename "$file")" == liblammps* ]] || rm -f "$file"
    # done
    # rm -f ${pkgdir}/usr/lib/ld-linux*


}
