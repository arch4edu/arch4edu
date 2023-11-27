# Maintainer: Lawrence González <pentestian [at] airmail [dot] cc>
# Contributor: Jan Cholasta <grubber at grubber cz>

_name=gzdoom
pkgname=lzdoom
_pkgver=3.88b
pkgver=3.88.b
pkgrel=2
pkgdesc='Advanced Doom source port with OpenGL support (legacy version)'
arch=('i686' 'x86_64')
url='http://www.zdoom.org/'
license=('BSD' 'custom:dumb' 'GPL3' 'LGPL3')
conflicts=('lzdoom-bin')
depends=('hicolor-icon-theme' 'libjpeg' 'sdl2' 'alsa-lib')
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
sha256sums=('a9d0b425bc4ee39dc237e1e8f06e3504e13ccb6d6a5e6d44cb8ce6964a1ce43b'
            '7b3ffa8b74e5d6283206dd074b09e944aa07670ec7d7b1fe587350ffb91819b3')

prepare() {
	cd "$srcdir/${_name}-$_pkgver"

	# Patches GCC 11 errors
	sed -i '/^#include "types\.h"$/a \#include <limits>' src/scripting/types.cpp

	# Patches soundfonts paths
	sed -i -f - src/gameconfigfile.cpp <<- "EOF"
		\%^\t\tSetValueForKey("Path", "/usr/share/games/doom/fm_banks", true);$% a \
		\t\tSetValueForKey("Path", SHARE_DIR "/soundfonts", true);\
		\t\tSetValueForKey("Path", SHARE_DIR "/fm_banks", true);\
		\t\tSetValueForKey("Path", "/usr/share/soundfonts", true);
		EOF
}

build() {
	cd "$srcdir/${_name}-$_pkgver"

	local _cflags="-ffile-prefix-map=\"$PWD\"=. \
					-DSHARE_DIR=\\\"/usr/share/$pkgname\\\" \
					-DFLUIDSYNTHLIB2=\\\"libfluidsynth.so.2\\\""
	cmake -DCMAKE_BUILD_TYPE=Release \
			-DCMAKE_C_FLAGS="${CFLAGS} ${_cflags}" \
			-DCMAKE_CXX_FLAGS="${CXXFLAGS} ${_cflags}" \
			-DCMAKE_EXE_LINKER_FLAGS="${LDFLAGS} -Wl,-z,noexecstack" \
			-DCMAKE_INSTALL_PREFIX=/usr \
			-DINSTALL_PATH=bin \
			-DINSTALL_PK3_PATH="share/$pkgname" \
			.
	make
}

package() {
	cd "$srcdir/${_name}-$_pkgver"

	make install DESTDIR="$pkgdir"
	install -D -m644 "soundfonts/${pkgname}.sf2" \
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
