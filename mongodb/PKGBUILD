# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>
# Maintainer: Christoph Bayer <chrbayer@criby.de>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Mathias Stearn <mathias@10gen.com>
# Contributor: Alec Thomas
# Contributor: Fredy García <frealgagu at gmail dot com>

pkgname=mongodb
# #.<odd number>.# releases are unstable development/testing
pkgver=4.2.1
pkgrel=1
pkgdesc="A high-performance, open source, schema-free document-oriented database"
arch=("x86_64")
url="https://www.${pkgname}.com/"
license=("custom:SSPL")
# lsb-release::/etc/lsb-release required by src/mongo/util/processinfo_linux.cpp::getLinuxDistro()
depends=("curl" "libstemmer" "lsb-release" "snappy" "gperftools")
optdepends=("${pkgname}-tools: mongoimport, mongodump, mongotop, etc")
makedepends=("scons" "python-psutil" "python-setuptools" "python-regex" "python-cheetah3" "python-yaml" "python-requests")
checkdepends=("python-pymongo")
backup=("etc/${pkgname}.conf")
source=(
  "http://downloads.${pkgname}.org/src/${pkgname}-src-r${pkgver}.tar.gz"
  "${pkgname}.sysusers"
  "${pkgname}.tmpfiles"
)
sha256sums=('6d0e82e70b6940698ed464e11894c441db5f07c98a0e16e1607283277553683a'
            '3757d548cfb0e697f59b9104f39a344bb3d15f802608085f838cb2495c065795'
            'b7d18726225cd447e353007f896ff7e4cbedb2f641077bce70ab9d292e8f8d39')

_scons_args=(
  #--use-system-pcre # wait for pcre 8.44+ https://jira.mongodb.org/browse/SERVER-40836 and https://jira.mongodb.org/browse/SERVER-42990
  --use-system-snappy
  # --use-system-yaml # https://jira.mongodb.org/browse/SERVER-43980
  --use-system-zlib
  #--use-system-wiredtiger # https://jira.mongodb.org/browse/SERVER-42813 upstream broke this in 4.2.0, says in meantime not to use it
  --use-system-stemmer
  --use-sasl-client
  --ssl
  --disable-warnings-as-errors
  # --use-system-asio     # https://jira.mongodb.org/browse/SERVER-21839 marked as fixed, but still doesn't compile.  MongoDB uses custom patches.
  # --use-system-icu      # Doesn't compile
  --use-system-tcmalloc   # in gperftools
  # --use-system-boost    # Doesn't compile
  # --use-system-valgrind # Compiles, but namcap says not used
  # --use-system-sqlite   #   "
  # --use-system-mongo-c  # Doesn't compile
)

prepare() {
  cd "${srcdir}/${pkgname}-src-r${pkgver}"

  # Keep historical Arch dbPath
  sed -i 's|dbPath: /var/lib/mongo|dbPath: /var/lib/mongodb|' rpm/mongod.conf

  # Keep historical Arch conf file name
  sed -i 's|-f /etc/mongod.conf|-f /etc/mongodb.conf|' rpm/mongod.service

  # Keep historical Arch user name (no need for separate daemon group name)
  sed -i 's/User=mongod/User=mongodb/' rpm/mongod.service
  sed -i 's/Group=mongod/Group=mongodb/' rpm/mongod.service
  sed -i 's/chown mongod:mongod/chown mongodb:mongodb/' rpm/mongod.service

  # Remove sysconfig file, used by upstream's init.d script not used on Arch
  sed -i '/EnvironmentFile=-\/etc\/sysconfig\/mongod/d' rpm/mongod.service

  # Make systemd wait as long as it takes for MongoDB to start
  # If MongoDB needs a long time to start, prevent systemd from restarting it every 90 seconds
  # See: https://jira.mongodb.org/browse/SERVER-38086
  sed -i 's/\[Service]/[Service]\nTimeoutStartSec=infinity/' rpm/mongod.service

  # Prevent building using debug symbols, since binaries will be stripped anyway
  # Reduces makepkg -- which fully runs check() -- build size from 259GB to 2.3GB, and time by at least 37%
  # See: https://jira.mongodb.org/browse/SERVER-44038
  sed -i '/"-ggdb" if not env.TargetOSIs/d' SConstruct
}

build() {
  cd "${srcdir}/${pkgname}-src-r${pkgver}"

  export SCONSFLAGS="$MAKEFLAGS"
  scons core "${_scons_args[@]}"
}

check() {
  # Before 4.2.0, only 8 unit tests would fail under devtools, because mlock() is not available under systemd-nspawn
  # See https://jira.mongodb.org/browse/SERVER-32773
  # 4.2.0 uses mlock() in many more places.  At first attempt, I had 24 tests pass, and 345 skipped due to the failing test.
  # After repeatedly re-running check() to find additional failures and increasing skipping 8 unit tests to 27, only had an extra 2 passing
  # Disabling unit tests entirely, the db tests fail as well
  # Also disabling the db tests, the integration tests fail as well
  # It's not practical to re-run check() hundreds of more times to pick up a few additional tests, so they will just all be skipped through devtools

  # I'd use "systemd-detect-virt" to detect systemd-nspawn, but it only succeeds running as root, saying there is "none" as builduser
  if [[ -f /chrootbuild ]]; then
    echo "devtools detected, skipping check() because tests fail not being able to use mlock() within systemd-nspawn"
  else
    cd "${srcdir}/${pkgname}-src-r${pkgver}"

    export SCONSFLAGS="$MAKEFLAGS"

    scons unittests "${_scons_args[@]}"

    python "${srcdir}/${pkgname}-src-r${pkgver}/buildscripts/resmoke.py" --suites=unittests

    scons dbtest "${_scons_args[@]}"
    python "${srcdir}/${pkgname}-src-r${pkgver}/buildscripts/resmoke.py" --suites=dbtest

    scons integration_tests "${_scons_args[@]}"
    python "${srcdir}/${pkgname}-src-r${pkgver}/buildscripts/resmoke.py" --suites=integration_tests_replset,integration_tests_standalone --dbpathPrefix="${srcdir}"
  fi
}

package() {
  cd "${srcdir}/${pkgname}-src-r${pkgver}"

  scons install --prefix="${pkgdir}/usr" "${_scons_args[@]}"

  # Keep historical Arch conf file name
  install -Dm644 "rpm/mongod.conf" "${pkgdir}/etc/${pkgname}.conf"

  # Keep historical Arch service name
  install -Dm644 "rpm/mongod.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"

  # Install manpages
  install -Dm644 "debian/mongo.1" "${pkgdir}/usr/share/man/man1/mongo.1"
  install -Dm644 "debian/mongod.1" "${pkgdir}/usr/share/man/man1/mongod.1"
  install -Dm644 "debian/mongos.1" "${pkgdir}/usr/share/man/man1/mongos.1"

  install -Dm644 "${srcdir}/${pkgname}.sysusers" "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"
  install -Dm644 "${srcdir}/${pkgname}.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"
  install -Dm644 LICENSE-Community.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE-Community.txt"

  # This script won't run on Arch. If needed, see AUR package mongodb-compass.
  rm "${pkgdir}/usr/bin/install_compass"
}
