# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>

pkgname=jrosetta
pkgver=1.0.4
pkgrel=5
pkgdesc="Graphical console engine for Swing"
arch=('any')
url="http://dev.artenum.com/projects/JRosetta/"
license=('GPL2')
depends=('java-runtime')
#source=("http://maven.artenum.com/content/groups/public/com/artenum/jrosetta/jrosetta-api/$pkgver/jrosetta-api-$pkgver.jar"
#"http://maven.artenum.com/content/groups/public/com/artenum/jrosetta/jrosetta-engine/$pkgver/jrosetta-engine-$pkgver.jar")
source=(
"https://mrwitek.github.io/aur-repo/jrosetta-api-1.0.4.jar"
"https://mrwitek.github.io/aur-repo/jrosetta-engine-1.0.4.jar"
)
md5sums=('00082a2e745c8e0042608650334a9aaf'
         'cdef53b29bce0ccd46d9986996df40a6')
sha1sums=('18897a184332af2572c2e965da05db8ecd8a61c8'
          'e2537ebc971c4b095f3998463df9de0616ba656b')
sha256sums=('45703efaed9b4eb46830814ca5c5b19220021064a65ed225daa5b74a95c38044'
            '291e5c5fd8e7335e9ef8b241ae8ee0b3acd7936fc2fe83a632d12e66acd2380e')
sha512sums=('7f6e8fefd70b34a21c884920c6aa5b3e8d03b3e4c6c4fe86a449496307c460c7f96c9277983afdc36547725f68189dfcd0fa97556070b43b7d9d2b221e73ed6a'
            '18eb337308b32c96e23d70d760abdecc917baa627ff50dda9f166a7056eaed77d7b9bffcca907f9fc32157a6edbeef9370759f630f111b2d692071ba30c34b0c')
noextract=("jrosetta-engine-$pkgver.jar" "jrosetta-api-$pkgver.jar")

package() {
      cd "$srcdir"
      install -Dm644 "$srcdir/$pkgname-api-$pkgver.jar" "$pkgdir/usr/share/java/$pkgname/$pkgname-API.jar"
      install -Dm644 "$srcdir/$pkgname-engine-$pkgver.jar" "$pkgdir/usr/share/java/$pkgname/$pkgname-engine.jar"
}
