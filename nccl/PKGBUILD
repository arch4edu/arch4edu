# Maintainer : Daniel Bermond < yahoo-com: danielbermond >
 
pkgname=nccl
pkgver=1.3.0.1
_srcver=1.3.0
pkgrel=1
_srcrel=1
_cudaver=8.0
pkgdesc="NVIDIA CUDA optimized primitives for collective multi-GPU communication"
arch=('x86_64')
url="https://github.com/NVIDIA/nccl.git"
license=('BSD')
depends=('cuda')
optdepends=("openmpi: To use 'ncclCommInitRank' in multi-process applications")
conflicts=('nccl-git')
source=("${pkgname}-${_srcver}-${_srcrel}.tar.gz"::"https://github.com/NVIDIA/nccl/archive/v${_srcver}-${_srcrel}.tar.gz")
sha256sums=('53f36151061907bdcafad1c26c1d9370a0a8400f561a83704a5138213ba51003')

build() {
    cd "${pkgname}-${_srcver}-${_srcrel}"
    make CUDA_HOME=/opt/cuda lib
}

package() {
    cd "${pkgname}-${_srcver}-${_srcrel}"
    make CUDA_HOME=/opt/cuda PREFIX=${pkgdir}/opt/cuda install
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
