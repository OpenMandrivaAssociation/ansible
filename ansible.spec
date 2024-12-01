Name: ansible
Summary: SSH-based configuration management, deployment, and task execution system
Version: 11.0.0
Release: 1
Group: Development/Python
License: GPLv3
Source0: https://files.pythonhosted.org/packages/source/a/ansible/ansible-%{version}.tar.gz
Source1000: %{name}.rpmlintrc
Url: https://ansibleworks.com
BuildArch: noarch
BuildSystem: python

%description

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%prep
%autosetup -p1

%install -a
ln -s ansible-community %{buildroot}%{_bindir}/ansible

%files
%defattr(-,root,root)
%{python3_sitelib}/ansible*
%{_bindir}/ansible*
