%define SHA256SUM0 3b083b55a7cda7782e370bf03412dbf51ca4a94c1d56325ff70a1545d7a30adc
%define debug_package %{nil}
%global gh_user bcicen

Name:           ctop
Version:        0.7.3
Release:        1%{?dist}
Summary:        Top-like interface for Docker container metrics
Group:          Applications/System
License:        MIT
URL:            https://ctop.sh
Source0:        https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
ctop provides a concise and condensed overview of real-time metrics for
multiple containers as well as an single container view for inspecting
a specific container.

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -
%autosetup -n %{name}-%{version}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
go env -w GO111MODULE=off
go get -u github.com/golang/dep/cmd/dep
GO111MODULE=on go install

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Apr 20 2020 Ricardo Fuhrmann <fuhrmanns+copr@gmail.com> - 0.7.3-1
- 0.7.3

