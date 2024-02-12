# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: Julie Shapiro <jshapiro at nvidia dot com>
# Contributor: Kien Dang <mail at kien dot ai>
pkgname=('libnvidia-container' 'libnvidia-container-tools')
pkgbase=libnvidia-container
pkgver=1.14.5
pkgrel=2
_nvmodver=495.44
pkgdesc="NVIDIA container runtime library"
arch=('x86_64')
url='https://github.com/NVIDIA/libnvidia-container'
license=('BSD-3-Clause AND Apache-2.0 AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND GPL-2.0-only')
depends=('libcap' 'libelf' 'libseccomp')
makedepends=('bmake' 'git' 'go' 'libtirpc' 'lsb-release' 'rpcsvc-proto')
_commit=870d7c5d957f5780b8afa57c4d5cc924d4d9ed26  # tags/v1.14.5^0
source=("git+https://github.com/NVIDIA/libnvidia-container.git#commit=${_commit}"
        "nvidia-modprobe-${_nvmodver}.tar.gz::https://github.com/NVIDIA/nvidia-modprobe/archive/${_nvmodver}.tar.gz"
        'no-manual-debuginfo.patch')
noextract=("nvidia-modprobe-${_nvmodver}.tar.gz")
sha256sums=('SKIP'
            'ae6e9c7e6b43368945c28f6b8b6d0d7cc36ee7e1be8955a009a1cb189e46de92'
            '4c0ffca77dee2d0c98ea92716b5c3cff0d41f974000fea29ca905435d3acbe8e')

# v1.14.4 and v1.14.5 are identical

#pkgver() {
#  cd "$pkgbase"
#  git describe --tags | sed 's/^v//;s/-/+/g'
#}

prepare(){
  cd "$pkgbase"

  # NVIDIA modprobe configuration based on & mk/nvidia-modprobe.mk
  mkdir -p "deps/src/nvidia-modprobe-${_nvmodver}"
  bsdtar -xvf "$srcdir/nvidia-modprobe-${_nvmodver}.tar.gz" -C "deps/src/nvidia-modprobe-${_nvmodver}/" \
    --strip-components=1 -xz "nvidia-modprobe-${_nvmodver}/modprobe-utils"
  touch "deps/src/nvidia-modprobe-${_nvmodver}/.download_stamp"
  patch -d "deps/src/nvidia-modprobe-${_nvmodver}" -p1 < mk/nvidia-modprobe.patch
  patch -Np1 -i ../no-manual-debuginfo.patch
}

build(){
  cd "$pkgbase"
  make prefix=/usr WITH_LIBELF=yes WITH_TIRPC=yes
}

package_libnvidia-container() {
  cd "$pkgbase"
  make prefix=/usr DESTDIR="$pkgdir" install

  # remove empty leftover directory
  rm -rf "$pkgdir/usr/lib/debug"

  # remove CLI for tools
  rm -rf "$pkgdir/usr/bin"

  # remove duplicate licenses
  rm -rf "$pkgdir/usr/share"

  # install BSD-3-Clause license
  install -Dm644 NOTICE -t "$pkgdir/usr/share/licenses/$pkgname/"
}

package_libnvidia-container-tools() {
  pkgdesc+=" (command-line tools)"
  depends=('libnvidia-container')

  cd "$pkgbase"
  make prefix=/usr DESTDIR="$pkgdir" install

  # remove lib and include
  rm -rf "$pkgdir"/usr/{include,lib}

  # remove duplicate licenses
  rm -rf "$pkgdir/usr/share"

  # install BSD-3-Clause license
  install -Dm644 NOTICE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
