Name: ansible
Release: 3
Summary: SSH-based configuration management, deployment, and task execution system
Version: 1.6.10
Group: Development/Python
License: GPLv3
Source0: http://releases.ansible.com/ansible/%{name}-%{version}.tar.gz
Source1000: %{name}.rpmlintrc
Url: http://ansibleworks.com
BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python2-setuptools
Requires: python2-yaml
Requires: python2-paramiko
Requires: python2-jinja2
Requires: python2-keyczar

%description

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install -O1 --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/ansible/
cp examples/hosts $RPM_BUILD_ROOT/etc/ansible/
cp examples/ansible.cfg $RPM_BUILD_ROOT/etc/ansible/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/{man1,man3}/
cp -v docs/man/man1/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/ansible
cp -va library/* $RPM_BUILD_ROOT/%{_datadir}/ansible/
rm -f $RPM_BUILD_ROOT%{_datadir}/ansible/utilities/fireball $RPM_BUILD_ROOT%{_mandir}/man3/ansible.fireball*

%files
%defattr(-,root,root)
%{python2_sitelib}/ansible*
%{_bindir}/ansible*
%{_datadir}/ansible
%config(noreplace) %{_sysconfdir}/ansible
%doc README.md PKG-INFO COPYING
%doc %{_mandir}/man1/ansible*
%doc examples/playbooks
