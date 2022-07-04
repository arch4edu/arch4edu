# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Maintainer: Jaroslav Lichtblau <dragonlord at aur dot archlinux dot org>
# Contributor: Andrzej Giniewicz <gginiu at gmail dot com>

pkgbase=python-scikit-image
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
pkgver=0.19.2
pkgrel=1
pkgdesc="Image processing routines for SciPy"
arch=('i686' 'x86_64')
url="http://scikit-image.org"
license=('BSD')
makedepends=('cython>=0.29.21' 'python-setuptools' 'python-pythran' 'python-packaging>=20.0')
depends=('python-numpy>1.18.0' 'python-scipy>=1.4.1' 'python-networkx>=2.2' 'python-pillow>8.3.0' 'python-pywavelets>=1.1.1' 'python-imageio>=2.4.1' 'python-tifffile>=2019.7.26' 'python-packaging>=20.0')
checkdepends=('python-pytest>=5.2.0'
              'python-pytest-cov>=2.7.0'
              'python-matplotlib>=3.0.3'
              'python-pytest-flake8'
              'python-pytest-localserver'
              'python-pooch>=1.3.0')
#             'python-pytest-faulthandler')
optdepends=('python-pyqt5: for imshow[x, fancy=True] and skivi'
            'pyside2: for imshow[x, fancy=True] and skivi'
            'python-qtpy'
            'python-matplotlib>=3.0.3'
            'freeimage: for reading various types of image file formats'
            'python-pyamg: fast cg_mg mode of random walker segmentation'
            'python-astropy>=3.1.2: Provides FITS I/O capability'
            'python-imread: Optional I/O plugin providing most standard formats'
            'python-simpleitk: Optional I/O plugin providing a wide variety of formats. including specialized formats using in medical imaging'
            'python-dask>=2.17.0: used to speed up certain functions'
            'python-cloudpickle>=0.2.1: necessary to provide the 'processes' scheduler for dask'
            'python-pooch>=1.3.0')
options=('!emptydirs')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('d433b4642a6f8219e749dfbbe4b5e742d560996540c9749ede510274d061866d')

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
