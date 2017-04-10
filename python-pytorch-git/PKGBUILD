# Maintainer: Stephen Zhang <zsrkmyn at gmail dot com>

pkgbase="python-pytorch-git"
pkgname=("python-pytorch-git" "python2-pytorch-git")
_pkgname="pytorch"
pkgver=0.1.10.r46.gbe6322e4
pkgrel=1
pkgdesc="Tensors and Dynamic neural networks in Python with strong GPU acceleration"
arch=('x86_64')
url="https://github.com/pytorch/pytorch"
license=('BSD')
makedepends=('python' 'python-setuptools' 'python2' 'python2-setuptools' 'gcc5' 'cmake')
depennds=('cuda' 'cudnn')
source=("git://github.com/pytorch/pytorch")
sha256sums=('SKIP')

pkgver () {
  cd "${_pkgname}"
  (
    set -o pipefail
    git describe --tag 2>/dev/null | sed -e 's/\([^-]*-g\)/r\1/;s/-/./g' -e 's/^v//g'
  )
}


prepare() {
  cd "$srcdir/"

  cp -a "${_pkgname}" "${_pkgname}-py2"
  cd "${_pkgname}"
  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
      -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
      -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
      -i $(find . -name '*.py')
}

build() {
  msg "Building Python 2"
  cd "$srcdir/${_pkgname}-py2"
  CC=gcc-5 \
  CXX=g++-5 \
  WITH_CUDA=1 \
  CUDA_HOME=/opt/cuda \
  WITH_CUDNN=1 \
  CUDNN_LIB_DIR=/opt/cuda/lib64 \
  CUDNN_INCLUDE_DIR=/opt/cuda/include \
  python2 setup.py build

  msg "Building Python 3"
  cd "$srcdir/${_pkgname}"
  CC=gcc-5 \
  CXX=g++-5 \
  WITH_CUDA=1 \
  CUDA_HOME=/opt/cuda \
  WITH_CUDNN=1 \
  CUDNN_LIB_DIR=/opt/cuda/lib64 \
  CUDNN_INCLUDE_DIR=/opt/cuda/include \
  python setup.py build
}

package_python2-pytorch-git() {
  conflicts=('python2-pytorch')
  provides=('python2-pytorch')
  depends+=('python2' 'python2-yaml' 'python2-numpy')
  cd "$srcdir/${_pkgname}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1 --skip-build
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-pytorch-git() {
  conflicts=('python-pytorch')
  provides=('python-pytorch')
  depends+=('python' 'python-yaml' 'python-numpy')
  cd "$srcdir/${_pkgname}"
  python setup.py install --root="$pkgdir"/ --optimize=1 --skip-build
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

# vim:set ts=2 sw=2 et:
