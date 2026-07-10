%global tl_name asmeconf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.46
Release:	%{tl_revision}.1
Summary:	A LaTeX template for ASME conference papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/asmeconf
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asmeconf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asmeconf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The asmeconf class provides a LaTeX template for ASME conference papers,
following ASME's guidelines for margins, fonts, headings, captions, and
reference formats as of 2025. This LaTeX template is intended to be used
with the asmeconf.bst BibTeX style, for reference formatting, which is
part of this distribution. Unlike older ASME conference LaTeX templates,
asmeconf pdfs will contain hyperlinks, bookmarks, and metadata; and the
references can include the DOI and URL fields. This LaTeX template
enables inline author names, following ASME's current style, but it can
also produce the traditional grid style. Options include line numbering,
final column balancing, various math options, government copyright,
archivability and accessibility (PDF/A), and multilingual support. The
code is compatible with pdfLaTeX or LuaLaTeX. This LaTeX template is not
a publication of ASME, but it does conform to ASME's currently published
guidelines for conference papers.

