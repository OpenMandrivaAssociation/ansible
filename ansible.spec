Name: ansible
Release: 1
Summary: SSH-based configuration management, deployment, and task execution system
Version: 1.7.2
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
python setup.py build

%install
python setup.py install -O1 --root=%{buildroot}
mkdir -p %{buildroot}/etc/ansible/
cp examples/hosts %{buildroot}/etc/ansible/
cp examples/ansible.cfg %{buildroot}/etc/ansible/
mkdir -p %{buildroot}/%{_mandir}/{man1,man3}/
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_datadir}/ansible
cp -va library/* %{buildroot}/%{_datadir}/ansible/
rm %{buildroot}/%{_datadir}/ansible/utilities/fireball

%clean

%files
%{py_puresitedir}/ansible*
%{_bindir}/ansible*
%{_datadir}/ansible
#%exclude %{_datadir}/ansible/utilities/fireball
#%exclude %{_mandir}/man3/ansible.fireball.*
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


