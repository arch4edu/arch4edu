# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: Francois Boulogne <fboulogne at april dot org>

pkgname=python-tifffile
pkgver=2020.6.3
_pyname=${pkgname#python-}
pkgrel=1
pkgdesc="Read and write image data from and to TIFF files"
arch=('any')
url="https://github.com/cgohlke/tifffile"
license=('BSD')
makedepends=('python-setuptools')
depends=('python-numpy')
optdepends=('python-matplotlib: required only for plotting'
            'python-imagecodecs: required only for encoding or decoding LZW, JPEG, etc.')
#checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('e79403a8b98b0df7ade8d43469151b959fd56239001471fac62beabca6f56377')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build
}

#check() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    PYTHONPATH="build/lib" pytest
#}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root="${pkgdir}" --optimize=1
}

# vim:ts=2:sw=2:et:
