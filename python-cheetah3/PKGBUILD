# Maintainer: Alex Brinister <alex_brinister at yahoo dot com>

pkgname=python-cheetah3
_name=Cheetah3
pkgver=3.2.3
pkgrel=1
pkgdesc="A Python 3-powered template engine and code generator"
arch=(x86_64)
url="http://www.cheetahtemplate.org"
license=(custom)
depends=('python-setuptools')
optdepends=('python-markdown')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('ebc735b59d61912679405469f9d509fc73bbdde51c414320994421849f4a02266d2c286c0f618cab2a592ab47ac0a4be9ec444fab75145a0c31dd0c3c39fc1e3')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # Avoid conflict with python2-cheetah
  for name in cheetah cheetah-analyze cheetah-compile; do
    mv "${pkgdir}/usr/bin/${name}"{,3}
  done
}
