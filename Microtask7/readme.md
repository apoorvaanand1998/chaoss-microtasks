> Based on the JSON documents produced by Graal and its source code, try to answer the following questions:

> Which are the common methods of the Graal backends?
> List and explain at least 2 Git commands used by Graal (and not implemented in Perceval).

1) The common methods are

- `fetch(self, category, paths, from_date, to_date, branches, latest_items)` - The method retrieves from a Git repository a list of
commits. Commits are returned in the same order they were obtained. The parameter latest_items returns only those commits which are new since the last time this method was called. It returns a generator of commits.
- `metadata_category(item)` - Extracts and returns the category of Graal item. For example, for Cocom it is 'code complexity' and for Colic it is 'code_license_nomos' or 'code_license_scancode'
- `_filter_commit(self, commit)` - Filter a commit according to its data (e.g., author, sha, etc.), takes perceval commit item and returns a bool.
- `_analyze(self, commit)` - Analyzes a commit and corresponding checkout version. Takes a perceval commit item and stores the analysis info (depending on the backend) in a list, and returns that list.
- `_post(self, commit)` - Removes attributes of the graal item obtained. Returns a commit.
- `analyze(self, file_path)` - Analyze the content of a file. Depending on the backend, CLOC and Lizard is used (for Cocom) and Nomos (for Colic) is used. Returns a dict with all the info of analysis.

2) Two git commands used by Graal that aren't used by Perceval are:

- git worktree - Manage multiple working trees attached to the same repository.
A git repository can support multiple working trees, allowing you to check out more than one branch at a time. With git worktree add a new working tree is associated with the repository. This new working tree is called a "linked working tree" as opposed to the "main working tree" prepared by "git init" or "git clone". A repository has one main working tree (if it's not a bare repository) and zero or more linked working trees. When you are done with a linked working tree, remove it with git worktree remove.

- git checkout - Updates files in the working tree to match the version in the index or the specified tree. If no paths are given, git checkout will also update HEAD to set the specified branch as the current branch.

The worktree is necessary as we used the --bare option during cloning which means there's no worktree to work with, for example with checkout. So for this, we add a worktree where we can do our work for the analysis depending on the backend. After everything is done, the worktree is pruned.
