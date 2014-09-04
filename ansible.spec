Name: ansible
Release: %mkrel 1
Summary: SSH-based configuration management, deployment, and task execution system
Version: 1.6.10
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Group: Development/Python
License: GPLv3
Source0: http://releases.ansible.com/ansible/%{name}-%{version}.tar.gz
Url: http://ansibleworks.com
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: PyYAML
Requires: python-paramiko
Requires: python-jinja2
Requires: python-keyczar

%description

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

#%package fireball
#Summary: Ansible fireball transport support
#Group: Development/Libraries
#Requires: %{name} = %{version}-%{release}
#Requires: python-keyczar
#Requires: python-zmq
#
#%description fireball
#
#Ansible can optionally use a 0MQ based transport mechanism, which is
#considerably faster than the standard ssh mechanism when there are
#multiple actions, but requires additional supporting packages.
#
#%package node-fireball
#Summary: Ansible fireball transport - node end support
#Group: Development/Libraries
#Requires: python-keyczar
#Requires: python-zmq
#
#%description node-fireball
#
#Ansible can optionally use a 0MQ based transport mechanism, which has
#additional requirements for nodes to use.  This package includes those
#requirements.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/ansible/
cp examples/hosts $RPM_BUILD_ROOT/etc/ansible/
cp examples/ansible.cfg $RPM_BUILD_ROOT/etc/ansible/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/{man1,man3}/
cp -v docs/man/man1/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/ansible
cp -va library/* $RPM_BUILD_ROOT/%{_datadir}/ansible/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/ansible*
%{_bindir}/ansible*
%{_datadir}/ansible
%exclude %{_datadir}/ansible/utilities/fireball
%exclude %{_mandir}/man3/ansible.fireball.*
%config(noreplace) %{_sysconfdir}/ansible
%doc README.md PKG-INFO COPYING
%doc %{_mandir}/man1/ansible*
%doc examples/playbooks

#%files fireball
#%{_datadir}/ansible/utilities/fireball
#%doc %{_mandir}/man3/ansible.fireball.*
#
#%files node-fireball
#%doc README.md PKG-INFO COPYING


%changelog
* Sun Aug 10 2014 bcornec <bcornec> 1.6.10-1.mga4
+ Revision: 661320
- Fix #13649 Cf: https://bugs.mageia.org/show_bug.cgi?id=13649
- python-setuptools is a BuildRequire of course !
- Ansible now needs python-setuptools to build
- Fix https://bugs.mageia.org/show_bug.cgi?id=13649 by updating to upstream 1.6.8

  + luigiwalser <luigiwalser>
    - add upstream security fixes for safe_eval and apt_repository (mga#13278)

* Wed Jan 22 2014 bcornec <bcornec> 1.4.3-1.mga4
+ Revision: 567445
- Update to upstream 1.4.3

* Tue Dec 03 2013 bcornec <bcornec> 1.4.1-1.mga4
+ Revision: 554733
- Update to upstream 1.4.1

* Sat Nov 23 2013 bcornec <bcornec> 1.4-1.mga4
+ Revision: 552390
- Update to upstream ansible 1.4

* Mon Nov 11 2013 philippem <philippem> 1.3.4-4.mga4
+ Revision: 550500
- Add Requires python-keyczar on main package for accelerated mode

* Sun Nov 03 2013 bcornec <bcornec> 1.3.4-3.mga4
+ Revision: 549294
- Update to upstream 1.3.4

* Tue Oct 22 2013 umeabot <umeabot> 1.3.2-3.mga4
+ Revision: 542481
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 pterjan <pterjan> 1.3.2-2.mga4
+ Revision: 497632
- Rebuild to add different pythonegg provides for python 2 and 3

* Tue Oct 08 2013 bcornec <bcornec> 1.3.2-1.mga4
+ Revision: 493040
- Update ansible to 1.3.2 upstream

* Mon Sep 09 2013 bcornec <bcornec> 1.2.3-2.mga4
+ Revision: 476539
- Push reltag to 2 for ansible as previous patches consequence
- Do not generate the 0mq packages for now as zeromq is not in Mageia yet and SSH can be used
- Update Group in SPEC file for ansible
- Update sha for ansible
- Import from Fedora the ansible package
- Created package structure for ansible.

