# Sources for my spec files

These are my spec files of some apps that are not available for Fedora. The specs are used in [copr](https://copr.fedorainfracloud.org/coprs/fuhrmann) to build the packages.

### Useful links

* [RPKG quick start](https://docs.pagure.org/rpkg-util/quick_start.html#new-project)
* [Preparing software for packaging](https://rpm-packaging-guide.github.io/#preparing-software-for-packaging)
* [My COPR profile](https://copr.fedorainfracloud.org/coprs/fuhrmann)
* [Packaging: SourceURL](https://fedoraproject.org/wiki/Packaging:SourceURL)
* [Downloading sources at build](https://stackoverflow.com/questions/33177450/how-do-i-get-rpmbuild-to-download-all-of-the-sources-for-a-particular-spec)
* [Packaging problems and solutions](https://wiki.mageia.org/en/Packaging_problems_and_solutions)

### Available COPRs

These are the available COPRs and how to use them:

#### i3-gaps

To install the most recent version of [i3-gaps](https://github.com/Airblader/i3):
```
sudo dnf copr enable fuhrmann/i3-gaps
sudo dnf install i3-gaps
```

[fuhrmann/i3-gaps](https://copr.fedorainfracloud.org/coprs/fuhrmann/i3-gaps)

#### git-friendly

To install the most recent version of [git friendly](https://github.com/git-friendly/git-friendly)

```
sudo dnf copr enable fuhrmann/git-friendly
sudo dnf install git-friendly
```

[fuhrmann/git-friendly](https://copr.fedorainfracloud.org/coprs/fuhrmann/git-friendly)
