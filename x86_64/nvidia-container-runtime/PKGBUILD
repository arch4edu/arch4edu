# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Julie Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-runtime

# Author's note
# I am so mad that this cannot be a split package with nvidia-container-toolkit
# due to it needing a different pkgver. That said, now that the code for this
# runtime has been moved into the toolkit repo, this file is basically
# identical to nvidia-container-toolkit's PKGBUILD.

pkgver=3.13.1
pkgrel=1

toolkit_ver=1.13.1

pkgdesc='NVIDIA opencontainer runtime fork to expose GPU devices to containers.'
arch=('x86_64')
# see note above.
url='https://github.com/NVIDIA/nvidia-container-toolkit'
license=('APACHE')

makedepends=('go')
depends=('libseccomp' 'nvidia-container-toolkit>=1.9.0')
options=(!lto)

source=("v${pkgver}-${pkgrel}.tar.gz"::"${url}/archive/v${toolkit_ver}.tar.gz")
sha256sums=('76c783143f3a91cc5fd0070a75666f0f4bee4c7153b1af6074037a9b6a94e0c2')

_srcdir="nvidia-container-toolkit-${toolkit_ver}"

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
