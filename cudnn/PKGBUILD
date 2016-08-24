# Maintainer: Benjamin Chrétien <chretien dot b +aur at gmail dot com>
pkgname=cudnn
pkgver=5.1.3
pkgrel=1
pkgdesc="NVIDIA CUDA Deep Neural Network library"
arch=('x86_64')
url="https://developer.nvidia.com/cuDNN"
license=('proprietary')
depends=('cuda')
source=()
sha256sums=()

_cudnnSrcDir="$(realpath .)"
_cudnnSrcName="cudnn-7.5-linux-x64-v5.1-rc.tgz"
_cudnnSha256="40d506d0a8a00a3faccce1433346806b8cd2535683b6f08a63683ce6e474419f"

prepare() {
  echo "###################################################################"
  echo "# cuDNN is only available to registered CUDA developers.          #"
  echo "# Register on the website, and download the cuDNN source tarball. #"
  echo "###################################################################"
  echo

  while [ ! -f "${_cudnnSrcDir}/${_cudnnSrcName}" ]; do
    echo "Error: ${_cudnnSrcName} not found in $(realpath ${_cudnnSrcDir})"
    echo -n "Enter the directory containing the cuDNN source tarball ${_cudnnSrcName}: "
    read _cudnnSrcDir
  done

  # Check for file validity
  sha256sum -c <(printf "${_cudnnSha256}  ${_cudnnSrcDir}/${_cudnnSrcName}\n") || return 1

  # Untar
  mkdir -p "${srcdir}/${pkgname}-${pkgver}"
  tar -xzvf "${_cudnnSrcDir}/${_cudnnSrcName}" -C "${srcdir}/${pkgname}-${pkgver}"
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  mkdir -p "${pkgdir}/opt"
  cp -r cuda "${pkgdir}/opt"
}

# vim: ft=sh syn=sh et
