#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	RC6
Summary:	Crypt::RC6 Perl module - RC6 block cipher encryption
Summary(pl.UTF-8):	Moduł Perla Crypt::RC6 - szyfr blokowy RC6
Name:		perl-Crypt-RC6
Version:	1.0
Release:	25
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6cd523b2ebfea33c66fc5f4252e88ce7
Patch0:		%{name}-endian.patch
URL:		http://search.cpan.org/dist/Crypt-RC6/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::CBC compliant RC6 block cipher encryption module. RC6 is an
evolutionary improvement of RC5, designed to meet the requirements of
the Advanced Encryption Standard (AES). This implementation requires
the use of a 16-, 24-, or 32-byte key and 16-byte blocks for
encryption/decryption. Twenty rounds are performed.

%description -l pl.UTF-8
Moduł jest zgodną z Crypt::CBC implementacją szyfru blokowego RC6. RC6
jest ewolucyjnym rozszerzeniem RC5, opracowanym na potrzeby AES
(Advanced Security Standard - standardu zaawansowanego
bezpieczeństwa). Ta implementacja wymaga użycia 16, 24, lub
32-bajtowego klucza i 16-bajtowych bloków do kodowania i dekodowania.
Wykonywane jest dwadzieścia kroków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorarch}/Crypt/RC6.pm
%dir %{perl_vendorarch}/auto/Crypt/RC6
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/RC6/*.so
%{_mandir}/man3/*
