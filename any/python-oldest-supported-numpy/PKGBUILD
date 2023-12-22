# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-oldest-supported-numpy
_pyname=${pkgname#python-}
pkgver=2023.12.21
pkgrel=1
pkgdesc="Meta-package providing oldest supported Numpy for given Python version"
arch=('any')
url="https://github.com/scipy/oldest-supported-numpy"
license=('BSD')
depends=('python-numpy')
#makedepends=('python-setuptools' 'python-wheel' 'python-build' 'python-installer')
makedepends=('python-setuptools')
#checkdepends=('python-pytest')
checkdepends=('python-nose')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('a2ef01b917cec33780bb5e7e0f0aa274')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    #export _npver=$(python -c 'import numpy; print(numpy.__version__)')
    #sed -i '/'"$(get_pyver .)"'/!b;n;c\numpy=='"${_npver}" oldest_supported_numpy.egg-info/requires.txt
    #sed -i "/$(get_pyver .)/s/==.*;/>=${_npver};/" setup.cfg
    sed -i "/$(get_pyver .)/s/==/>=/" setup.cfg
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build
#   python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

#   python setup.py test
#   pytest
    nosetests
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    #python -m installer --destdir="${pkgdir}" dist/*.whl
}
