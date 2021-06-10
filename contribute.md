---
title: Contributing
subtitle: How to Contribute to PISM?
layout: page
hero_height: is-medium
hero_image: https://images.unsplash.com/photo-1542831371-29b0f74f9713
hero_darken: true
show_sidebar: true
---

# Contributing to PISM

There are many ways you can contribute to PISM:

* Fix typos, inaccuracies, and omissions in the manual.
+ Improve documentation of existing features.
* Provide additional examples.
* Add new tests for existing code.
* Report issues with the code or documentation.
* Fix bugs in PISM.
* Implement new features.

Please see [Contributing to PISM](https://pism.github.io/pism/contributing/index.html) in PISM's manual for some guidelines.

In summary: documentation and code contributions are preferred via pull requests to [https://github.com/pism/pism](https://github.com/pism/pism).

1. [Fork PISM's repository](https://help.github.com/en/articles/fork-a-repo).
1. Create a branch that will contain your changes.
1. Implement proposed changes.
    * Make changes to the code or documentation (or both).
    * Test your changes.
    * Add verification or regression tests (optional but **strongly encouraged**).
    * Update documentation, if necessary.
    * Update the change log ``CHANGES.rst``. If your contribution contains a bug fix, please describe the bug and its effects.

1. [Create a pull request](https://help.github.com/en/articles/creating-a-pull-request) and make sure to [allow edits from maintainers](https://help.github.com/en/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork)

If you are planning a large contribution we encourage you to open an issue at [https://github.com/pism/pism/issues](https://github.com/pism/pism/issues) or e-mail us at <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> and interact with us frequently to ensure that your effort is well-directed.

{% include notification.html message="**Note:** By submitting code, the contributor gives irretrievable consent to the redistribution and modification of the contributed source code as described in the PISM's open source license." %}
