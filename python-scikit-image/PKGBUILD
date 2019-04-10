# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Maintainer: Jaroslav Lichtblau <dragonlord at aur dot archlinux dot org>
# Contributor: Andrzej Giniewicz <gginiu at gmail dot com>

pkgbase=python-scikit-image
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
pkgver=0.15.0
pkgrel=1
pkgdesc="Image processing routines for SciPy"
arch=('i686' 'x86_64')
url="http://scikit-image.org/"
license=('BSD')
makedepends=('cython' 'python-six')
depends=('python-scipy' 'python-matplotlib' 'python-networkx' 'python-pillow' 'python-pywavelets')
optdepends=('python-pyqt4: for imshow(x, fancy=True) and skivi'
            'freeimage: for reading various types of image file formats'
            'python-pyamg: fast cg_mg mode of random walker segmentation')
options=('!emptydirs')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('df111e654b47e5ea456c50553debe4c5ddd97258894c7ad3b7f2f9f10798e053')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
