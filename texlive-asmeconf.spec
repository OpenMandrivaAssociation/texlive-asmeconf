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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/asmeconf
%dir %{_datadir}/texmf-dist/doc/latex/asmeconf
%dir %{_datadir}/texmf-dist/tex/latex/asmeconf
%dir %{_datadir}/texmf-dist/doc/latex/asmeconf/examples
%dir %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-wide-equation-example
%{_datadir}/texmf-dist/bibtex/bst/asmeconf/asmeconf.bst
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/README.md
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/asmeconf-sample.bib
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/asmeconf-style.css
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/asmeconf-template.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/asmeconf-template.tex
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/CONTRACTOR-copyright-asmeconf-template.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/GOVT-copyright-asmeconf-template.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-accessible-PDF-UA-2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-accessible-PDF-UA-2.tex
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-authorgrid-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-authorgrid-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-fontspec.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-fontspec.tex
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-lualatex-ode-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-lualatex-ode-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-wide-equation-example/asmeconf-template-widetext.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-wide-equation-example/asmeconf-template-widetext.tex
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-wide-equation-example/asmewide.sty
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-wide-equation-example/tesseral-harmonic.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/examples/asmeconf-wide-equation-example/zonal-harmonic2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/sample-figure-1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/sample-figure-2a.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmeconf/sample-figure-2b.pdf
%{_datadir}/texmf-dist/tex/latex/asmeconf/asmeconf.cls
