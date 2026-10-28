# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgname=python-pytest-remotedata
_pname=${pkgname#python-}
_pyname=${_pname//-/_}
pkgver=0.4.3
pkgrel=1
pkgdesc="Pytest plugin used for controlling access to data files hosted online"
arch=('any')
url="https://github.com/astropy/pytest-remotedata"
license=('BSD-3-Clause')
depends=('python-pytest>=7.2' 'python-packaging')
makedepends=('python-hatchling'
             'python-hatch-vcs'
             'python-build'
             'python-installer')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('0a7b9a476a2e7325a8902158adad8783')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

#get_pyinfo() {
#    [[ $1 == "site" ]] && python -c "import site; print(site.getsitepackages()[0])" || \
#        python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    # ValueError: Pytest terminal summary report not found
#   ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname/-/_}*egg-info \
#       build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
#   PYTHONPATH="${PWD}/build/lib" pytest -vv -l -ra --color=yes -o console_output_style=count # --remote-data # || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count # --remote-data #
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    test-env/bin/python -m pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count # --remote-data #
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer dist/*.whl
#   test-env/bin/python -m pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count # --remote-data #
#   python -m installer --destdir=tmp_install dist/*.whl
#   PYTHONPATH="${PWD}/tmp_install/$(get_pyinfo site)" pytest -vv -l -ra --color=yes -o console_output_style=count #
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
