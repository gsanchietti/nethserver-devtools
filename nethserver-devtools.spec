Summary: NethServer tools for building RPMs
Name: nethserver-devtools
Version: 1.1.2
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: perl, perl(Test::Inline) >= 0.12, perl(XML::Parser)
Requires: python-docutils

%description
Use "genfilelist" to create a filelist file with correct ownerships and
permissions.

%prep
%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/sbin/e-smith
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}%{perl_vendorlib}/esmith/Build
mkdir -p ${RPM_BUILD_ROOT}/usr/share/nethserver-devtools

cp -a root/etc ${RPM_BUILD_ROOT}/
cp -a root/sbin ${RPM_BUILD_ROOT}/
cp -a esmith ${RPM_BUILD_ROOT}%{perl_vendorlib}/
cp -av root/usr/share/nethserver-devtools/ ${RPM_BUILD_ROOT}/usr/share/

%files
%defattr(-,root,root)
%attr(0755,root,root) /sbin/e-smith/genfilelist
%attr(0755,root,root) /sbin/e-smith/buildtests
%attr(0755,root,root) /sbin/e-smith/validate-lexicon
%attr(0755,root,root) /sbin/e-smith/generate-lexicons
%attr(0755,root,root) /sbin/e-smith/update-po
%attr(-,root,root) %dir /sbin/e-smith
%attr(0644,root,root) %{perl_vendorlib}/esmith/Build/CreateLinks.pm
%attr(0644,root,root) /etc/rpm/macros.nethserver-devtools
%attr(-,root,root) %dir /usr/share/nethserver-devtools
%attr(0644,root,root) /usr/share/nethserver-devtools/docs.mk
%attr(0644,root,root) /usr/share/nethserver-devtools/roles.rst
%doc COPYING


%changelog
* Mon Mar 24 2014 Davide Principi <davide.principi@nethesis.it> - 1.1.2-1.ns6
- Support Sphinx RST text roles - Enhancement #2700 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1.ns6
- RST format for help files - Enhancement #2627 [NethServer]

* Tue Oct 29 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1.ns6
- Implement Composer PSR-0 autoloader - Feature #2293 [Nethgui]

* Tue Mar 19 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- *.spec.in: fixed Release tag



