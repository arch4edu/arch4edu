# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgname=python-astropy-sphinx-theme
_pname=${pkgname#python-}
_pyname=${_pname//-/_}
pkgver=2.0
pkgrel=1
pkgdesc="The sphinx theme for Astropy and affiliated packages."
arch=('any')
url="https://github.com/astropy/astropy-sphinx-theme"
license=('BSD')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer')
checkdepends=('python-pytest'
              'python-sphinx')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('9c4d9033cc7df306e2134eceec7597d2950d424e4fe6201f2fbf788e3ceb8b97')

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    sed -i '/use_2to3/d' setup.py
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_gitname}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count #
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}
    depends=('python-setuptools>=30.3.0')

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
