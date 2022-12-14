# Maintainer: Severen Redwood <me@severen.dev>
# Contributor: Tomasz Jakub Rup <tomasz.rup@gmail.com>

pkgname=pnpm
pkgver=7.18.2
pkgrel=1
pkgdesc="Fast, disk space efficient package manager"
arch=("any")
url="https://pnpm.js.org/"
license=("MIT")
depends=("nodejs>=14.6.0")
makedepends=("git" "npm" "jq")
source=("git+https://github.com/$pkgname/$pkgname.git?signed#tag=v$pkgver")
sha256sums=('SKIP')
validpgpkeys=("7B74D1299568B586BA9962B5649E4D4AF74E7DEC") # Zoltan Kochan <z@kochan.io>

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
