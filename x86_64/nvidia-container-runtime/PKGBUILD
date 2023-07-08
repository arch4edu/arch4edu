# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Julie Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-runtime

# Author's note
# I am so mad that this cannot be a split package with nvidia-container-toolkit
# due to it needing a different pkgver. That said, now that the code for this
# runtime has been moved into the toolkit repo, this file is basically
# identical to nvidia-container-toolkit's PKGBUILD.

pkgver=3.13.1
pkgrel=2

_toolkit_ver=1.13.3

pkgdesc='NVIDIA opencontainer runtime fork to expose GPU devices to containers.'
arch=('x86_64')
# see note above.
url='https://github.com/NVIDIA/nvidia-container-toolkit'
license=('APACHE')

makedepends=('go')
depends=('libseccomp' 'nvidia-container-toolkit>=1.9.0')
options=(!lto)

source=("${pkgname}-${pkgver}-${pkgrel}.tar.gz"::"${url}/archive/v${_toolkit_ver}.tar.gz")
sha256sums=('6f9199bf4a9b1bec17cb6a452e0771f7dc3bbf32234491eddfb7796130eac52a')

_srcdir="nvidia-container-toolkit-${_toolkit_ver}"

build() {
  cd "${_srcdir}"

  mkdir bin

  GO111MODULE=auto \
  GOPATH="${srcdir}/gopath" \
  GOOS=linux \
  go build -v \
    -modcacherw \
    -buildmode=pie \
    -gcflags "all=-trimpath=${PWD}" \
    -asmflags "all=-trimpath=${PWD}" \
    -o bin \
    "./..."
    # using LDFLAGS is busted because -Wl breaks linking to cuDriver* for some reason :(
    #-ldflags "-s -w -extldflags \"${LDFLAGS}\"" \
    # only go > 1.13
    # -trimpath \

  # go leaves a bunch of local stuff with 0400, making it break future `makepkg -C` _grumble grumble_
  GO111MODULE=auto \
  GOPATH="${srcdir}/gopath" \
  go clean -modcache
}

package_nvidia-container-runtime() {
  install -D -m755 "${_srcdir}/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -D -m644 "${_srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
