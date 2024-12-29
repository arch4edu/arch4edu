# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix

# On Debian there is v2.2.1-3.1, same developer (smurfix)
# https://packages.debian.org/sid/yapps2
# _debver isn't in pkgver= for not messing with repology.org

pkgname=python-yapps2
pkgver=2.2.1
_debver=3.1
pkgrel=5
pkgdesc="Yet Another Python Parser System, Python3 fork by smurfix"
arch=(any)
url="https://github.com/smurfix/yapps"
license=(MIT)
depends=(python python-importlib-metadata python-setuptools)
#makedepends=(python-setuptools)
#checkdepends=(python-pytest)
conflicts=(python2-yapps2)
#source=("${pkgname}-debian-${pkgver}.tar.gz::https://github.com/smurfix/yapps/archive/refs/tags/DEBIAN-${_pkgver}.tar.gz")
source=("http://deb.debian.org/debian/pool/main/y/yapps2/yapps2_${pkgver}.orig.tar.gz"
        "http://deb.debian.org/debian/pool/main/y/yapps2/yapps2_${pkgver}-${_debver}.diff.gz")
sha256sums=('3f46dbef0d9b067a00dced333c1b2c09d78963e0dd14872a39715889b7228f73'
            'b41f6ec42dadb3ce55d45bc9e068f5713e69b453e9098313c4fac73d626fea68')

prepare() {
  cd "yapps2-${pkgver}"
  patch -Np1 -i ../"yapps2_${pkgver}-${_debver}.diff"
}

build() {
  #cd "${srcdir}/yapps-DEBIAN-${_pkgver}"
  cd "yapps2-${pkgver}"
  python setup.py build
}

#check() {
#  #cd "${srcdir}/yapps-DEBIAN-${_pkgver}"
#  pytest -v
#}

package() {
  #cd "${srcdir}/yapps-DEBIAN-${_pkgver}"
  cd "yapps2-${pkgver}"
  python setup.py install --skip-build --optimize=1 --prefix=/usr --root="${pkgdir}"
  install -D LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
