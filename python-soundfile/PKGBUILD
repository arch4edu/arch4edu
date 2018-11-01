pkgbase=python-soundfile
pkgname=('python-soundfile' 'python2-soundfile')
pkgver=0.10.1
pkgrel=1
pkgdesc="An audio library based on libsndfile, CFFI and NumPy"
url="https://github.com/bastibe/PySoundFile"
arch=('any')
license=('BSD')
makedepends=('python-setuptools' 'python2-setuptools' 'libsndfile' 'python-cffi' 'python2-cffi' 'python-numpy' 'python2-numpy')
source=("https://github.com/bastibe/PySoundFile/archive/${pkgver}.tar.gz")
sha256sums=('f53fc58b943827fee60e40ee87c11d1ff21cf6567c65449897371a4019be8c28')

build() {
  cp -r "${srcdir}"/SoundFile-$pkgver "${srcdir}"/SoundFile-$pkgver-py2

  cd "${srcdir}"/SoundFile-$pkgver
  python setup.py build

  cd "${srcdir}"/SoundFile-$pkgver-py2
  python2 setup.py build
}

package_python-soundfile() {
  depends=('python-cffi' 'libsndfile' 'python-numpy')

  cd "${srcdir}/SoundFile-$pkgver"
  python setup.py install --root=${pkgdir} --optimize=1
}

package_python2-soundfile() {
  depends=('python2-cffi' 'libsndfile' 'python2-numpy')

  cd "${srcdir}/SoundFile-$pkgver"
  python2 setup.py install --root=${pkgdir} --optimize=1
}

