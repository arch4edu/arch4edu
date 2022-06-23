# Maintainer: Martchus <martchus@gmx.net>
# Contributor: Marco Pompili <aur AT emarcs DOT org>
# Contributor: Giorgio Gilestro crocowhile@gmail.com
# Contributor: Mladen Milinkovic <maxrd2@smoothware.net>

pkgname=sphinxbase
pkgver=5prealpha
pkgrel=13
pkgdesc='Common library for sphinx speech recognition'
url='https://cmusphinx.sourceforge.net/'
arch=('i686' 'x86_64')
license=('BSD')
makedepends=('bison' 'swig')
depends=('python' 'lapack' 'libpulse') # not sure if libsamplerate is needed 'libsamplerate'
source=("http://downloads.sourceforge.net/project/cmusphinx/${pkgname}/${pkgver}/${pkgname}-${pkgver}.tar.gz"
        "sphinxbase-5prealpha-fix-doxy2swig.patch")

sha256sums=('f72bdb59e50b558bed47cc2105777200d2b246a0f328e913de16a9b22f9a246f'
            '1cb485202f83dc517872f5ab41f59d18884af1b85799166d80e08860f7729919')
options=('!libtool')

prepare() {
  cd "${pkgname}-${pkgver}"

  patch -p1 -b -i ../sphinxbase-5prealpha-fix-doxy2swig.patch

  echo "Reconfiguring project for current version of Automake"
  autoreconf -ivf > /dev/null
}

build() {
  cd "${pkgname}-${pkgver}"

  export PYTHON=/usr/bin/python PYTHONWARNINGS=ignore
  ./configure --prefix=/usr
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}/" install

  install -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" \
                "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
