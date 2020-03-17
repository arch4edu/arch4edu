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
pkgver=1.3.1
pkgrel=1
arch=(x86_64)
pkgdesc='High-level, high-performance, dynamic programming language (compiled with the Intel MKL library)'
url='https://julialang.org/'
license=(MIT)
depends=(fftw hicolor-icon-theme intel-mkl libgit2 libunwind libutf8proc suitesparse mbedtls openlibm)
makedepends=(cmake gcc-fortran gmp python)
optdepends=('gnuplot: If using the Gaston Package from julia')
provides=('julia')
conflicts=('julia' 'julia-git')
backup=(etc/julia/startup.jl)
source=("https://github.com/JuliaLang/julia/releases/download/v$pkgver/$_pkgname-$pkgver-full.tar.gz"
        libunwind-version.patch
        make-install-no-build.patch)
sha256sums=('053908ec2706eb76cfdc998c077de123ecb1c60c945b4b5057aa3be19147b723'
            'a5eec1e43e1161c313b1d32a5f35a67d6b4a2bbc2d6d324c010f6f2b35be4a72'
            '0b57e0bc6e25c92fde8a6474394f7a99bfb57f9b5d0f7b53f988622ae67de8b7')

prepare() {
  cd $_pkgname-$pkgver

  # Fixing libunwind version check
  # https://github.com/JuliaLang/julia/pull/29082
  #patch -p1 -i ../libunwind-version.patch

  # Don't build again in install
  patch -p1 -i ../make-install-no-build.patch

}

build() {
  export PATH="$srcdir/bin:$PATH"
  env CFLAGS="$CFLAGS -w" CXXFLAGS="$CXXFLAGS -w" make VERBOSE=1 -C $_pkgname-$pkgver \
    USE_SYSTEM_LLVM=0 \
    USE_SYSTEM_LIBUNWIND=1 \
    USE_SYSTEM_PCRE=1 \
    USE_INTEL_MKL=1 \
    USE_INTEL_LIBM=1 \
    USE_INTEL_JITEVENTS=1 \
    USE_SYSTEM_GMP=1 \
    USE_SYSTEM_MPFR=1 \
    USE_SYSTEM_SUITESPARSE=1 \
    USE_SYSTEM_DSFMT=0 \
    USE_SYSTEM_LIBUV=0 \
    USE_SYSTEM_UTF8PROC=1 \
    USE_SYSTEM_LIBGIT2=1 \
    USE_SYSTEM_LIBSSH2=1 \
    USE_SYSTEM_MBEDTLS=1 \
    USE_SYSTEM_CURL=1 \
    USE_SYSTEM_PATCHELF=1 \
    USE_SYSTEM_ZLIB=1 \
    USE_SYSTEM_P7ZIP=1 \
    USE_SYSTEM_OPENLIBM=1 \
    MARCH=x86-64
    #USE_SYSTEM_BLAS=1 \
    #USE_SYSTEM_LAPACK=1 \
    #USEICC=1 \
    #USEIFC=1
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

  make -C $_pkgname-$pkgver DESTDIR="$pkgdir" install \
    prefix=/usr \
    libexecdir=/usr/lib \
    sysconfdir=/etc

  # Documentation is in the julia-docs package.
  # Man pages in /usr/share/julia/doc/man are duplicate.
  rm -rf "$pkgdir/usr/share/"{doc,julia/doc}

  install -Dm644 $_pkgname-$pkgver/LICENSE.md \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
