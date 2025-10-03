pkgname=gemini-cli
pkgver=0.7.0
pkgrel=1
epoch=1
pkgdesc="An open-source AI agent that brings the power of Gemini directly into your terminal. "
arch=('x86_64')
url="https://github.com/google-gemini/gemini-cli"
license=('Apache-2.0')
makedepends=('npm')
depends=('nodejs')
source=("https://registry.npmjs.org/@google/$pkgname/-/$pkgname-$pkgver.tgz")
sha256sums=('a9cc6e57d470158b533b564f746f2d7409308870567ef2c9efd9b3a66b916741')

package() {
  npm install -g --prefix "${pkgdir}/usr" "${srcdir}/${pkgname}-${pkgver}.tgz"
}
