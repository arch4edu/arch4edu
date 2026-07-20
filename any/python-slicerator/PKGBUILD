# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: Luis Martinez <luis dot martinez at tuta dot io>
# Contributor: Francois Boulogne <fboulogne at april dot org>

## GPG key: https://github.com/tacaswell.gpg

pkgbase=python-slicerator
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}"-doc)
pkgver=1.1.0
pkgrel=1
pkgdesc="A lazy-loading, fancy-sliceable iterable"
url="https://slicerator.readthedocs.io/"
arch=('any')
license=('BSD-3-Clause')
makedepends=('python-setuptools'
             'python-build'
             'python-installer'
             'python-sphinx_rtd_theme'
             'python-numpydoc')
checkdepends=('python-pytest'
#             'python-pytest-xdist'
              'python-numpy')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('44010a7f5cd87680c07213b5cabe81d1fb71252962943e5373ee7d14605d6046')
#validpgpkeys=('96B7334D7610EE3E68AFFE589E027116943D6A8B') ## Thomas A. Caswell

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    sed -i "/language\ = /s/None/'en'/" docs/conf.py
    mkdir -p docs/_static
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    PYTHONPATH="." pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-slicerator() {
    cd ${srcdir}/${_pyname}-${pkgver}
    depends=('python')
    #PYTHONHASHSEED=0 python -m installer --destdir="$pkgdir/" dist/*.whl
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-slicerator-doc() {
    pkgdesc="Documentation for Python Slicerator module"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
