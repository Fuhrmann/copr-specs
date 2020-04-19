## Sources for my spec files

### Some useful links

rpkg docs: https://docs.pagure.org/rpkg-util/quick_start.html#new-project

rpm docs: https://rpm-packaging-guide.github.io/#preparing-software-for-packaging

copr profile: https://copr.fedorainfracloud.org/coprs/fuhrmann/

packaging: https://fedoraproject.org/wiki/Packaging:SourceURL

downloading sources: https://stackoverflow.com/questions/33177450/how-do-i-get-rpmbuild-to-download-all-of-the-sources-for-a-particular-spec

packaging problems and solutions: https://wiki.mageia.org/en/Packaging_problems_and_solutions

### Using my copr

```
sudo dnf copr enable fuhrmann/i3-gaps
sudo dnf install i3-gaps
```

```
sudo dnf copr enable fuhrmann/git-friendly
sudo dnf install git-friendly
```
