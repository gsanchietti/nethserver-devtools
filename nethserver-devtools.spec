Summary: NethServer tools for building RPMs
Name: nethserver-devtools
Version: 1.1.4
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: perl
Requires: python-docutils

%description
Use "genfilelist" to create a filelist file with correct ownerships and
permissions.

%prep
%setup

%build

%install
rm -rf %{buildroot}
%{__install} -d \
    %{buildroot}/%{_bindir} \
    %{buildroot}/%{_datadir}/nethserver-devtools \
    %{buildroot}/%{_sysconfdir}/rpm/

%{__install} -vp src/bin/* %{buildroot}/%{_bindir}/
%{__install} -vp src/share/* %{buildroot}/%{_datadir}/nethserver-devtools/
%{__install} -vp src/rpm/* %{buildroot}/%{_sysconfdir}/rpm/
%{__install} -vpD src/perl/esmith/Build/CreateLinks.pm %{buildroot}/%{perl_vendorlib}/esmith/Build/CreateLinks.pm

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/genfilelist
%{perl_vendorlib}/esmith/Build/CreateLinks.pm
%{_sysconfdir}/rpm/macros.nethserver-devtools
%{_datadir}/nethserver-devtools/docs.mk
%{_datadir}/nethserver-devtools/roles.rst
%dir %{_datadir}/nethserver-devtools



%changelog
* Tue May 19 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.4-1
- Fix case where macro argument list is empty. Refs #2654 [NethServer]

* Tue May 19 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- Select rst2html output language - Enhancement #2654 [NethServer]

* Mon Mar 24 2014 Davide Principi <davide.principi@nethesis.it> - 1.1.2-1.ns6
- Support Sphinx RST text roles - Enhancement #2700 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1.ns6
- RST format for help files - Enhancement #2627 [NethServer]

* Tue Oct 29 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1.ns6
- Implement Composer PSR-0 autoloader - Feature #2293 [Nethgui]

* Tue Mar 19 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- *.spec.in: fixed Release tag



