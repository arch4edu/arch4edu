# Maintainer: Christopher Arndt <aur at chrisarndt dot de>

_name=SoundFile
pkgname=python-soundfile
pkgver=0.10.2
pkgrel=2
pkgdesc="An audio library based on libsndfile, CFFI and NumPy"
url="https://github.com/bastibe/PySoundFile"
arch=('any')
license=('BSD')
makedepends=('python-setuptools')
depends=('python-cffi' 'libsndfile' 'python-numpy')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('637f6218c867b8cae80f6989634a0813b416b3e6132480d056e6e5a89a921571')


build() {
  cd "${srcdir}/${_name}-${pkgver}"

  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"

  python setup.py install --root="${pkgdir}" --skip-build --optimize=1

  # install license
  install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
}
