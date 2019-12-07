# Maintainer: K. Morton <pryre.dev@outlook.com>
# Contributor: Anselmo L. S. Melo <anselmo.melo@intel.com>
pkgname=qgroundcontrol
pkgver=3.5.6
pkgrel=1
pkgdesc="Micro air vehicle ground control station."
arch=('x86_64')
url="http://qgroundcontrol.org/"
license=('GPL3')

#Git commit hash for version-specific submodules
pkgver_mavlink='d240d0986710045663894aebcea89e71ce981ee4' #libs/mavlink/include/mavlink
pkgver_gps='2a4865adc3808687d6c6f550f497a02eb920c382' #src/GPS/Drivers

depends=('bzip2'
		 'dbus'
		 'flac'
		 'gst-plugins-base-libs'
		 'libasyncns'
		 'libffi'
		 'libgcrypt'
		 'libgpg-error'
		 'libogg'
		 'libsndfile'
		 'libsystemd'
		 'libunwind'
		 'libx11'
		 'libxau'
		 'libxcb'
		 'libxdmcp'
		 'libxext'
		 'lz4'
		 'orc'
		 'pcre'
		 'sdl2'
		 'xz'
		 'zlib'
		 'icu'
		 'qt5-speech'
		 'qt5-multimedia'
		 'qt5-serialport'
		 'qt5-charts'
		 'qt5-quickcontrols'
		 'qt5-quickcontrols2'
		 'qt5-location'
		 'qt5-svg'
		 'qt5-graphicaleffects'
)

makedepends=('git' 'qt5-base')

source=("qgroundcontrol-${pkgver}.tar.gz::https://github.com/mavlink/qgroundcontrol/archive/v${pkgver}.tar.gz"
		"mavlink-v2.0-qgc${pkgver}.zip::https://github.com/mavlink/c_library_v2/archive/${pkgver_mavlink}.zip"
		"gps-drivers-qgc${pkgver}.zip::https://github.com/PX4/GpsDrivers/archive/${pkgver_gps}.zip"
)

sha256sums=('5ae468336dddab5843c8c3df7cd7607b5fd394fda2900ce684d771c0dff9d1df'
			'65c0fc60be9435375f74990a5c83fb0cdef6d15c100245759d2465d480a5b9b5'
			'1ab58c633edcfff9288bd868bf33e2c9990afa27fa5df8f1731675d98a4ce6e4'
)

prepare() {
	mavlinkdir="c_library_v2-${pkgver_mavlink}"
	gpsdir="GpsDrivers-${pkgver_gps}"

	mkdir -p "${srcdir}/${pkgname}-${pkgver}/build"

	# Copy in the mavlink source
	rm -r "${srcdir}/${pkgname}-${pkgver}/libs/mavlink/include/mavlink/v2.0"
	cp -R "${srcdir}/${mavlinkdir}" "${srcdir}/${pkgname}-${pkgver}/libs/mavlink/include/mavlink/"
	mv "${srcdir}/${pkgname}-${pkgver}/libs/mavlink/include/mavlink/${mavlinkdir}" "${srcdir}/${pkgname}-${pkgver}/libs/mavlink/include/mavlink/v2.0"
	# Copy in the GPS source
	rm -r "${srcdir}/${pkgname}-${pkgver}/src/GPS/Drivers"
	cp -R "${srcdir}/${gpsdir}" "${srcdir}/${pkgname}-${pkgver}/src/GPS/"
	mv "${srcdir}/${pkgname}-${pkgver}/src/GPS/${gpsdir}" "${srcdir}/${pkgname}-${pkgver}/src/GPS/Drivers"

	cd "${srcdir}/${pkgname}-${pkgver}/"
	patch --strip=1 < "${startdir}/${pkgname}-libicudata.patch"
	patch --strip=1 < "${startdir}/${pkgname}-mavlink-warn.patch"
}

build() {
	cd "$srcdir/${pkgname}-${pkgver}/build"
	qmake ../qgroundcontrol.pro
	make

	echo "[Desktop Entry]
Type=Application
Name=QGroundControl Release
Comment=Ground control for unmanned vehicles
Path=/opt/${pkgname}/
Exec=/usr/bin/${pkgname}
Icon=/opt/${pkgname}/qgroundcontrol.png
Terminal=false
Categories=Qt;Utility;" > "$srcdir/${pkgname}.desktop"
}

package() {
	mkdir -p "${pkgdir}/opt" "${pkgdir}/usr/bin" "${pkgdir}/usr/share/applications"
	cp -R "${srcdir}/${pkgname}-${pkgver}/build/release" "${pkgdir}/opt/${pkgname}"
	cp "${srcdir}/${pkgname}-${pkgver}/resources/icons/qgroundcontrol.png" "${pkgdir}/opt/${pkgname}"
	cp "${srcdir}/${pkgname}-${pkgver}/deploy/qgroundcontrol-start.sh" "${pkgdir}/opt/${pkgname}"

	# Remove the default one as we want to use our own desktop file
	rm "${pkgdir}/opt/${pkgname}/${pkgname}.desktop"
	cp "${srcdir}/${pkgname}.desktop" "${pkgdir}/opt/${pkgname}"

	ln -s "/opt/${pkgname}/qgroundcontrol-start.sh" "${pkgdir}/usr/bin/${pkgname}"
	ln -s "/opt/${pkgname}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}

# vim:set ts=2 sw=2 et:
