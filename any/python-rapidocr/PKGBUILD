# Maintainer: aliu <AA RON LIU <GMAIL.COM> >
pkgname=python-rapidocr
pkgver=3.8.4
pkgrel=2
pkgdesc='Cross-runtime OCR library'
arch=('any')
license=('Apache-2.0')
depends=('python>=3.8'
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
	# Operation requires at least one of these and adjusted engine_type config
	'python-onnxruntime: Recommended runtime'
	'python-onnxruntime-cpu: Faster than GPU-accelerated onnxruntime (https://github.com/microsoft/onnxruntime/issues/13198)'
	'python-openvino: Supported runtime'
	'python-paddlepaddle: Supported runtime'
	'python-pytorch: Supported runtime'
)
makedepends=('python-build' 'python-installer' 'python-setuptools')
url='https://github.com/RapidAI/RapidOCR'
source=("https://github.com/RapidAI/RapidOCR/archive/v${pkgver}.tar.gz"
	# models bundled in PyPI wheel, from default_models.yaml
	'https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.8.0/onnx/PP-OCRv4/det/ch_PP-OCRv4_det_mobile.onnx'
	'https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.8.0/onnx/PP-OCRv4/cls/ch_ppocr_mobile_v2.0_cls_mobile.onnx'
	'https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.8.0/onnx/PP-OCRv4/rec/ch_PP-OCRv4_rec_mobile.onnx'
	# patch-in version number
	'pyproject.toml.patch')
b2sums=('56e313f692823a1bd8b799bb3cb9d48980cd215dc0e23d1dba4e960e2c3c67282c994981a0383cae2b8c5344d1db74aa2a1a457e2122d42717c32c45e015af48'
        '67566aa137427a05919373bfee74ee69735d9b5d888f7f8b8fd9bf10e9e75e3b129e91a1ea74d1b8b2eb8b0be81576101d081c16530296385fd3c1bed107282a'
        'f0c251313ce88e8ce74ebc995e3d7488541727ac9d242db4089bef7c131b0a8d59e7a322b592f5f07e5702e8d58e232510103f18438b5cb8cbfbb285cd3290a6'
        '9efd96d3174c3ee940ce3e5f99932ec7571ceb5a180ecdde512db09244958daf70d3909de437a6670cb873abd17254ae4a362a9ceccbb8b8d50874f5bd3b4080'
        '81484510a756aa733985e8ba0f9198011487786b45fa67fb1a65799f3bd0fd6d2c2b66453c6af6c9b8496fe07432d60941766b2901c729b82d9f24e6d3083773')

prepare() {
	cd "${srcdir}/RapidOCR-${pkgver}/python"

	# Patch in version number without needing to install a nonce dependency
	# that fetches the version number from git
	patch < "${srcdir}/pyproject.toml.patch"
	sed -i "s/VERSION_NUM/\"${pkgver}\"/" pyproject.toml

	rm rapidocr/models/.gitkeep  # i don't like you
	# From prepare_wheel_assets.py, run by gen_whl_to_pypi_rapidocr GH Action
	mv "${srcdir}/"*.onnx -t rapidocr/models/
	cat <<- EOF > MANIFEST.in
	include rapidocr/models/ch_PP-OCRv4_det_mobile.onnx
	include rapidocr/models/ch_ppocr_mobile_v2.0_cls_mobile.onnx
	include rapidocr/models/ch_PP-OCRv4_rec_mobile.onnx
	EOF
}

build() {
	cd "${srcdir}/RapidOCR-${pkgver}/python"
	python -m build --wheel --no-isolation
}

check() {
	cd "${srcdir}/RapidOCR-${pkgver}/python/build/lib"
	if [[ -f /etc/rapidocr/config.yaml ]]; then
		mv {rapidocr,"${srcdir}"}/config.yaml
		cp /etc/rapidocr/config.yaml rapidocr/config.yaml
	fi
	PYTHONPATH="$PWD" python -m rapidocr.main check
}

package() {
	cd "${srcdir}/RapidOCR-${pkgver}/python"
	python -m installer --destdir="${pkgdir}" dist/*.whl
	# move config file to /etc
	mkdir -p "${pkgdir}/etc/rapidocr/"
	if [[ -f "${srcdir}/config.yaml" ]]; then  # created backup during check()
		mv {"${srcdir}","${pkgdir}"}/etc/rapidocr}/config.yaml
		rm "${pkgdir}"/usr/lib/python*/site-packages/rapidocr/config.yaml
	else
		mv "${pkgdir}"/usr/lib/python*/site-packages/rapidocr/config.yaml "${pkgdir}"/etc/rapidocr/config.yaml
	fi
	set -x
	ln -s /etc/rapidocr/config.yaml "$(ls -d "${pkgdir}"/usr/lib/python*/site-packages/rapidocr)/config.yaml"
}
