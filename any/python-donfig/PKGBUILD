# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-donfig
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=0.8.1.post1
pkgrel=1
pkgdesc="Python package for configuring a python package"
arch=('any')
url="https://donfig.readthedocs.io"
license=('MIT')
makedepends=('python-setuptools'
             'python-versioneer'
             'python-build'
             'python-installer')  # wheel required by new setuptools typing-validation <- bases
#            'python-sphinx'
checkdepends=('python-pytest'
              'python-cloudpickle'
              'python-yaml')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('316ee7f6403887ddf7121aa93576fb5a')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation --skip-dependency-check

#   msg "Building Docs"
#   PYTHONPATH="../build/lib" make -C doc html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest -vv -l -ra --color=yes -o console_output_style=count #-p xdist -n 4 # || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count #
}

package_python-donfig() {
    depends=('python>=3.8' 'python-yaml')
#   optdepends=('python-donfig-doc: Documentation for Donfig')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-donfig-doc() {
#    pkgdesc="Documentation for Python Donfig"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 ../../LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
