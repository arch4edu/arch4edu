# Maintainer: George C. Privon <accounts5 at privon dot com>
# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-emcee
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
pkgver=3.1.6
pkgrel=1
pkgdesc="Kick ass affine-invariant ensemble MCMC sampling"
arch=('any')
url="http://emcee.readthedocs.io"
depends=('python-numpy')
optdepends=('python-tqdm: For progress bars'
            'python-h5py: For HDF5 backend'
            'python-scipy'
            'python-emcee-doc: Documentations for emcee')
license=('MIT')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer')
checkdepends=('python-pytest'
              'python-scipy'
              'python-h5py')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('9d0f7cbb4edb96bf397513ba2871e867')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
}

package_python-emcee() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
