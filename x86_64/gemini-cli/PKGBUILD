pkgname=gemini-cli
pkgver=0.1.18
pkgrel=1
pkgdesc="An open-source AI agent that brings the power of Gemini directly into your terminal. "
arch=('x86_64')
url="https://github.com/google-gemini/gemini-cli"
license=('Apache-2.0')
makedepends=('npm')
depends=('nodejs')
source=("https://registry.npmjs.org/@google/$pkgname/-/$pkgname-$pkgver.tgz")
sha256sums=('35d5d1f5807ecf9204fb856adf45567af4cc22c9e814f7dad8f358d55530856d')

package() {
  npm install -g --prefix "${pkgdir}/usr" "${srcdir}/${pkgname}-${pkgver}.tgz"
}
