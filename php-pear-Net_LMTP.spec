%define		status		stable
%define		pearname	Net_LMTP
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - an implementation of the RFC2033 LMTP protocol
Summary(pl.UTF-8):	%{pearname} - implementacja protokołu LMTP (RFC2033)
Name:		php-pear-%{pearname}
Version:	1.0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	1d09ef288ebd6d8e63a5f186ea801e15
URL:		http://pear.php.net/package/Net_LMTP/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-Net_Socket
Obsoletes:	php-pear-Net_LMTP-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an implementation of the RFC2033 LMTP using
PEAR's Net_Socket and Auth_SASL class.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten pakiet dostarcza implementację protokołu LMTP (opisanego w
RFC2033) za pomocą klas Net_Socket oraz Auth_SASL.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Net_LMTP/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/*.php
