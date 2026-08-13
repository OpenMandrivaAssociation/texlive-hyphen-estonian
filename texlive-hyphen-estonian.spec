%global tl_name hyphen-estonian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Estonian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-estonian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-estonian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Estonian in T1/EC and UTF-8 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-estonian:
estonian loadhyph-et.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-estonian:
\addlanguage{estonian}{loadhyph-et.tex}{}{2}{3}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-estonian:
['estonian'] = {
	loader = 'loadhyph-et.tex',
	lefthyphenmin = 2,
	righthyphenmin = 3,
	synonyms = {  },
	patterns = 'hyph-et.pat.txt',
},
TL_HYPHEN_EOF
