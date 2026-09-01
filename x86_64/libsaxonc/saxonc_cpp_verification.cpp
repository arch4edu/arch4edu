// SPDX-License-Identifier: 0BSD

#include <cstring>

#include "saxonc/SaxonProcessor.h"
#include "saxonc/XPathProcessor.h"
#include "saxonc/XQueryProcessor.h"
#include "saxonc/Xslt30Processor.h"
#include "saxonc/XsltExecutable.h"
#include "saxonc/XdmItem.h"
#include "saxonc/XdmNode.h"

static int exercise_saxonc(void) {
	SaxonProcessor processor(false);
	if (std::strcmp(processor.getSaxonEdition(), "HE") != 0) {
		return 1;
	}

	XdmNode *document = processor.parseXmlFromString("<x>ok</x>");
	if (document == nullptr) {
		return 2;
	}

	XPathProcessor *xpath = processor.newXPathProcessor();
	xpath->setContextItem(document);
	XdmItem *xpath_result = xpath->evaluateSingle("string(/x)");
	if (xpath_result == nullptr || std::strcmp(xpath_result->getStringValue(), "ok") != 0) {
		delete xpath_result;
		delete xpath;
		delete document;
		return 3;
	}
	delete xpath_result;
	delete xpath;

	XQueryProcessor *xquery = processor.newXQueryProcessor();
	xquery->setQueryContent("1 + 1");
	const char *query_result = xquery->runQueryToString();
	if (query_result == nullptr || std::strstr(query_result, "2") == nullptr) {
		operator delete((void *)query_result);
		delete xquery;
		delete document;
		return 4;
	}
	operator delete((void *)query_result);
	delete xquery;

	Xslt30Processor *xslt = processor.newXslt30Processor();
	XsltExecutable *executable = xslt->compileFromString(
		"<xsl:stylesheet version='3.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>"
		"<xsl:template match='/'><out><xsl:value-of select='/x'/></out></xsl:template>"
		"</xsl:stylesheet>");
	if (executable == nullptr) {
		delete xslt;
		delete document;
		return 5;
	}
	const char *transform_result = executable->transformToString(document);
	if (transform_result == nullptr || std::strstr(transform_result, "<out>ok</out>") == nullptr) {
		operator delete((void *)transform_result);
		delete executable;
		delete xslt;
		delete document;
		return 6;
	}
	operator delete((void *)transform_result);
	delete executable;
	delete xslt;
	delete document;

	SaxonProcessor licensed_requested(true);
	if (std::strcmp(licensed_requested.getSaxonEdition(), "HE") != 0) {
		return 7;
	}

	return 0;
}

int main(void) {
	const int result = exercise_saxonc();
	SaxonProcessor::release();
	return result;
}
