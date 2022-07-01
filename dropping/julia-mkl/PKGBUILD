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
pkgver=1.6.3
pkgrel=1
arch=(x86_64)
pkgdesc='High-level, high-performance, dynamic programming language (compiled with the Intel MKL library)'
url='https://julialang.org/'
license=(MIT)
depends=(fftw hicolor-icon-theme intel-mkl intel-oneapi-compiler-shared libgit2 libunwind libutf8proc suitesparse mbedtls pcre2 llvm-libs p7zip)
makedepends=(cmake gcc-fortran gmp python llvm patchelf)
optdepends=('gnuplot: If using the Gaston Package from julia')
provides=('julia')
conflicts=('julia' 'julia-git')
backup=(etc/julia/startup.jl)
source=("https://github.com/JuliaLang/julia/releases/download/v$pkgver/$_pkgname-$pkgver-full.tar.gz"
        julia-hardcoded-libs.patch
        make-install-no-build.patch)
sha256sums=('29aad934582fb4c6dd9f9dd558ad649921f43bc7320eab54407fdf6dd3270a33'
            '7497bff3cc6faac0a0664e620fd5525d7bb19d1bc3d2ff7f4d900dc36d476ceb'
            '8be4605f92a009072ca7e843549c225fc4e959893498e7c4f8f79e861e63714d')
options=(!buildflags !makeflags)

prepare() {
  cd $_pkgname-$pkgver

  # Don't hardcode library names
  patch -p1 -i ../julia-hardcoded-libs.patch
  # Don't build again in install
  patch -p1 -i ../make-install-no-build.patch
}

_buildopts="prefix=/usr \
    bindir=/usr/bin \
    sysconfdir=/etc \
    libexecdir=/usr/lib \
    USE_BINARYBUILDER=0 \
    USE_SYSTEM_CSL=1 \
    USE_SYSTEM_LLVM=1 \
    USE_SYSTEM_LIBUNWIND=1 \
    USE_SYSTEM_PCRE=1 \
    USE_INTEL_MKL=1 \
    USE_INTEL_LIBM=1 \
    USE_INTEL_JITEVENTS=1 \
    USE_PERF_JITEVENTS=0 \
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
    MARCH=x86-64"
    #USEICC=1 \
    #USEIFC=1 \

build() {
  cd $_pkgname-$pkgver
  make VERBOSE=1 JLDFLAGS=${LDFLAGS} $_buildopts
}

#check() {
#  cd $_pkgname-$pkgver/test
#
#  # this is the make testall target, plus the --skip option from
#  # travis/appveyor/circleci (one test fails with DNS resolution errors)
#  # Also skip tests that check for a hardcoded version number
#  ../julia --check-bounds=yes --startup-file=no ./runtests.jl all \
#    --skip Sockets \
#    --skip broadcast \
#    --skip Distributed \
#    --skip nghttp2_jll \
#    --skip GMP_jll \
#    --skip LibCURL \
#    --skip LibSSH2_jll \
#    --skip MbedTLS_jll \
#    --skip SuiteSparse_jll \
#    --skip PCRE2_jll \
#    --skip LibGit2_jll \
#    --skip MozillaCACerts_jll \
#    --skip NetworkOptions \
#    --skip OpenBLAS_jll \
#    --skip cmdlineargs
#  find ../stdlib \( -name \*.cov -o -name \*.mem \) -delete
#  rm -fr ../stdlib/Artifacts/test/artifacts
#}

package() {
  cd $_pkgname-$pkgver
  make DESTDIR="$pkgdir" install $_buildopts

  ln -s /opt/intel/oneapi/compiler/latest/linux/compiler/lib/intel64/libimf.so "$pkgdir"/usr/lib/julia

  rm "$pkgdir"/usr/lib/julia/libccalltest.so.debug # Remove debug testing library
  install -Dm644 LICENSE.md -t "$pkgdir"/usr/share/licenses/$pkgname
}
