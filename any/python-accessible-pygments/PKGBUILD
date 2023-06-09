# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-accessible-pygments
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=0.0.4
pkgrel=1
pkgdesc="A collection of accessible pygments styles"
arch=('any')
url="https://quansight-labs.github.io/accessible-pygments"
license=('BSD')
makedepends=('python-setuptools'
             'python-pygments')
#            'python-wheel'
#            'python-build'
#            'python-installer'
#            'python-sphinx')
checkdepends=('python-nose')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('ecacd117d7258a285ccc282a33abd906')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python setup.py build
#   python -m build --wheel --no-isolation

#   msg "Building Docs"
#   PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

#   pytest -vv --color=yes #\
    nosetests
}

package_python-accessible-pygments() {
    depends=('python-pygments>=1.5')
#   optdepends=('python-accessible-pygments-doc: Documentation for accessible-pygments')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
#   python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-accessible-pygments-doc() {
#    pkgdesc="Documentation for Python Accessible pygments"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 ../../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
