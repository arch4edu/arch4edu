pkgname='python-scikit-learn-intelex'
_module='scikit-learn-intelex'
_src_folder='scikit_learn_intelex-2025.7.0'
pkgver='2025.7.0'
pkgrel=1
pkgdesc="Intel(R) Extension for Scikit-learn is a seamless way to speed up your Scikit-learn application."
url="https://github.com/intel/scikit-learn-intelex"
depends=('python' 'python-scikit-learn' 'python-daal')
makedepends=('python-build' 'python-installer' 'python-wheel')
license=('custom:Apache Software License')
arch=('any')
source=("https://files.pythonhosted.org/packages/35/d0/2806f98921db15bc0f45f8837dfde15ec9b9a1e8e35d210c7de588ac7098/scikit_learn_intelex-2025.7.0-py313-none-manylinux_2_28_x86_64.whl")
sha256sums=('e41b283b0727b28ad4d67e5effa6f2d91d11513b116077f2f780fdcdcf86a00f')

package() {
    python -m installer --destdir="${pkgdir}" scikit_learn_intelex-2025.7.0-py313-none-manylinux_2_28_x86_64.whl
}

