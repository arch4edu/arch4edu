# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Simon Legner <Simon.Legner@gmail.com>

pkgname=bazel
pkgver=0.4.2
pkgrel=1
pkgdesc="Correct, reproducible, and fast builds for everyone"
arch=('i686' 'x86_64')
url='https://bazel.io/'
license=('Apache')
depends=('java-environment>=8' 'libarchive' 'zip' 'unzip')
makedepends=('git' 'protobuf')
options=('!distcc' '!strip')
source=("https://github.com/bazelbuild/bazel/releases/download/${pkgver}/bazel-${pkgver}-dist.zip"
        "https://github.com/bazelbuild/bazel/releases/download/${pkgver}/bazel-${pkgver}-dist.zip.sig")
sha512sums=('6df536990f085cc58eeeaa495deef9c6df7508d1947b39f62ad006a0d9ff151959999bb5c043270cf6475dfb611f7301cc1e9858ad78c5ba6eec95ea83783125'
            'SKIP')
validpgpkeys=('71A1D0EFCFEB6281FD0437C93D5919B448457EE0')

build() {
  ./compile.sh
  ./output/bazel build scripts:bazel-complete.bash
  cd output
  ./bazel shutdown
}

package() {
  pwd
  install -Dm755 ${srcdir}/output/bazel ${pkgdir}/usr/bin/bazel
  install -Dm755 ${srcdir}/bazel-bin/scripts/bazel-complete.bash ${pkgdir}/etc/bash_completion.d/bazel-complete.bash
  mkdir -p ${pkgdir}/opt/bazel/
  for d in examples third_party tools; do
    cp -r ${srcdir}/${d} ${pkgdir}/opt/bazel/
  done
}
