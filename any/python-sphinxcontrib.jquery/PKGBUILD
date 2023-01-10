# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-sphinxcontrib.jquery
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=3.0.0
pkgrel=1
pkgdesc="Extension to include jQuery on newer Sphinx releases"
arch=('any')
url="https://github.com/sphinx-contrib/jquery"
license=('custom:0BSD')
makedepends=('python-flit-core'
             'python-wheel'
             'python-build'
             'python-installer')
#checkdepends=('python-pytest')
checkdepends=('python-nose')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz"
        "https://github.com/sphinx-contrib/jquery/raw/master/LICENCE")
md5sums=('bbdc263b54529e4d5da045221d501c31'
         'SKIP')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

#   msg "Building Docs"
#   mkdir -p dist/lib
#   bsdtar -xpf dist/${_pyname/./_}-${pkgver}-py2.py3-none-any.whl -C dist/lib
#   cd ${srcdir}/${_pyname}-${pkgver}/docs
#   PYTHONPATH="../dist/lib" make html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    nosetests || warning "Tests failed"
#   pytest
}

package_python-sphinxcontrib.jquery() {
    depends=('python-sphinx')
#   optdepends=('python-sphinxcontrib.jquery-doc: Documentation for sphinxcontrib.jquery')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 ${srcdir}/LICENCE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-sphinxcontrib.jquery-doc() {
#    pkgdesc="Documentation for Sphinx-hoverxref"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
