# SPDX-License-Identifier: 0BSD

from os import environ

from saxonche import PySaxonProcessor, __version__

expected_version = environ["SAXONCHE_EXPECTED_VERSION"]

if __version__ != expected_version:
    raise RuntimeError(f"Unexpected saxonche version: {__version__}")

with PySaxonProcessor(license=False) as processor:
    if processor.edition != "HE":
        raise RuntimeError(f"Unexpected Saxon edition: {processor.edition}")
    expected_processor_version = expected_version.rsplit(".", 1)[0]
    if expected_processor_version not in processor.version:
        raise RuntimeError(f"Unexpected processor version: {processor.version}")

    xpath = processor.new_xpath_processor()
    xpath_result = xpath.evaluate_single("1 + 1")
    if xpath_result is None or str(xpath_result) != "2":
        raise RuntimeError(f"Unexpected XPath result: {xpath_result}")

    document = processor.parse_xml(xml_text="<x>ok</x>")
    xslt = processor.new_xslt30_processor()
    executable = xslt.compile_stylesheet(
        stylesheet_text=(
            "<xsl:stylesheet version='3.0' "
            "xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>"
            "<xsl:template match='/'>"
            "<out><xsl:value-of select='/x'/></out>"
            "</xsl:template>"
            "</xsl:stylesheet>"
        )
    )
    result = executable.transform_to_string(xdm_node=document)
    if result is None or "<out>ok</out>" not in result:
        raise RuntimeError(f"Unexpected XSLT result: {result}")
