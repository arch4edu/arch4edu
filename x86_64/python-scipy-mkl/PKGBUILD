# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Ray Rashif <schiv@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Bodor Dávid Gábor <david.gabor.bodor@gmail.com>
# Contributor: Andrzej Giniewicz <gginiu@gmail.com>

pkgname=python-scipy-mkl
pkgver=1.12.0
pkgrel=1
pkgdesc="SciPy is open-source software for mathematics, science, and engineering."
arch=('x86_64')
url="http://www.scipy.org/"
license=('BSD')
depends=('intel-oneapi-mkl' 'python-numpy' 'python-pooch')
provides=("python-scipy")
conflicts=('python-scipy')
makedepends=('cython' 'gcc-fortran' 'meson-python' 'procps-ng' 'pybind11' 'python-build' 'python-installer' 'python-pythran')
checkdepends=('python-pytest')
optdepends=('python-pillow: for image saving module')
source=("https://pypi.python.org/packages/source/s/scipy/scipy-$pkgver.tar.gz")
sha256sums=('4bf5abab8a36d20193c698b0f1fc282c1d083c94723902c447e5d2f1780936a3')

build() {
	source /opt/intel/oneapi/setvars.sh
	cd scipy-${pkgver}

	# https://github.com/scipy/scipy/issues/16200#issuecomment-1615094519
	python -m build --wheel --no-isolation --skip-dependency-check \
		-C setup-args=-Dblas=mkl-dynamic-lp64-seq \
		-C setup-args=-Dlapack=mkl-dynamic-lp64-seq
}

check() {
	cd scipy-${pkgver}
	python -m venv --system-site-packages test-env
	test-env/bin/python -m installer dist/*.whl
	cd test-env
	bin/python -c "from scipy import test; test('full')"
}

package() {
	cd scipy-${pkgver}
	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
