Name:           perl-XML-Parser
Version:        2.36
Release:        3
Summary:        A low level Perl module for parsing XML either via trees or streaming
Group:          Development/Libraries
License:        GPL+ or Artistic
Url:            http://search.cpan.org/dist/XML-Parser/
Source0:        %{name}-%{version}.tar.bz2
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  expat-devel

%description
This module provides ways to parse XML documents. It is built on top
of XML::Parser::Expat, which is a lower level interface to James
Clark's expat library. Each call to one of the parsing methods creates
a new instance of XML::Parser::Expat which is then used to parse the
document. Expat options may be provided when the XML::Parser object is
created. These options are then passed on to the Expat object on each
parse call. They can also be given as extra arguments to the parse
methods, in which case they override options given at XML::Parser
creation time.


%prep
%setup
chmod 644 samples/{canonical,xml*}
%{__perl} -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' samples/{canonical,xml*}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{perl_vendorarch}/XML/*
%{perl_vendorarch}/auto/XML/*
%doc %{_mandir}/man3/*.3*
