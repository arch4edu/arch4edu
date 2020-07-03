# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-toolkit

pkgver=1.1.2
pkgrel=2

pkgdesc='NVIDIA container runtime toolkit'
arch=('x86_64')
url='https://github.com/NVIDIA/container-toolkit'
license=('Apache')

makedepends=('go')
depends=('libnvidia-container-tools')
conflicts=('nvidia-container-runtime-hook' 'nvidia-container-runtime<2.0.0')
replaces=('nvidia-container-runtime-hook')

source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('8f103d3fdc1a790eb5c883c0d27f9482c31c4da2adad6413dc6d86902d991ded')

_srcdir="nvidia-container-toolkit-${pkgver}"
_golang_pkg_path="github.com/NVIDIA/container-toolkit/pkg"

build() {
  cd "${_srcdir}"
  GOPATH="${srcdir}/gopath" \
  go build -v \
    -buildmode=pie \
    -gcflags "all=-trimpath=${PWD}" \
    -asmflags "all=-trimpath=${PWD}" \
    -ldflags "-s -w -extldflags ${LDFLAGS}" \
    -o "${pkgname}" \
    "${_golang_pkg_path}"
    # -trimpath \  # only go > 1.13
    #-ldflags " -s -w -extldflags=-Wl,-z,now,-z,relro" \

  # go leaves a bunch of local stuff with 0400, making it break future `makepkg -C` _grumble grumble_
  GOPATH="${srcdir}/gopath" \
  go clean -modcache
}

package() {
  install -D -m755 "${_srcdir}/${pkgname}" "$pkgdir/usr/bin/${pkgname}"
  pushd "$pkgdir/usr/bin/"
  ln -sf "${pkgname}" "nvidia-container-runtime-hook"
  popd
  install -D -m644 "${_srcdir}/config/config.toml.centos" "$pkgdir/etc/nvidia-container-runtime/config.toml"

  install -D -m644 "${_srcdir}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
