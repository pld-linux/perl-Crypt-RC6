%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	RC6
Summary:	Crypt::RC6 Perl module - RC6 block cipher encryption
Summary(pl):	Modu³ Perla Crypt::RC6 - szyfr blokowy RC6
Name:		perl-Crypt-RC6
Version:	1.0
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::CBC compliant RC6 block cipher encryption module. RC6 is an
evolutionary improvement of RC5, designed to meet the requirements of
the Advanced Encryption Standard (AES). This implementation requires
the use of a 16-, 24-, or 32-byte key and 16-byte blocks for
encryption/decryption. Twenty rounds are performed.

%description -l pl
Modu³ jest zgodn± z Crypt::CBC implementacj± szyfru blokowego RC6. RC6
jest ewolucyjnym rozszerzeniem RC5, opracowanym na potrzeby AES
(Advanced Security Standard - standardu zaawansowanego
bezpieczeñstwa). Ta implementacja wymaga u¿ycia 16, 24, lub
32-bajtowego klucza i 16-bajtowych bloków do kodowania i dekodowania.
Wykonywane jest dwadzie¶cia kroków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_sitearch}/Crypt/RC6.pm
%dir %{perl_sitearch}/auto/Crypt/RC6
%{perl_sitearch}/auto/Crypt/RC6/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/RC6/*.so
%{_mandir}/man3/*
