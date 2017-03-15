# Release workflows for euth_wagtail

The versions numbers follow semantic versioning. The master branch contains
the development version of the project. For each release a new release branch
is created. Those will be named: `release<major>.<minor>`. Individual patch
levels should than be a tag named: `r<major>.<minor>.<patch>`.

Below are examples for releasing version 1.6

## Creating a release

```
git checkout master
git pull
git merge release1.5
git checkout -b release1.6

# fix bugs found on stage, and commit them

# do the release
git tag --annotate --sign r1.6.0  # add release notes to annotation

# ensure bugfixes are applied to master
git checkout master
git pull
git merge release1.6
```

## fixing production bugs

If a bug in a released version is discovered it should be fixed on the release
branch. To fix it also for future releases, the release branch should than be
merged into the master branch.

```
# fix bugs found on production

# create a patch release
git tag r1.6.1

# ensure bugfixes are applied to master
git checkout master
git pull
git merge release1.6
```
