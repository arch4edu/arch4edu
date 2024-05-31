#Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>
#Maintainer: Rafael Fontenelle <rafaelff at gnome dot org>

pkgname="mongodb-bin"
pkgver="7.0.11"
_basever="7.0"
_basedist="focal"
pkgrel=1
pkgdesc="A high-performance, open source, schema-free document-oriented database"
arch=("x86_64" "aarch64")
url="https://www.mongodb.com/"
license=("SSPL-1.0")
depends=(mongosh-bin curl openssl-1.1)
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
sha256sums_x86_64=('7eac4d52ca54fbbcc561edb95376cca14aa7ab8777cdd02d2026c22550f2e40d'
					'53760e9ea7e4b018eac0fdf0bab85a713db588b49a6236247402bd2dcf58e741')
sha256sums_aarch64=('521099b2f868b04a5c0a777f8ee547b2d70ecd5241af94fe5f2d7b9c45843af8'
					'd4e8cccb288ac431a74cb7bac499d1b6a23aab393219b9cd3d3bef72c5135c72')

prepare() {
	mkdir -p output
	bsdtar -O -xf mongodb-org-server_${pkgver}_${CARCH}.deb data.tar.xz | bsdtar -C output -xJf - #server extracted
	bsdtar -O -xf mongodb-org-mongos_${pkgver}_${CARCH}.deb data.tar.xz | bsdtar -C output -xJf - #mongos extracted

	# Remove insecure RUNPATH '$ORIGIN/../lib' as reported by namcap
	chrpath -d output/usr/bin/mongos

	# Keep historical Arch dbPath
	sed -i 's|dbPath: /var/lib/mongo$|dbPath: /var/lib/mongodb|' output/etc/mongod.conf

	# Keep historical Arch conf file name
	sed -i 's|/etc/mongod.conf|/etc/mongodb.conf|' output/lib/systemd/system/mongod.service

	# Keep historical Arch user name (no need for separate daemon group name)
	sed -i 's/User=mongod$/User=mongodb/' output/lib/systemd/system/mongod.service
	sed -i 's/Group=mongod$/Group=mongodb/' output/lib/systemd/system/mongod.service

	# Avoid legacy PID filepath
	sed -i 's|/var/run/|/var/|' output/lib/systemd/system/mongod.service

	# Remove sysconfig file, used by upstream's init.d script not used on Arch
	sed -i '/^EnvironmentFile=/d' output/lib/systemd/system/mongod.service

	# Make systemd wait as long as it takes for MongoDB to start
	# If MongoDB needs a long time to start, prevent systemd from restarting it every 90 seconds
	# See: https://jira.mongodb.org/browse/SERVER-38086
	sed -i 's/\[Service]/[Service]\nTimeoutStartSec=infinity/' output/lib/systemd/system/mongod.service
}

package() {
	install -Dm644 output/etc/mongod.conf "$pkgdir/etc/mongodb.conf"
	install -Dm644 output/lib/systemd/system/mongod.service "$pkgdir/usr/lib/systemd/system/mongodb.service"
	install -Dm755 output/usr/bin/* -t "$pkgdir/usr/bin"
	install -Dm644 output/usr/share/man/man1/* -t "$pkgdir/usr/share/man/man1"
	install -Dm644 mongodb.sysusers "$pkgdir/usr/lib/sysusers.d/mongodb.conf"
	install -Dm644 mongodb.tmpfiles "$pkgdir/usr/lib/tmpfiles.d/mongodb.conf"
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
