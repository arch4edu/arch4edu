# Maintainer: Severen Redwood <me@severen.dev>
# Contributor: Tomasz Jakub Rup <tomasz.rup@gmail.com>

pkgname=pnpm
pkgver=8.5.0
pkgrel=1
pkgdesc="Fast, disk space efficient package manager"
arch=("any")
url="https://pnpm.js.org/"
license=("MIT")
depends=("nodejs>=16.14")
makedepends=("git" "npm" "jq")
source=("$pkgname-$pkgver.tar.gz::https://github.com/pnpm/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('f69c7ef19d5c3e9fefa1b0a52ba5814dfd3f97c0a19ba35d6aa8af3a920108a2')

package() {
  npm install -g \
    --cache "$srcdir/npm-cache" \
    --prefix "$pkgdir/usr" \
    "$pkgname"

  # Fix permissions and ownership.
  # See: https://bugs.archlinux.org/task/63396
  find "$pkgdir/usr" -type d -exec chmod 755 {} +
  chown -R root:root "$pkgdir"

  # Delete unnecessary JavaScript source maps.
  find "$pkgdir/usr/lib" -depth -name "*.map" -delete

  # Move README and LICENSE to the appropriate location.
  local _npmdir="$pkgdir/usr/lib/node_modules/$pkgname"
  install -Dm644 "$_npmdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 "$_npmdir/README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
  rm -rf "$pkgdir/usr/etc" "$_npmdir/LICENSE" "$_npmdir/README.md"

  # Remove references to $srcdir and $pkgdir.
  # See: https://wiki.archlinux.org/title/Node.js_package_guidelines#Package_contains_reference_to_$srcdir/$pkgdir
  local _tmp_package="$(mktemp)"
  jq '.|=with_entries(select(.key|test("_.+")|not))' "$_npmdir/package.json" > "$_tmp_package"
  mv "$_tmp_package" "$_npmdir/package.json"
  chmod 644 "$_npmdir/package.json"
}
