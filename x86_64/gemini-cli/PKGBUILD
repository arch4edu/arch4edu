pkgname=gemini-cli
pkgver=0.1.22
pkgrel=1
pkgdesc="An open-source AI agent that brings the power of Gemini directly into your terminal. "
arch=('x86_64')
url="https://github.com/google-gemini/gemini-cli"
license=('Apache-2.0')
makedepends=('npm')
depends=('nodejs')
source=("https://registry.npmjs.org/@google/$pkgname/-/$pkgname-$pkgver.tgz")
sha256sums=('e62d207a949175f9044146bd7bdc4a7d2926265ab07b86901aca77c79bf5bfd8')

package() {
  npm install -g --prefix "${pkgdir}/usr" "${srcdir}/${pkgname}-${pkgver}.tgz"
}
