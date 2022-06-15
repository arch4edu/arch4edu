# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-remotedata
_pyname=${pkgname#python-}
pkgver=0.3.3
pkgrel=1
pkgdesc="Pytest plugin used for controlling access to data files hosted online"
arch=('any')
url="https://github.com/astropy/pytest-remotedata"
license=('BSD')
depends=('python-pytest>=4.6' 'python-packaging')
makedepends=('python-setuptools-scm')
#checkdepends=('python-astropy')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('8507cafd80961585366c5d3c9116cc47')

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
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
