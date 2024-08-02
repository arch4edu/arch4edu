# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-sphinx_contributors
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=0.2.7
pkgrel=1
pkgdesc="Contributors extension for Sphinx"
arch=('any')
url="https://sphinx-contributors.readthedocs.io"
license=('BSD')
makedepends=('python-flit-core'
             'python-build'
             'python-installer'
             'python-sphinx-furo')
checkdepends=('python-pytest')  #python-sphinx
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('7ff8fe3657645ce61639ade0d82b12fc')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    mkdir -p dist/lib
    bsdtar -xpf dist/${_pyname/-/_}-${pkgver}-py3-none-any.whl -C dist/lib
    PYTHONPATH="../dist/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    PYTHONPATH="dist/lib" pytest || warning "Tests failed" # -vv --color=yes
}

package_python-sphinx_contributors() {
    depends=('python>=3.7' 'python-sphinx>=3')
    optdepends=('python-sphinx_contributors-doc: Documentation for sphinx-contributors')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE.md
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-sphinx_contributors-doc() {
    pkgdesc="Documentation for sphinx contributors"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE.md
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
