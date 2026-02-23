#Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>
#Maintainer: Rafael Fontenelle <rafaelff at gnome dot org>

pkgname="mongodb-bin"
pkgver="8.2.4"
_basever="8.2"
_basedist="noble"
pkgrel=1
pkgdesc="A high-performance, open source, schema-free document-oriented database"
arch=("x86_64" "aarch64")
url="https://www.mongodb.com/"
license=("SSPL-1.0")
depends=(mongosh-bin curl openssl)
makedepends=(chrpath)
optdepends=("mongodb-tools: The MongoDB tools provide import, export, and diagnostic capabilities.")
provides=("mongodb=$pkgver")
conflicts=("mongodb" "mongodb-shell-bin")
backup=("etc/mongodb.conf")

_repo_url=https://repo.mongodb.org/apt/ubuntu/dists/${_basedist}/mongodb-org/${_basever}/multiverse
source=(
	"mongodb.sysusers"
	"mongodb.tmpfiles"
	"LICENSE"
)
source_x86_64=(
	mongodb-org-server_${pkgver}_x86_64.deb::"${_repo_url}/binary-amd64/mongodb-org-server_${pkgver}_amd64.deb"
	mongodb-org-mongos_${pkgver}_x86_64.deb::"${_repo_url}/binary-amd64/mongodb-org-mongos_${pkgver}_amd64.deb"
)
source_aarch64=(
	mongodb-org-server_${pkgver}_aarch64.deb::"${_repo_url}/binary-arm64/mongodb-org-server_${pkgver}_arm64.deb"
	mongodb-org-mongos_${pkgver}_aarch64.deb::"${_repo_url}/binary-arm64/mongodb-org-mongos_${pkgver}_arm64.deb"
)
noextract=(
	mongodb-org-server_${pkgver}_${CARCH}.deb
	mongodb-org-mongos_${pkgver}_${CARCH}.deb
)

sha256sums=('47b884569102f7c79017ee78ef2e98204a25aa834c0ee7d5d62c270ab05d4e2b'
            '51ee1e1f71598aad919db79a195778e6cb6cfce48267565e88a401ebc64497ac'
            '09d99ca61eb07873d5334077acba22c33e7f7d0a9fa08c92734e0ac8430d6e27')

sha256sums_x86_64=('b7ff31128c1a707039d44066b5afa3bf12744dae49fd01878a9ce53b9ac531c1'
                   'a85969cbe8ece8d226a4ff8cd8b06d2ca910bacad689a3cd94767615b9b7964f')
sha256sums_aarch64=('641a5ef7f4d7ac61c865f5c2870ba957eb55ce636ad5471288819ba3355b1eb7'
                    'aa749158ac3ef8413084bfe7f47883d46cf4dc1e936754fcaccc164626792a9c')

prepare() {
	mkdir -p output
	bsdtar -O -xf mongodb-org-server_${pkgver}_${CARCH}.deb data.tar.zst | bsdtar -C output -xJf - #server extracted
	bsdtar -O -xf mongodb-org-mongos_${pkgver}_${CARCH}.deb data.tar.zst | bsdtar -C output -xJf - #mongos extracted

	# Remove insecure RUNPATH '$ORIGIN/../lib' as reported by namcap
	chrpath -d output/usr/bin/mongos

	# Keep historical Arch dbPath
	sed -i 's|dbPath: /var/lib/mongo$|dbPath: /var/lib/mongodb|' output/etc/mongod.conf

	# Keep historical Arch conf file name
	sed -i 's|/etc/mongod.conf|/etc/mongodb.conf|' output/usr/lib/systemd/system/mongod.service

	# Keep historical Arch user name (no need for separate daemon group name)
	sed -i 's/User=mongod$/User=mongodb/' output/usr/lib/systemd/system/mongod.service
	sed -i 's/Group=mongod$/Group=mongodb/' output/usr/lib/systemd/system/mongod.service

	# Avoid legacy PID filepath
	sed -i 's|/var/run/|/var/|' output/usr/lib/systemd/system/mongod.service

	# Remove sysconfig file, used by upstream's init.d script not used on Arch
	sed -i '/^EnvironmentFile=/d' output/usr/lib/systemd/system/mongod.service

	# Make systemd wait as long as it takes for MongoDB to start
	# If MongoDB needs a long time to start, prevent systemd from restarting it every 90 seconds
	# See: https://jira.mongodb.org/browse/SERVER-38086
	sed -i 's/\[Service]/[Service]\nTimeoutStartSec=infinity/' output/usr/lib/systemd/system/mongod.service
}

package() {
	install -Dm644 output/etc/mongod.conf "$pkgdir/etc/mongodb.conf"
	install -Dm644 output/usr/lib/systemd/system/mongod.service "$pkgdir/usr/lib/systemd/system/mongodb.service"
	install -Dm755 output/usr/bin/* -t "$pkgdir/usr/bin"
	install -Dm644 output/usr/share/man/man1/* -t "$pkgdir/usr/share/man/man1"
	install -Dm644 mongodb.sysusers "$pkgdir/usr/lib/sysusers.d/mongodb.conf"
	install -Dm644 mongodb.tmpfiles "$pkgdir/usr/lib/tmpfiles.d/mongodb.conf"
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
