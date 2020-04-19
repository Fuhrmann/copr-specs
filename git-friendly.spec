%define SHA256SUM0 eda37ce98ed81f14b0e500d5e7e132f04d93815ba90d63e856f464165bd60f1e
%define debug_package %{nil}


Name: git-friendly
Version: 1.0.2
Release: 1%{?dist}
Summary: Streamline your git workflow: just type pull, branch, merge, push
License: MIT
URL: https://github.com/%{name}/%{name}/archive/%{version}.tar.gz
Source0: https://github.com/%{name}/%{name}/archive/%{version}.tar.gz

Requires: git

%description
A collection of shell scripts for making pulling, pushing, branching, merging, and stashing with Git fast and painless.

Git sometimes requires typing two or three commands just to execute something basic like fetching new code. git-friendly adds a few new commands — pull, push, branch, merge and stash which:

- does the most useful thing by default; plus
- push copies a GitHub compare URL to your clipboard;
- pull runs commands like bundle install, npm install, yarn install, and composer install if necessary;
- branch tracks remote branches if they are available;
- stash includes untracked files by default.

Less time fighting Git — more time actually doing work.


%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -
%autosetup -n %{name}-%{version}

%build
/bin/true

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 branch %{buildroot}/usr/local/bin/branch
install -m 0755 merge %{buildroot}/usr/local/bin/merge
install -m 0755 pull %{buildroot}/usr/local/bin/pull
install -m 0755 push %{buildroot}/usr/local/bin/push
install -m 0755 stash %{buildroot}/usr/local/bin/stash

%files
/usr/local/bin/branch
/usr/local/bin/merge
/usr/local/bin/pull
/usr/local/bin/push
/usr/local/bin/stash

%changelog

