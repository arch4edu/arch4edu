# Maintainer: NicoHood <archlinux {cat} nicohood {dog} de>
# PGP ID: 97312D5EB9D7AE7D0BD4307351DAE9B7C1AE9161

pkgname=arduino-builder
pkgver=1.6.1
pkgrel=3
pkgdesc="A command line tool for compiling Arduino sketches"
arch=('x86_64')
url="https://github.com/arduino/arduino-builder"
license=('GPL')
depends=('arduino-ctags')
makedepends=('go' 'git' 'unzip')
optdepends=('arduino-avr-core: AVR core with upstream avr-gcc and avrdude')
source=("${pkgname}-${pkgver}.tar.xz::https://github.com/arduino/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.xz"
		"${pkgname}-${pkgver}.tar.xz.asc::https://github.com/arduino/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.xz.asc")
sha512sums=('b6e8bf43ad343e98c3d71985dbbaefee27f51c5d31248f920d4880446a3e6b5f0ea0461f61e65b2e3205e4c0a06696390c401198b7b0e8fd16cdc874da4f451b'
            'SKIP')
validpgpkeys=('326567C1C6B288DF32CB061A95FA6F43E21188C4') # Arduino Packages <support@arduino.cc>

build()
{
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

	cd "${srcdir}/${pkgname}-${pkgver}"
	go build

	# TODO Fix ctags test environment at build time
	# https://github.com/arduino/arduino-builder/issues/202
}

#check()
#{
	# Test will download ~1GB of testfiles
	#echo "Running check() for the first time might take a while as it downloads ~1GB of testfiles. Skip with --nocheck"
	#cd "${srcdir}/${pkgname}-${pkgver}"
	#go test -timeout 60m github.com/arduino/arduino-cli/...
#}

package()
{
	cd "${srcdir}/${pkgname}-${pkgver}"

	# Install main tool
	install -Dm755 "arduino-builder" "${pkgdir}/usr/bin/arduino-builder"

	# Install platform.txt files
	install -Dm644 -t "${pkgdir}/usr/share/arduino/hardware/" "${srcdir}"/${pkgname}-${pkgver}/hardware/*

	# Fix platform.txt for arch arduino-ctags
	echo 'tools.ctags.path=/usr/bin' > "${pkgdir}/usr/share/arduino/hardware/platform.txt"
	echo 'tools.ctags.cmd.path={path}/arduino-ctags' >> "${pkgdir}/usr/share/arduino/hardware/platform.txt"

	# Add documentation
	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" "${srcdir}/${pkgname}-${pkgver}/README.md"
}
