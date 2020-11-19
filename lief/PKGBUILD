# Maintainer: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgname=lief
pkgver=0.10.1
pkgrel=3
pkgdesc='Library to instrument executable formats'
arch=(x86_64)
url='https://lief.quarkslab.com/'
license=(APACHE)
depends=(python)
makedepends=(git cmake python-setuptools)
source=("git+https://github.com/lief-project/LIEF#tag=${pkgver}"
        https://github.com/lief-project/LIEF/pull/365/commits/68f61547226cfb3b09d1628bf11f68443b7a8bcf.diff
        https://github.com/lief-project/LIEF/pull/365/commits/f9e88a6665e80675c67310089d43045ebd3b64ef.diff)
sha256sums=(SKIP
            65caea9a2316a5d3b8ffff742643cabb4e1d182b9fa7a2e41bbe02d892b94086
            b7dcb28ee259410424578ddc89a2dc7fd7f605a4d266d06fa9919915b1efdb37)

prepare()
{
  cd "${srcdir}/LIEF"

  patch -p1 < ../68f61547226cfb3b09d1628bf11f68443b7a8bcf.diff
  patch -p1 < ../f9e88a6665e80675c67310089d43045ebd3b64ef.diff
}

build() {
  cd "${srcdir}/LIEF"
  mkdir build

  cmake . -B build -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1
  make -C build
  python setup.py build --build-temp=build
}

package() {
  cd "${srcdir}/LIEF"

  make -C build DESTDIR="${pkgdir}" install
  python setup.py install --optimize=1 --root="${pkgdir}" --skip-build
}
