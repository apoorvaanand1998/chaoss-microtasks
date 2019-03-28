> Based on the JSON documents produced by Graal and its source code, try to answer the following questions:

> Which are the common methods of the Graal backends?
> List and explain at least 2 Git commands used by Graal (and not implemented in Perceval).

1) The common methods are

- fetch(self, category, paths, from_date, to_date, branches, latest_items)
- metadata_category(item)
- _filter_commit(self, commit)
- _analyze(self, commit)
- _post(self, commit)
- analyze(self, file_path)

2) 2 git commands used by Graal that aren't used by Perceval are:

- git worktree - Manage multiple working trees attached to the same repository.
A git repository can support multiple working trees, allowing you to check out more than one branch at a time. With git worktree add a new working tree is associated with the repository. This new working tree is called a "linked working tree" as opposed to the "main working tree" prepared by "git init" or "git clone". A repository has one main working tree (if it's not a bare repository) and zero or more linked working trees. When you are done with a linked working tree, remove it with git worktree remove.

- git checkout - Updates files in the working tree to match the version in the index or the specified tree. If no paths are given, git checkout will also update HEAD to set the specified branch as the current branch.
