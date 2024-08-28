Name:		texlive-asmeconf
Version:	71956
Release:	1
Summary:	A LaTeX template for ASME conference papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asmeconf
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asmeconf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asmeconf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The asmeconf class provides a LaTeX template for ASME
conference papers, following ASME's guidelines for margins,
fonts, headings, captions, and reference formats as of 2022.
This LaTeX template is intended to be used with the
asmeconf.bst BibTeX style, for reference formatting, which is
part of this distribution. Unlike older ASME conference LaTeX
templates, asmeconf pdfs will contain hyperlinks, bookmarks,
and metadata; and the references can include the DOI and URL
fields. This LaTeX template enables inline author names,
following ASME's current style, but it can also produce the
traditional grid style. Options include line numbering, final
column balancing, various math options, government copyright,
archivability (PDF/A), and multilingual support. The code is
compatible with pdfLaTeX or LuaLaTeX. This LaTeX template is
not a publication of ASME, but it does conform to ASME's
currently published guidelines for conference papers.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/asmeconf
%{_texmfdistdir}/bibtex/bst/asmeconf
%doc %{_texmfdistdir}/doc/latex/asmeconf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
