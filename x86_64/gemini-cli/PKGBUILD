pkgname=gemini-cli
pkgver=0.6.0
pkgrel=1
epoch=1
pkgdesc="An open-source AI agent that brings the power of Gemini directly into your terminal. "
arch=('x86_64')
url="https://github.com/google-gemini/gemini-cli"
license=('Apache-2.0')
makedepends=('npm')
depends=('nodejs')
source=("https://registry.npmjs.org/@google/$pkgname/-/$pkgname-$pkgver.tgz")
sha256sums=('3cd5b6f462f0ef108421530e9d9eed92f0d557fb2ff2d6712845b8f0cbbd2c18')

package() {
  npm install -g --prefix "${pkgdir}/usr" "${srcdir}/${pkgname}-${pkgver}.tgz"
}
