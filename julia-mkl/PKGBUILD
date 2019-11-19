# Maintainter: Jingbei Li <i@Jingbei.li>
# Contributor: Alexander F. Rødseth <xyproto@archlinux.org>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Lex Black <autumn-wind@web.de>
# Contributor: Michael Jakl <jakl.michael@gmail.com>
# Contributor: devmotion <nospam-archlinux.org@devmotion.de>
# Contributor: Valentin Churavy <v.churavy@gmail.com>

pkgname=julia-mkl
_pkgname=julia
epoch=2
pkgver=1.2.0
pkgrel=1
arch=(x86_64)
pkgdesc='High-level, high-performance, dynamic programming language (compiled with the Intel MKL library)'
url='https://julialang.org/'
license=(MIT)
depends=(fftw hicolor-icon-theme intel-mkl libgit2 libunwind libutf8proc suitesparse)
makedepends=(cmake gcc-fortran gmp python2)
optdepends=('gnuplot: If using the Gaston Package from julia')
provides=('julia')
conflicts=('julia' 'julia-git')
backup=(etc/julia/startup.jl)
source=("https://github.com/JuliaLang/julia/releases/download/v$pkgver/$_pkgname-$pkgver-full.tar.gz"
        libunwind-version.patch
        Make.user)
sha256sums=('2419b268fc5c3666dd9aeb554815fe7cf9e0e7265bc9b94a43957c31a68d9184'
            'a5eec1e43e1161c313b1d32a5f35a67d6b4a2bbc2d6d324c010f6f2b35be4a72'
            '1c7a83bd66504514dbb9a0bf0177d0994bd21cddb877799bd20bcb5113894e8b')

prepare() {
  cd $_pkgname-$pkgver

  # Add and use option to build with system cblas
  #patch -p1 --no-backup-if-mismatch -i ../cblas.patch

  # Fixing libunwind version check
  # https://github.com/JuliaLang/julia/pull/29082
  #patch -p1 -i ../libunwind-version.patch

  # Configuring the build
  cp -f ../Make.user Make.user

  # Prepare a symlink from "python" to "python2"
  mkdir -p "$srcdir/bin"
  ln -s /usr/bin/python2 "$srcdir/bin/python"

  #cd deps/srccache
  #xzcat llvm-6.0.1.src.tar.xz | tar xf -
  #sed 's/ detail::join_impl/ llvm::detail::join_impl/g' -i $(grep ' detail::join_impl' llvm-6.0.1.src -rl)
  #tar cf - llvm-6.0.1.src | xz -T0 -c > llvm-6.0.1.src.tar.xz
  #md5sum llvm-6.0.1.src.tar.xz | cut -d' ' -f1 > ../checksums/llvm-6.0.1.src.tar.xz/md5
  #sha512sum llvm-6.0.1.src.tar.xz | cut -d' ' -f1 > ../checksums/llvm-6.0.1.src.tar.xz/sha512
}

build() {
  export PATH="$srcdir/bin:$PATH"
  env CFLAGS="$CFLAGS -w" CXXFLAGS="$CXXFLAGS -w" make -C $_pkgname-$pkgver
}

#check() {
# cd $_pkgname-$pkgver/test
#
# # this is the make testall target, plus the --skip option from
# # travis/appveyor/circleci (one test fails with DNS resolution errors)
# ../julia --check-bounds=yes --startup-file=no ./runtests.jl all --skip Sockets --skip Distributed --skip LibGit2/libgit2
# find ../stdlib \( -name \*.cov -o -name \*.mem \) -delete
# rm -r depot/compiled
#}

package() {

  make -C $_pkgname-$pkgver DESTDIR="$pkgdir" install

  # Documentation is in the julia-docs package.
  # Man pages in /usr/share/julia/doc/man are duplicate.
  rm -rf "$pkgdir/usr/share/"{doc,julia/doc}

  install -Dm644 $_pkgname-$pkgver/LICENSE.md \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
