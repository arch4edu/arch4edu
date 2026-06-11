# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-astropy-sphinx-theme
_pname=${pkgbase#python-}
_pyname=${_pname//-/_}
pkgname=("python-${_pname}" "python-${_pname}-doc")
pkgver=3.1
pkgrel=1
pkgdesc="The sphinx theme for Astropy and affiliated packages."
arch=('any')
url="https://github.com/astropy/astropy-sphinx-theme"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm>=8'
             'python-build'
             'python-installer'
             'python-sphinx')
checkdepends=('python-pytest')   # sphinx already in makedepends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('eff780a7b9b00a165782bd703decff9f32bfa6dcb606ce583fe2fc768ca45019')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    sed -i '/use_2to3/d' setup.py
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname/-/_}*egg-info \
        build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_gitname}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count #
}

package_python-astropy-sphinx-theme() {
    cd ${srcdir}/${_pyname}-${pkgver}
    depends=('python-sunpy-sphinx-theme>=2.1.1')

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-astropy-sphinx-theme-doc() {
    pkgdesc="Documentation for astropy-sphinx-theme"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE.rst
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
