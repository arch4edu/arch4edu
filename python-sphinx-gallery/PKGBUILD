# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-sphinx-gallery
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=0.8.2
pkgrel=1
pkgdesc="Sphinx extension to automatically generate an examples gallery"
arch=('i686' 'x86_64')
url="http://sphinx-gallery.github.io"
license=('BSD')
makedepends=('python-setuptools')
#'python-sphinx' 'python-pillow' 'python-scipy' 'python-seaborn')
checkdepends=('python-pytest-cov' 'python-matplotlib' 'python-pillow' 'python-sphinx' 'python-joblib')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('2e8e42f95a6a49dbee35820b3204863f')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python setup.py build

#   msg "Building Docs"
#   python setup.py build_sphinx
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed"
}

package_python-sphinx-gallery() {
    depends=('python-sphinx>=1.8.3' 'python-pillow' 'python-matplotlib')
    optdepends=('python-seaborn'
                'mayavi'
                'python-pypandoc')
#               'python-sphinx-gallery-doc: Documentation of Sphinx-Gallery')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}

#package_python-sphinx-gallery-doc() {
#    pkgdesc="Documentation for Sphinx-Gallery extension"
#    cd ${srcdir}/${_pyname}-${pkgver}/doc/_build
#
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
