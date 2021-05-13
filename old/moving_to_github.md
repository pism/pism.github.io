#### Using Git to contribute to PISM {#using_git_to_contribute_to_pism}

Here are the steps you need to make

 * Install Git\
   * *apt-get install git* on Ubuntu 11.04 (package name is *git-core* in earlier)\
   * *port install git-core* on Mac OS X with MacPorts\
 * Install a GUI for git (for example *gitg*, *git-cola* or *tig* on Linux, 

 * Get an account on [github.com](http://github.com)\
 * Add an SSH public key at
   [https://github.com/account/ssh](https://github.com/account/ssh)\
 * Send us an e-mail asking to become a "collaborator"
   [uaf-pism@alaska.edu](uaf-pism@alaska.edu)\
 * Clone the PISM repository by running

   git clone git@github.com:pism/pism.git pism-dev

#### Editing code and committing changes {#editing_code_and_committing_changes}

The work-flow when using Subversion usually looks like

    # edit some code in existing files, add foo.cc
    svn add foo.cc
    svn commit -m "Fixed a bug and added foo.cc."

When using git, you

    # edit some code in existing files, add foo.cc
    git add foo.cc
    git commit -a -m "Fixed a bug and added foo.cc."
    git push
