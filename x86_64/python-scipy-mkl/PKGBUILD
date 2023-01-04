# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Ray Rashif <schiv@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Bodor Dávid Gábor <david.gabor.bodor@gmail.com>
# Contributor: Andrzej Giniewicz <gginiu@gmail.com>

pkgname=python-scipy-mkl
pkgver=1.10.0
pkgrel=1
pkgdesc="SciPy is open-source software for mathematics, science, and engineering."
arch=('x86_64')
url="http://www.scipy.org/"
license=('BSD')
depends=('intel-oneapi-mkl' 'python-numpy')
provides=("python-scipy=$pkgver")
conflicts=('python-scipy')
makedepends=('cython' 'gcc-fortran' 'procps-ng' 'pybind11' 'python-pythran' 'python-setuptools')
checkdepends=('python-pytest')
optdepends=('python-pillow: for image saving module')
source=("https://github.com/scipy/scipy/releases/download/v${pkgver}/scipy-${pkgver}.tar.gz")
sha256sums=('c8b3cbc636a87a89b770c6afc999baa6bcbb01691b5ccbbc1b1791c7c0a07540')

build() {
	source /opt/intel/oneapi/setvars.sh
	cd scipy-${pkgver}
	python setup.py config_fc build
}

check() {
	cd ${srcdir}/scipy-${pkgver}
	python3 setup.py config_fc install --prefix=/usr --root=${srcdir}/test --optimize=1
	export PYTHONPATH=${srcdir}/test/usr/lib/python3.10/site-packages
	cd ${srcdir}
	python -c "from scipy import test; test('full')"
}

package() {
	cd scipy-${pkgver}
	python3 setup.py config_fc install --prefix=/usr --root="${pkgdir}/" --optimize=1

	install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
