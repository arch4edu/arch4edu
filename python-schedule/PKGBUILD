# Maintainer: Dylan Whichard <dylan@whichard.com>
_name=schedule
pkgname=python-schedule
pkgver=0.5.0
pkgrel=2
pkgdesc='Python job scheduling for humans.'
arch=('any')
url="https://github.com/dbader/$_name"
license=('MIT')
depends=('python>=2.3')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('1003a07c2dce12828c25a03a611a7371cedfa956e5f1b4abc32bcc94eb5a335b')

package() {
	cd "$srcdir/$_name-$pkgver"
	python setup.py install --root="$pkgdir" --optimize=1 || return 1
}
