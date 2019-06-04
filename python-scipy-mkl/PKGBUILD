# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Ray Rashif <schiv@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Bodor Dávid Gábor <david.gabor.bodor@gmail.com>
# Contributor: Andrzej Giniewicz <gginiu@gmail.com>

pkgname='python-scipy-mkl'
pkgver=1.3.0
pkgrel=1
pkgdesc="SciPy is open-source software for mathematics, science, and engineering."
arch=('x86_64')
url="http://www.scipy.org/"
license=('BSD')
depends=('intel-compiler-base' 'intel-fortran-compiler' 'intel-mkl' 'python-numpy')
provides=("python-scipy=$pkgver")
conflicts=('python-scipy')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
optdepends=('python-pillow: for image saving module')
source=("https://github.com/scipy/scipy/releases/download/v${pkgver}/scipy-${pkgver}.tar.gz")
sha512sums=('11dfe6027061efb176811d1d2c8b60ee53157f6fff59baa312b3b6a84461123e12f044d5d138d04b1162612d35c6cc34837208d56cdf79c294862ef90c62ea1d')

build() {
	export LDFLAGS="-Wall -shared"

	# build for python3
	cd scipy-${pkgver}
	python3 setup.py config --compiler=intelem --fcompiler=intelem build_clib --compiler=intelem --fcompiler=intelem build_ext --compiler=intelem --fcompiler=intelem
}

#check() {
#	# we need to do a temp install so we can import scipy
#	# also, the tests must not be run from the scipy source directory
#	export LDFLAGS="-Wall -shared"
#
#	cd ${srcdir}/scipy-${pkgver}
#	python3 setup.py config_fc --fcompiler=intelem install \
#	  --prefix=/usr --root=${srcdir}/test --optimize=1
#	export PYTHONPATH=${srcdir}/test/usr/lib/python3.7/site-packages
#	cd ${srcdir}
#	python -c "from scipy import test; test('full')"
#}

package() {
	export LDFLAGS="-Wall -shared"

	cd scipy-${pkgver}
	python3 setup.py config --compiler=intelem --fcompiler=intelem install --prefix=/usr --root="${pkgdir}/" --optimize=1

	install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
