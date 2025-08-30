pkgname=gemini-cli
pkgver=0.2.2
pkgrel=1
pkgdesc="An open-source AI agent that brings the power of Gemini directly into your terminal. "
arch=('x86_64')
url="https://github.com/google-gemini/gemini-cli"
license=('Apache-2.0')
makedepends=('npm')
depends=('nodejs')
source=("https://registry.npmjs.org/@google/$pkgname/-/$pkgname-$pkgver.tgz")
sha256sums=('5cba2f88c33f809dfcdc3e46490da05aca7c3fd121c6340b6e040398dafd1612')

package() {
  npm install -g --prefix "${pkgdir}/usr" "${srcdir}/${pkgname}-${pkgver}.tgz"
}
