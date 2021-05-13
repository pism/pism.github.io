##### Committing to PISM development {#committing_to_pism_development}

`  - Create an account on `[`http://github.com`](http://github.com)`.`\
`  - `[`Set`` ``up`` ``Git`](http://help.github.com/set-up-git-redirect)` on your own system, if it is not already present.`\
`  - Send an e-mail to `[`uaf-pism@alaska.edu`](uaf-pism@alaska.edu)` asking to be added to the "team" of PISM developers.  We will make you a member of organization `[`https://github.com/pism`](https://github.com/pism)`.`\
`  - Being a project member allows you to `[`post`` ``"issues"`` ``at`` ``the`` ``github`` ``host`](https://github.com/pism/pism/issues?milestone=&sort=created&direction=desc&labels=&state=open)`, which may be labeled as "bugs", "tasks", "feature requests", etc.`\
`  - Clone the PISM source code repository using Git, with a URL that includes write permission, and select the dev branch to work on: git clone -b dev git@github.com:pism/pism.git pism-dev`

\<WRAP center round important 60%\> Please commit all changes to the
*dev* branch or \"topical\" branches. The *stable* branches, including
the current default branch, are managed by PISM developers at UAF.
Please feel free to fork the stable branches, however, especially if
your workflow is helped by having a non-changing base code.
`</WRAP>`{=html}

To change the URL of the PISM repository in an existing clone, see *man
git-remote* and look for the *set-url* command. This might be necessary
if you cloned using a read-only URL.

##### Best practices {#best_practices}

To satisfy our NASA-funded responsibility at UAF, we need to retain some
little bit of control. We need PISM to do what we are funded to do. The
following list of \"best practices\" facilitates such minimal control
while encouraging healthy development. Perfection on these \"rules\" is
not expected at any time. Mistakes are //always// forgiven. We are
well-protected by version control.

`  - Non-UAF developers should commit on the `*`dev`*` branch and not on `*`stable`*` branches, because UAF manages stable releases.  We do the merge of `*`dev`*` into the next `*`stableX.Y`*` release.  If you find a bug in the stable release then `[`please`` ``report`` ``it`](reporting_bugs)` and we will fix it at UAF.  Even better, send a pull request if you have fixed it in a fork, or send a patch to `[`uaf-pism@alaska.edu`](uaf-pism@alaska.edu)`.  If a bug exists in `*`dev`*` and you can safely fix it directly, then that is much appreciated.`\
`  - The software tests present in the dev branch are somewhat-thorough regression tests.  (They are better than nothing!)  Please run them before a commit to minimally check that you have not broken something: ``<code>`{=html}\
`    cd 'your build directory'`\
`    make`\
`    make test``</code>`{=html}` Proposing and building additional fast-running software tests for the dev branch is //strongly// encouraged.`\
`  - Posting a task (= an `[`issue`` ``with`` ``a`` `*`task`*` ``label`](https://github.com/pism/pism/issues?labels=task&sort=created&direction=desc&state=open&page=1)`) describing what you plan to do is always reasonable before doing it.  You can assign the task to yourself.  Creating a `*`git`` ``branch`*` with a name like `*`issue-XX`*` or `*`new-XX-model`*` is a good idea if you need to test before committing.  If you are hoping a UAF developer will do something to help you then you might mark it as a `[*`feature`` ``request`*](https://github.com/pism/pism/issues?direction=desc&labels=feature_request&milestone=&page=1&sort=created&state=open)` instead of a `*`task`*`.`\
`  - Posting bug reports is always worthwhile!  You can email to `[`uaf-pism@alaska.edu`](uaf-pism@alaska.edu)`, but even better is to post a bug report at the github site (i.e. an `[`issue`` ``with`` ``a`` `*`bug`*` ``label`](https://github.com/pism/pism/issues?labels=bug&sort=created&direction=desc&state=open&page=1)`).  See `[`How`` ``to`` ``report`` ``a`` ``bug`](reporting_bugs)`.`\
`  - Please post a bug report even if you already know how to fix it.  That way other developers may see that related matters are affected.`\
`  - When in doubt about adding spaghetti code because of existing/bad PISM design choices, please consider posting a task asking UAF developers for abstraction or modularization.   You might be asking us to do something we want to do anyway, but it raises the priority.`\
`  - Please use a text editor aware of code indentation.  Uses spaces, and not the "tab" character, to indent code.`

##### Git workflow {#git_workflow}

The PISM team is currently using a simplified \"merge\" workflow and not
a [\"pull request\"
workflow](http://scottchacon.com/2011/08/31/github-flow.html).

If you are just starting with Git, it may not be obvious how to use it
to make changes and merge them into the *dev* branch at
*github.com/pism/pism*. See [the Git documentation
page](http://git-scm.com/documentation).

A reasonable principle is this: try to *git pull* only into a clean
history. If not, you may find you are generating confusing modifications
to the history seen by everyone.

Here is one suggested workflow if your first act was (already) to go
change some source files in your working copy of *dev* branch:

`YOU CHANGED FILES foo.cc bar.sh` `git stash` `git pull` `git stash pop`
`RESOLVE ANY CONFLICTS` `git add foo.cc bar.sh`
`git commit -m "why I changed stuff and how it makes it better"`
`git push`

Note that *git pull* could be replaced by the two steps *git fetch* and
*git merge origin*.

An alternative work flow with the same basic affect as the above is

`YOU CHANGED FILES foo.cc bar.sh` `git add foo.cc bar.sh`
`git commit -m "why I changed stuff and how it makes it better"`
`git status # CHECK FOR OTHER UNCOMMITTED CHANGES (add, commit THEM IF PRESENT)`
`git pull --rebase`
`RESOLVE ANY CONFLICTS AND git add AND git commit FOR FILES WITH FIXED CONFLICTS`
`git push`

Finally, a suggested alternative is to create a new \'topic\' branch for
your changes. Merge the changes in *dev* more-or-less frequently in to
your new branch, and eventually merge your changes back into *dev* once
you are done and the new \'topic\' branch code has been tested.
