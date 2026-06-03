# Maintainer: aliu <AA RON LIU <GMAIL.COM> >
pkgname=python-rapidocr
pkgver=3.8.1
pkgrel=1
pkgdesc='Cross-runtime OCR library'
arch=('any')
license=('Apache-2.0')
depends=('python>=3.6'
	'python-pyclipper>=1.2.0'
	'python-opencv>=4.5.1.48'
	'python-numpy>=1.19.5' 'python-numpy<3.0.0'
	'python-six>=1.15.0'
	'python-shapely>=1.7.1' #'python-shapely!=2.0.4'
	'python-yaml'
	'python-pillow'
	'python-tqdm'
	'python-omegaconf'
	'python-requests'
	'python-colorlog')
optdepends=(
	'python-onnxruntime: Recommended runtime'
	'python-onnxruntime-cpu: Faster than GPU-accelerated onnxruntime (https://github.com/microsoft/onnxruntime/issues/13198)'
	'python-openvino: Supported runtime'
	'python-paddlepaddle: Supported runtime'
	'python-pytorch: Supported runtime'
)
makedepends=('python-build' 'python-installer' 'python-setuptools')
url='https://github.com/RapidAI/RapidOCR'
source=("https://github.com/RapidAI/RapidOCR/archive/v${pkgver}.tar.gz"
	'https://github.com/RapidAI/RapidOCR/releases/download/v1.1.0/required_for_whl_v3.0.0.zip'
	"https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.8.0/resources/fonts/FZYTK.TTF"  # needed for check
	'setup.py.patch')
sha256sums=('9b0118260bc8ca665ec5c9d4769729c9642ef44e61b8ce2f50fb925ff02438d7'
            'e050aa8cf29cdbea04550204336859069dcbf7bb86761112d2008ae93db13296'
            '4065a23df6823c8e2b69a0e76d02f02a6470b8774a5e91086609701ad95cc33f'
            'ebfa9ac2f957378702f1ec6d07e8ca7b2a3f1c66e8194fc63bc8a35dfcebb5ca')

prepare() {
	cd "${srcdir}/RapidOCR-${pkgver}/python"

	# Patch in version number without needing to install a nonce dependency
	# that fetches the version number from PyPI (what)
	patch < "$srcdir/setup.py.patch"
	sed -i "s/version=VERSION_NUM/version=\"${pkgver}\"/" setup.py

	# From gen_whl_to_pypi_rapidocr GH Action
	rm -r rapidocr/models/
	mv "$srcdir/required_for_whl_v3.0.0/resources/models" -T rapidocr/models/
	mkdir rapidocr_t; mv rapidocr{,_t/}; mv -T rapidocr{_t,}  # nest rapidocr within rapidocr
	cd rapidocr
    echo "from .rapidocr.main import RapidOCR, VisRes" > __init__.py

	if [[ -e rapidocr/rapidocr ]]; then
		rm -r rapidocr/rapidocr/  # no idea why\ {this happens,only under makepkg}
	fi
}

build() {
	cd "${srcdir}/RapidOCR-${pkgver}/python"
	python setup.py build

	if [[ -e build/lib/rapidocr/rapidocr ]]; then
		rm -r build/lib/rapidocr/rapidocr/  # no idea why\ {this happens,only under makepkg}
	fi
    install "$srcdir/FZYTK.TTF" build/lib/rapidocr/models/
}

check() {
	cd "${srcdir}/RapidOCR-${pkgver}/python/build/lib"
	PYTHONPATH="$PWD" python -m rapidocr.main check
}

package() {
	cd "${srcdir}/RapidOCR-${pkgver}/python"
	python setup.py install --root="${pkgdir}" --optimize=1
}
