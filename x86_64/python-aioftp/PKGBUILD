# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-aioftp
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=0.27.2
pkgrel=1
pkgdesc="ftp client/server for asyncio"
arch=('any')
url="https://aioftp.readthedocs.io"
license=('Apache-2.0')
makedepends=('python-setuptools'
             'python-build'
             'python-installer')  # wheel required by new setuptools
#            'python-sphinx'
checkdepends=('python-pytest-asyncio'
#             'python-pytest-xdist'
              'python-pytest-mock'
              'python-pytest-cov'
              'python-async-timeout'
              'python-trustme'
              'python-siosocks')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('7c048c3220081796c59832a6fd9fd8fad97e3cec12a50be3abccf2dcbbeb261a')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

#   msg "Building Docs"
#   PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

#   ln -rs ${srcdir}/${_pyname}-${pkgver}/src/${_pyname/-/_}*egg-info \
#       build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
#   PYTHONPATH="build/lib" pytest -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 # || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
    PYTHONPATH="src" pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-aioftp() {
    depends=('python>=3.10')
    optdepends=('python-siosocks>=0.2.0: Client socks proxy')
#               'python-aioftp-doc: Documentation for aioftp')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 license.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-aioftp-doc() {
#    pkgdesc="Documentation for Python aioftp"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 ../../license.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
