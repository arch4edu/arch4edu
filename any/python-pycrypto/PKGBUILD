# Contributor: Davide Depau <davide@depau.eu>
# Contributor: Drew DeVault <sir@cmpwn.com>
# Contributor: Bruce Zhang <zttt183525594@gmail.com>

pkgbase='python-pycrypto'
pkgname=('python-pycrypto' 'python-crypto')
_name="${pkgbase#python-}"
pkgver=2.7a1
pkgrel=5
pkgdesc='[DEPRECATED since 2013] Cryptographic primitives and algorithms for Python'
arch=('x86_64')
_repourl="https://github.com/${_name}/${_name}"
url="${_repourl}/blob/master/README.md"
license=('custom:Unlicense' 'PSF')
makedepends=(
  'gmp'
  'python-setuptools'
)
conflicts=('python-pycryptodome')
_tarname="${_name}-${pkgver}"
source=("${_tarname}.tar.gz::${_repourl}/archive/refs/tags/v${pkgver}.tar.gz"
        '0001-replaced-time.clock-with-time.process_time-time-cloc.patch')
b2sums=('a64fa64402a603d58762e5ce752adad8d59fb13a20d54aa402d34c3f1c4c97d101f6f07c4bbb98262973532a1e7759af0f4a339ac2046e2b3ae1249761d28907'
        '2095507a13248be6e995cd18350670580773b37a483121b9f416447ad2fcf82c8f2602d98e5ac277dca81255ac5472bfb8eb91d76860203a9e98043d0f192915')

prepare() {
  cd "${_tarname}"
  patch -p1 < '../0001-replaced-time.clock-with-time.process_time-time-cloc.patch'
}

build() {
  cd "${_tarname}"
  python setup.py build
}

package_python-pycrypto() {
  arch=('any')
  license=('Unlicense')
  depends=("python-crypto=${pkgver}")
}

package_python-crypto() {
  depends=(
    'gmp'
    'python'
  )

  cd "${_tarname}"
  python setup.py install --root="${pkgdir}" --prefix='/usr' --optimize=1 --skip-build
  install -Dm 644 'COPYRIGHT' "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  find 'LEGAL/' -type f -exec install -Dm 644 "{}" "${pkgdir}/usr/share/licenses/${pkgname}/{}" \;
}
