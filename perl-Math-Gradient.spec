#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Gradient
Summary:	Math::Gradient - calculating gradients for colour transitions etc.
Summary(pl):	Math::Gradient - obliczanie gradient�w do przej�� kolor�w itp.
Name:		perl-Math-Gradient
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	4324edf09a8f684153ac0079f8507a0b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Gradient is used to calculate smooth transitions between
numerical values (also known as a "Gradient"). This module was written
mainly to mix colours, but it probably has several other applications.
Methods are supported to handle both basic and multiple-point
gradients, both with scalars and arrays.

%description -l pl
Math::Gradient s�u�y do obliczania p�ynnych przej�� mi�dzy warto�ciami
liczbowymi (znanych te� jako "gradienty"). Modu� zosta� napisany
g��wnie do mieszania kolor�w, ale prawdopodobnie ma par� innych
zastosowa�. Zawiera metody do obs�ugi prostych i wielopunktowych
gradient�w, zar�wno na skalarach, jak i tablicach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Gradient.pm
%{_mandir}/man3/*
