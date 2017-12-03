# Maintainer: Jaroslav Lichtblau <dragonlord@aur.archlinux.org>
# Contributor: Andrzej Giniewicz <gginiu@gmail.com>

pkgbase=python-scikit-image
pkgname=('python2-scikit-image' 'python-scikit-image')
pkgver=0.13.1
pkgrel=1
pkgdesc="Image processing routines for SciPy"
arch=('i686' 'x86_64')
url="http://scikit-image.org/"
license=('BSD')
makedepends=('cython2' 'cython' 'python2-six' 'python-six' 'python2-scipy' 'python-scipy'
            'python2-matplotlib' 'python-matplotlib' 'python2-networkx' 'python-networkx'
            'python2-pillow' 'python-pillow' 'python2-pywavelets' 'python-pywavelets')
options=('!emptydirs')
source=(https://pypi.python.org/packages/83/2a/c5a39c12c196c19a443fa4d17c0768a24231e46ae952930a9d66bad45557/scikit-image-$pkgver.tar.gz)
sha256sums=('353879ddf7483f4621872c49cd9bc8a0ad1c3154ac0670b70799922f4cb899e8')

prepare() {
  cd "${srcdir}"
  cp -a scikit-image-$pkgver scikit-image-py2-$pkgver
  cd scikit-image-py2-$pkgver

  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
      -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
      -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
      -i $(find . -name '*.py')
}

build() {
  msg "Building Python2"
  cd "${srcdir}"/scikit-image-py2-$pkgver
  python2 setup.py build

  msg "Building Python3"
  cd "${srcdir}"/scikit-image-$pkgver
  python setup.py build
}

package_python2-scikit-image() {
  depends=('python2-scipy' 'python2-matplotlib' 'python2-networkx'
           'python2-pillow' 'python2-pywavelets')
  optdepends=('python2-pyqt4: for imshow(x, fancy=True) and skivi'
              'freeimage: for reading various types of image file formats')
  cd "${srcdir}"/scikit-image-py2-$pkgver

  python2 setup.py install --root="${pkgdir}"/ --optimize=1
  mv "${pkgdir}"/usr/bin/skivi "${pkgdir}"/usr/bin/skivi2
  install -D LICENSE.txt "${pkgdir}"/usr/share/licenses/$pkgname/LICENSE
}

package_python-scikit-image() {
  depends=('python-scipy' 'python-matplotlib' 'python-networkx'
           'python-pillow' 'python-pywavelets')
  optdepends=('python-pyqt4: for imshow(x, fancy=True) and skivi'
              'freeimage: for reading various types of image file formats'
              'python-pyamg: fast cg_mg mode of random walker segmentation')
  cd "${srcdir}"/scikit-image-$pkgver

  python setup.py install --root="${pkgdir}"/ --optimize=1
  install -D LICENSE.txt "${pkgdir}"/usr/share/licenses/$pkgname/LICENSE
}
