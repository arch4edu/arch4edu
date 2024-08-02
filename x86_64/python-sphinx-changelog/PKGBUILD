# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-sphinx-changelog
_pname=${pkgbase#python-}
_pyname=${_pname/-/_}
pkgname=("python-${_pname}" "python-${_pname}-doc")
pkgver=1.5.0
pkgrel=1
pkgdesc="A changelog renderer for sphinx"
arch=('any')
url="https://sphinx-changelog.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer'
             'python-sphinx-automodapi'
             'towncrier')
checkdepends=('python-nose')    # sphinx, towncrier already in makedepends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz"
        "https://raw.githubusercontent.com/OpenAstronomy/sphinx-changelog/main/changelog/template.rst")
md5sums=('f91356131c4b0aa5e6a135b01cd70811'
         'SKIP')

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -Dm644 -t changelog ${srcdir}/template.rst
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

#   pytest -vv --color=yes #|| warning "Tests failed"
    nosetests -v -x || warning "Tests failed"
}

package_python-sphinx-changelog() {
    depends=('python-sphinx' 'towncrier')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" licenses/*
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-sphinx-changelog-doc() {
    pkgdesc="Documentation for sphinx-changelog"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../licenses/*
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
