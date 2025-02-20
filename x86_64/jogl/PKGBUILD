# Maintainer: redponike <proton (dot) me>
# Contributor: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alexander Rødseth <rodseth@gmail.com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Simon Lipp <sloonz+aur@gmail.com>

pkgname=jogl
pkgver=2.5.0
pkgrel=1
pkgdesc="OpenGL bindings for Java"
arch=(x86_64 aarch64)
url="https://jogamp.org"
license=('BSD')
depends=('java-runtime' 'libgl')
source=("jogl.LICENSE.txt"
  "gluegen.LICENSE.txt"
  "jogl-all-v${pkgver}.jar::${url}/deployment/v${pkgver}/jar/jogl-all.jar"
  "gluegen-rt-v${pkgver}.jar::${url}/deployment/v${pkgver}/jar/gluegen-rt.jar")
source_aarch64=("jogl-all-natives-linux-aarch64-v${pkgver}.jar::${url}/deployment/v${pkgver}/jar/jogl-all-natives-linux-aarch64.jar"
  "gluegen-rt-natives-linux-aarch64-v${pkgver}.jar::${url}/deployment/v${pkgver}/jar/gluegen-rt-natives-linux-aarch64.jar")
source_x86_64=("jogl-all-natives-linux-amd64-v${pkgver}.jar::${url}/deployment/v${pkgver}/jar/jogl-all-natives-linux-amd64.jar"
  "gluegen-rt-natives-linux-amd64-v${pkgver}.jar::${url}/deployment/v${pkgver}/jar/gluegen-rt-natives-linux-amd64.jar")

md5sums=('e77015f08f0c8c3b39b9b7d379d57183'
         '3809542dae46666cb50b9cb7c6d5ac5f'
         '64c652f03e62a1cdb302cc1b948862ef'
         'db0859c3d735b9e93bb96115173f6c76')
md5sums_x86_64=('144bffd877fbf0f2f5333389b161a7e0'
                'ea956143f451c68d22b833464615c36e')
md5sums_aarch64=('1ecddb61541079e7e6c6cbc73f0412a9'
                 '1e28ac2f2de5ba2d4765f3c60a68e0e3')

noextract=("jogl-all-v${pkgver}.jar" "gluegen-rt-v${pkgver}.jar")

package() {
  # *.so files
  install -Ddm755 "${pkgdir}/usr/lib/${pkgname}"
  find "${srcdir}/natives" -type f -print0 | xargs -0 mv -t "${pkgdir}/usr/lib/${pkgname}"

  cd "${srcdir}"
  install -Dm644 "jogl-all-v${pkgver}.jar" "${pkgdir}/usr/share/java/${pkgname}/jogl-all.jar"
  install -Dm644 "gluegen-rt-v${pkgver}.jar" "${pkgdir}/usr/share/java/${pkgname}/gluegen-rt.jar"
  install -Dm644 "jogl.LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/jogl.LICENSE.txt"
  install -Dm644 "gluegen.LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/gluegen.LICENSE.txt"

  cd "${pkgdir}/usr/share/java/${pkgname}"
  ln -s "jogl-all.jar" "jogl2.jar"
  ln -s "gluegen-rt.jar" "gluegen2-rt.jar"

  cd "${pkgdir}/usr/lib"
  ln -s "jogl" "jogl2"
  ln -s "jogl" "gluegen2"
  ln -s "libgluegen-rt.so" "jogl/libgluegen2-rt.so"
}
