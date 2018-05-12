# Maintainer: zopieux <web+oss at zopieux dot com>

_pkgname=lua-cjson
_lua_version=5.1
_lua_version_nodot=${_lua_version//./}

pkgname=lua${_lua_version_nodot}-cjson
pkgver=2.1.0
pkgrel=1
pkgdesc="A fast JSON parsing and encoding support for Lua."
arch=(i686 x86_64)
url="https://www.kyne.com.au/~mark/software/lua-cjson.php"
license=('custom:MIT')
depends=("lua${_lua_version_nodot}")
optdepends=('perl: UTF8 implementation test')
source=("https://www.kyne.com.au/~mark/software/download/$_pkgname-$pkgver.tar.gz")
md5sums=('24f270663e9f6ca8ba2a02cef19f7963')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  make PREFIX=/usr LUA_INCLUDE_DIR=/usr/include/lua${_lua_version} LUA_VERSION=${_lua_version}
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  make PREFIX=/usr DESTDIR="$pkgdir/" LUA_INCLUDE_DIR=/usr/include/lua${_lua_version} LUA_VERSION=${_lua_version} install{,-extra}

  # license
  install -Dm644 LICENSE \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # use lua5.1
  sed -i "1s|env lua|&${_lua_version}|" $(grep -rl "env lua" "$pkgdir")

  # do not conflict with lua-cjson
  cd "$pkgdir/usr/bin"
  mv lua2json lua${_lua_version_nodot}2json
  mv json2lua json2lua${_lua_version_nodot}
}

# vim:set ts=2 sw=2 et:
