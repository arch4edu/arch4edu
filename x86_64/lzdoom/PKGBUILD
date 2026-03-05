# Maintainer: Lawrence González <pentestian [at] airmail [dot] cc>
# Contributor: Jan Cholasta <grubber at grubber cz>

_name=gzdoom
pkgname=lzdoom
_pkgver=l4.14.3a
pkgver=4.14.3a
pkgrel=1
pkgdesc='Advanced Doom source port with OpenGL support (legacy version)'
arch=('i686' 'x86_64')
url='http://www.zdoom.org/'
license=('BSD-3-Clause AND GPL-3.0-or-later AND LGPL-3.0-or-later AND bzip2-1.0.6 AND LicenseRef-DUMB AND LicenseRef-Lucent')
conflicts=('lzdoom-bin')
options=("!lto")
depends=('hicolor-icon-theme' 'sdl2' 'zmusic' 'libvpx' 'bzip2' 'glibc' 'gcc-libs')
makedepends=('cmake' 'fluidsynth>=2' 'gtk3')
optdepends=('blasphemer-wad: Blasphemer (free Heretic) game data'
			'chexquest3-wad: Chex Quest 3 game data'
			'doom1-wad: Doom shareware game data'
			'fluidsynth>=2: FluidSynth MIDI device'
			'timidity++: Timidity++ MIDI device'
			'freedm: FreeDM game data'
			'freedoom1: Freedoom: Phase 1 game data'
			'freedoom2: Freedoom: Phase 2 game data'
			'gtk3: IWAD selection dialog'
			'gxmessage: crash dialog (GNOME)'
			'hacx-wad: HacX game data'
			'harmony-wad: Harmony game data'
			'heretic1-wad: Heretic shareware game data'
			'hexen1-wad: Hexen demo game data'
			'kdialog: crash dialog (KDE)'
			'libsndfile: WAV/FLAC/OGG audio support'
			'mpg123: MP3 audio support'
			'openal: in-game sound'
			'soundfont-fluid: FluidR3 soundfont for FluidSynth'
			'strife0-wad: Strife shareware game data'
			'square1-wad: The Adventures of Square, Episode 1 game data'
			'urbanbrawl-wad: Urban Brawl: Action Doom 2 game data'
			'xorg-xmessage: crash dialog (other)')
source=("${pkgname}-${_pkgver}.tar.gz::https://github.com/drfrag666/${_name}/archive/refs/tags/${_pkgver}.tar.gz"
		"${pkgname}.desktop")
sha256sums=('dbb8dc288bba1f0b14764d76d84250bbdfdb85db25e82cbb2debd5185cb259e8'
            '7b3ffa8b74e5d6283206dd074b09e944aa07670ec7d7b1fe587350ffb91819b3')

prepare() {
	cd "$srcdir/${pkgname}-$_pkgver"

	# Patches soundfonts paths
	sed -i -f - src/gameconfigfile.cpp <<- "EOF"
		\%^\t\tSetValueForKey("Path", "/usr/share/games/doom/fm_banks", true);$% a \
		\t\tSetValueForKey("Path", SHARE_DIR "/soundfonts", true);\
		\t\tSetValueForKey("Path", SHARE_DIR "/fm_banks", true);\
		\t\tSetValueForKey("Path", "/usr/share/soundfonts", true);
		EOF
}

build() {
	cd "$srcdir/${pkgname}-$_pkgver"
	mkdir -p build
	cd build

	local _cflags="-ffile-prefix-map=\"$PWD\"=. \
					-DSHARE_DIR=\\\"/usr/share/$pkgname\\\" \
					-DFLUIDSYNTHLIB2=\\\"libfluidsynth.so.2\\\""

	cmake -DINSTALL_PK3_PATH="share/$pkgname" \
		-DINSTALL_SOUNDFONT_PATH=share/lzdoom \
		-DINSTALL_RPATH=/usr/lib \
		-DSYSTEMINSTALL=ON \
		-DCMAKE_CXX_FLAGS="$_cflags" \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr \
		-DCMAKE_BUILD_TYPE=RelWithDebInfo \
		..
	make
}

package() {
	cd "$srcdir/${pkgname}-$_pkgver"

	make -C build install DESTDIR="$pkgdir"
	install -D -m644 "soundfont/${pkgname}.sf2" \
			"$pkgdir/usr/share/$pkgname/soundfonts/${pkgname}.sf2"
	install -D -m644 fm_banks/GENMIDI.GS.wopl \
			"$pkgdir/usr/share/$pkgname/fm_banks/GENMIDI.GS.wopl"
	install -D -m644 fm_banks/gs-by-papiezak-and-sneakernets.wopn \
			"$pkgdir/usr/share/$pkgname/fm_banks/gs-by-papiezak-and-sneakernets.wopn"

	install -D -m644 "$srcdir/${pkgname}.desktop" \
			"$pkgdir/usr/share/applications/${pkgname}.desktop"
	install -D -m644 src/posix/zdoom.xpm \
			"$pkgdir/usr/share/icons/hicolor/256x256/apps/${pkgname}.xpm"
	install -D -m644 "ico_${pkgname}.png" \
			"$pkgdir/usr/share/icons/hicolor/496x496/apps/${pkgname}.png"

	install -D -m644 -t "$pkgdir/usr/share/licenses/$pkgname" docs/licenses/*
}
