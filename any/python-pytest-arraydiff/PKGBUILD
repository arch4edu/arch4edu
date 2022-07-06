# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-pytest-arraydiff
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
pkgver=0.5.0
pkgrel=1
pkgdesc="Pytest plugin to help with comparing array output from tests"
arch=('any')
url="https://github.com/astrofrog/pytest-arraydiff"
license=('BSD')
makedepends=('python-setuptools-scm')
checkdepends=('python-pytest' 'python-astropy')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('279c9933e08652200bd81fce2d80f0a7')

prepare() {
    export _pyver=$(python -c 'import sys; print("%d.%d" % sys.version_info[:2])')
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    export _pyver=$(python -c 'import sys; print("%d.%d" % sys.version_info[:2])')
    ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname/-/_}*egg-info \
        build/lib/${_pyname/-/_}-${pkgver}-py${_pyver}.egg-info
    PYTHONPATH="build/lib" pytest || warning "Tests failed"
}

package() {
    depends=('python-numpy' 'python-pytest>=4.6')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
