---
title: Contributing
subtitle: How to contribute to PISM?
layout: page
hero_height: is-medium
hero_image: https://images.unsplash.com/photo-1590935216109-8d3318de2c1c
hero_caption: "Photo: <a href='https://unsplash.com/photos/4J2OD3njVgI'>M. Winkler / Unsplash</a>"
hero_darken: false
show_sidebar: true
---

# General

There are many ways you can contribute to PISM:

* Fix typos, inaccuracies, and omissions in the manual
* Improve documentation of existing features
* Provide additional examples
* Add new tests for existing code
* Report issues with the code or documentation
* Fix bugs in PISM
* Implement new features

Please see [Contributing to PISM](https://pism.github.io/docs/contributing/index.html) in PISM's manual for some guidelines.

## Contribution workflow

In summary: documentation and code contributions are preferred via **pull requests** to [https://github.com/pism/pism](https://github.com/pism/pism).

1. [Fork PISM's repository](https://help.github.com/en/articles/fork-a-repo)
1. Create a branch that will contain your changes
1. Implement proposed changes
    * Make changes to the code or documentation (or both)
    * Test your changes
    * Add verification or regression tests (optional but *strongly encouraged*)
    * Update documentation, if necessary
    * Update the change log ``CHANGES.rst``. If your contribution contains a bug fix, please describe the bug and its effects

1. [Create a pull request](https://help.github.com/en/articles/creating-a-pull-request) and make sure to [allow edits from maintainers](https://help.github.com/en/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork)

If you are planning a large contribution we encourage you to open an **issue** at [https://github.com/pism/pism/issues](https://github.com/pism/pism/issues) or e-mail us at <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> and interact with us frequently to ensure that your effort is well-directed.

{% include notification.html message="**Note:** By submitting code, the contributor gives irretrievable consent to the redistribution and modification of the contributed source code as described in the PISM's [open source license](https://github.com/pism/pism/blob/master/COPYING)." status="is-info is-light" %}

## Bug reporting

Please see the [issues](https://github.com/pism/pism/issues) to check if someone already found a similar bug. You can post an issue there, and label it as a bug, if it is new. Alternatively, send a report by e-mail to <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>.

Please include the following information in all bug-reports and questions about particular PISM's behavior:

- the PISM version (the output of ``pismr -version``)
- the *full* command necessary to reproduce the bug
- the input files used by the run reproducing the bug
- a description of what PISM does wrong

For more details, please see [Submitting bug reports](https://pism.github.io/docs/contributing/bug-reporting.html) in PISM's manual.
