# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Maintainer: Jaroslav Lichtblau <dragonlord at aur dot archlinux dot org>
# Contributor: Andrzej Giniewicz <gginiu at gmail dot com>

pkgbase=python-scikit-image
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
pkgver=0.18.0
pkgrel=1
pkgdesc="Image processing routines for SciPy"
arch=('i686' 'x86_64')
url="http://scikit-image.org/"
license=('BSD')
makedepends=('cython>=0.29.21')
depends=('python-numpy>1.18.0' 'python-scipy>=1.0.1' 'python-matplotlib>3.0.0' 'python-networkx>=2.0' 'python-pillow>7.1.1' 'python-pywavelets>=1.1.1' 'python-imageio>=2.3.0' 'python-tifffile>=2019.7.26')
checkdepends=('python-pytest>=5.2.0'
              'python-pytest-cov>=2.7.0'
              'python-pytest-flake8'
              'python-pytest-localserver'
              'python-pooch') #>=1.3.0
#             'python-pytest-faulthandler')
optdepends=('python-pyqt5: for imshow[x, fancy=True] and skivi'
            'python-qtpy'
            'freeimage: for reading various types of image file formats'
            'python-pyamg: fast cg_mg mode of random walker segmentation'
            'python-astropy: Provides FITS I/O capability'
            'python-imread: Optional I/O plugin providing most standard formats'
            'python-simpleitk: Optional I/O plugin providing a wide variety of formats. including specialized formats using in medical imaging'
            'python-dask: used to speed up certain functions'
            'python-cloudpickle: necessary to provide the 'processes' scheduler for dask')
options=('!emptydirs')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('a0c78a117080101dbeeaa430804fe9512575cf2696ddbf822a7ee30d0776f5da')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build_ext --inplace
    python setup.py build
}

check() {
    cd "${_pyname}-${pkgver}"

    pytest || warning "Tests failed"
}

package_python-scikit-image() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -Dm644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 --skip-build
}
