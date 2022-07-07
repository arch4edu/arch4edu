# Contributor: Davide Depau <davide@depau.eu>
# Contributor: Drew DeVault <sir@cmpwn.com>
# Contributor: Bruce Zhang <zttt183525594@gmail.com>

pkgbase='python-pycrypto'
pkgname=('python-pycrypto' 'python-crypto')
_name="${pkgbase#python-}"
pkgver=2.6.1
pkgrel=7
pkgdesc='[DEPRECATED since 2013] Cryptographic primitives and algorithms for Python'
arch=('x86_64')
url="https://github.com/${_name}/${_name}/blob/master/README.md"
license=('custom:Unlicense' 'PSF')
makedepends=(
  'gmp'
  'python-setuptools'
)
_tarname="${_name}-${pkgver}"
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_tarname}.tar.gz"
        '0001-replaced-time.clock-with-time.process_time-time-cloc.patch')
sha512sums=('20a4aed4dac4e9e61d773ebc1d48ea577e9870c33f396be53d075a9bf8487d93e75e200179882d81e452efd0f6751789bac434f6f431b3e7c1c8ef9dba392847'
            '9a8c9812b3a13701571cb9cebb2fd755be7206f4045cbec76375259b716c2769dd25996cd8af89248cf7d9de0b088193a245442169c0c645ccd6083b529e3e50')

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
  conflicts=('python-pycryptodome')

  cd "${_tarname}"
  python setup.py install --root="${pkgdir}" --prefix='/usr' --optimize=1 --skip-build
  install -Dm 644 'COPYRIGHT' "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  find 'LEGAL/' -type f -exec install -Dm 644 "{}" "${pkgdir}/usr/share/licenses/${pkgname}/{}" \;
}
