# Maintainer: Tomasz Jakub Rup <tomasz.rup@gmail.com>

pkgname=pnpm
pkgver=7.14.2
pkgrel=1
pkgdesc="Fast, disk space efficient package manager"
arch=('any')
url="https://pnpm.js.org/"
license=('MIT')
depends=('nodejs>=14.6.0')
makedepends=('git' 'npm' 'jq')
source=("git+https://github.com/pnpm/pnpm.git?signed#tag=v$pkgver")
sha256sums=('SKIP')
validpgpkeys=("7B74D1299568B586BA9962B5649E4D4AF74E7DEC") # Zoltan Kochan <z@kochan.io>

package() {
	npm install -g --user root --prefix "$pkgdir"/usr "$pkgname"
	local _npmdir="$pkgdir/usr/lib/node_modules/$pkgname"
	find "$pkgdir"/usr -type d -exec chmod 755 {} +
	chown -R root:root "$pkgdir"
	find "$pkgdir"/usr/lib -depth -name '*.map' -delete
	install -Dm644 "$_npmdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm644 "$_npmdir/README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
	rm -rf "$pkgdir/usr/etc" "$_npmdir/LICENSE" "$_npmdir/README.md"

	local tmppackage="$(mktemp)"
	jq '.|=with_entries(select(.key|test("_.+")|not))' "$_npmdir/package.json" > "$tmppackage"
	mv "$tmppackage" "$_npmdir/package.json"
	chmod 644 "$_npmdir/package.json"
}
