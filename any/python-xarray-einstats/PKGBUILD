# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor:  Anton Kudelin <kudelin at proton dot me>

pkgbase=python-xarray-einstats
_pname=${pkgbase#python-}
_pyname=${_pname}
#_pyname=${_pname//-/_}
pkgname=("python-${_pname}")
# "python-${_pname}-doc")
pkgver=0.10.0
pkgrel=1
pkgdesc='Stats, linear algebra and einops for xarray'
arch=('any')
url='https://einstats.python.arviz.org'
license=('Apache-2.0')
makedepends=('python-flit-core'
             'python-build'
             'python-installer')
checkdepends=('python-pytest'
#             'python-pytest-xdist'
              'python-einops'
              'python-numba'
              'python-scipy'
              'python-xarray')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/arviz-devs/${_pyname}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('397691dfab517229b823e2fa34cd218c7466ec9ce397c7982085924ffcca6d06')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation --skip-dependency-check
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    mkdir -p dist/lib
    bsdtar -xpf dist/${_pyname/-/_}-${pkgver}-py3-none-any.whl -C dist/lib
    PYTHONPATH="dist/lib" pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package() {
    depends=('python>=3.12' 'python-scipy>=1.13' 'python-xarray>=2024.02.0')
    optdepends=('python-einops'
                'python-numba')
#               'python-xarray-einstats-doc: Documentation for -validation')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
