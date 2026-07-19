# Maintainer: @RubenKelevra <cyrond@gmail.com>

pkgname='python-docling'
_foldername=${pkgname#python-}
pkgver='2.82.0'
pkgrel=1
pkgdesc='SDK and CLI for parsing PDF, DOCX, HTML, and more into a unified document representation'
url='https://github.com/docling-project/docling'
depends=('python>=3.10'
         'python-beautifulsoup4'
         'python-certifi'
         'python-defusedxml'
         'python-docling-core>=2.70.0'
         'python-docling-ibm-models>=3.12.0'
         'python-docling-parse>=5.3.2'
         'python-filetype'
         'python-lxml'
         'python-marko'
         'python-openpyxl'
         'python-pluggy'
         'python-polyfactory'
         'python-pydantic-settings'
         'python-pypdfium2'
         'python-pylatexenc'
         'python-docx'
         'python-pptx'
         'python-rapidocr'
         'python-requests'
         'python-scipy'
         # 'python-accelerate' # already required by python-docling-ibm-models
         # 'python-huggingface-hub' # already required by python-docling-ibm-models
         # 'python-pandas' # already required by python-docling-core
         # 'python-pillow' # already required by python-docling-core/python-docling-ibm-models
         # 'python-pydantic' # already required by python-docling-core/python-docling-ibm-models
         # 'python-rtree' # already required by python-docling-ibm-models
         # 'python-pytorch' # already required by python-docling-ibm-models
         # 'python-torchvision' # already required by python-docling-ibm-models
         # 'python-tqdm' # already required by python-docling-ibm-models
         # 'python-typer' # already required by python-docling-core
)
optdepends=('python-easyocr: enable EasyOCR OCR engine'
            'python-tesserocr: enable Tesseract OCR engine'
            'python-playwright: enable HTML rendering for dynamic pages (htmlrender extra)'
            'python-transformers: enable VLM-based pipelines (vlm extra)'
            'python-onnxruntime-cpu: enable RapidOCR ONNX backend on CPU (rapidocr extra)'
            'python-onnxruntime-cuda: enable RapidOCR ONNX backend with CUDA (rapidocr extra)'
            'python-openai-whisper: enable ASR pipeline (asr extra)'
            'python-numba: improve ASR runtime performance (asr extra)'
)
# Upstream extras without a matching Arch/AUR package name at the moment:
# - qwen-vl-utils (vlm)
# - arelle-release (xbrl)
# - tritonclient[grpc] (remote-serving)
makedepends=('python-build'
             'python-installer'
             'python-setuptools'
             'python-wheel'
)
license=('MIT')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_foldername::1}/$_foldername/$_foldername-$pkgver.tar.gz")
b2sums=('b4d8a56d9fdad045c938ea9f9e49de905c1d28956ad277d73921cc191bce86a604aa099b54ec043d0daddd5045c77b5d109455e3d40deb387dac2736e0bbd28e')

build() {
	cd "${srcdir}/${_foldername}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_foldername}-${pkgver}"
	python -m installer --destdir="${pkgdir}" --compile-bytecode 2 dist/*.whl
	install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
