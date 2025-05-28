# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-siosocks
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=0.3.0
pkgrel=1
pkgdesc="sans-io socks proxy client/server with couple io backends"
arch=('any')
url="https://github.com/pohmelie/siosocks"
license=('MIT')
makedepends=('python-setuptools')
#            'python-wheel'
#            'python-build'
#            'python-installer')
checkdepends=('python-pytest-asyncio'
              'python-pytest-trio'
              'python-trio')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('0469b2a18d6cffed9d2f2a993d84b834')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python setup.py build
#   python -m build --wheel --no-isolation

#   msg "Building Docs"
#   python setup.py build_sphinx
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    #PYTHONPATH="build/lib" pytest --ignore=tests/test_socketserver.py #|| warning "Tests failed"
    PYTHONPATH="build/lib" pytest || warning "Tests failed" # -vv --color=yes #\
#       --deselect=tests/test_socketserver.py::test_connection_socks_success || warning "Tests failed"
}

package_python-siosocks() {
    depends=('python>=3.8')
    optdepends=('python-trio: trio')
#               'python-siosocks-doc: Documentation for siosocks')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 license.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 readme.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
#   python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-siosocks-doc() {
#    pkgdesc="Documentation for Python siosocks"
#    cd ${srcdir}/${_pyname}-${pkgver}/build/sphinx
#
#    install -D -m644 ../../license.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
