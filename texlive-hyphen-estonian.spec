# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-estonian
Version:	20111103
Release:	2
Summary:	Estonian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-estonian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Estonian in T1/EC and UTF-8 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-estonian
%_texmf_language_def_d/hyphen-estonian
%_texmf_language_lua_d/hyphen-estonian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-estonian <<EOF
\%\% from hyphen-estonian:
estonian loadhyph-et.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-estonian <<EOF
\%\% from hyphen-estonian:
\addlanguage{estonian}{loadhyph-et.tex}{}{2}{3}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-estonian <<EOF
-- from hyphen-estonian:
	['estonian'] = {
		loader = 'loadhyph-et.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-et.pat.txt',
		hyphenation = '',
	},
EOF
