# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-toolkit

pkgver=1.0.1
_runtime_pkgver=3.1.0

pkgrel=2
pkgdesc='NVIDIA container runtime toolkit'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('BSD')

makedepends=('go')
depends=('libnvidia-container-tools' 'docker>=1:19.03')
conflicts=('nvidia-docker' 'nvidia-container-runtime-hook' 'nvidia-container-runtime<2.0.0')
replaces=('nvidia-container-runtime-hook')

source=("https://github.com/NVIDIA/nvidia-container-runtime/archive/${_runtime_pkgver}.tar.gz")
sha256sums=('9fd1fd6d39e02b1e1cd41219cf8b2e657a4f3c4fad36ee94b397fff0cb9a0865')

_srcdir="nvidia-container-runtime-${_runtime_pkgver}"

prepare() {
  mkdir -p gopath/src
  ln -rTsf "${_srcdir}/toolkit/${pkgname}" "gopath/src/$pkgname"
}

build() {
  GOPATH="${srcdir}/gopath" go install -buildmode=pie -ldflags " -s -w -extldflags=-Wl,-z,now,-z,relro" "$pkgname"
}

package() {
  install -D -m755 "${srcdir}/gopath/bin/${pkgname}" "$pkgdir/usr/bin/${pkgname}"
  pushd "$pkgdir/usr/bin/"
  ln -sf "${pkgname}" "nvidia-container-runtime-hook"
  popd
  install -D -m644 "${_srcdir}/toolkit/config.toml.centos" "$pkgdir/etc/nvidia-container-runtime/config.toml"
  install -D -m755 "${_srcdir}/toolkit/oci-nvidia-hook" "$pkgdir/usr/libexec/oci/hooks.d/oci-nvidia-hook"
  install -D -m644 "${_srcdir}/toolkit/oci-nvidia-hook.json" "$pkgdir/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json"

  install -D -m644 "${_srcdir}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
