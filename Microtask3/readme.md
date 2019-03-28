> Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:

> * What is the meaning of the JSON attribute 'timestamp'?
> * What is the meaning of the JSON attribute 'updated_on'?
> * What is the meaning of the JSON attribute 'origin'?
> * What is the meaning of the JSON attribute 'category'?
> * What is the meaning of the JSON attribute 'uuid'?
> * Which are the common methods of the Perceval backends?
> * List and explain at least 3 Git commands used by the Perceval backend (you can rely on the Git documentation)


The JSON documents can be prepared by piping the output of Perceval.

1) "Timestamp", from it's name and the value itself, looked like it was in Unix time format. After checking, I realized that I was right, and the "timestamp" attribute gives us the time at which the perceval fetch is executed in unix time format.

2) The "updated_on" attribute gives us the time at which the commit, or issue (or whatever, as applicable depending on the backend) happened in unix time format.

3) The "origin" attribute gives us the URI of our specific backend.
For example, for the git backend of perceval it is - 'http://github.com/grimoirelab/perceval.git'
And for the github backend of perceval it is - 'https://github.com/grimoirelab/perceval'

4) The "category" attribute gives us the category of the data that has been mined from the backend. For git it can be a commit, for slack it can be a message and for github it can be an issue or a pull request or a repository.

5) "uuid" category was hard to figure out with just it's value. I knew it stood for "universally unique identifier", and after searching through the perceval files, I found that the uuid is generated from the SHA1 of the concatenation of values from the list of arguments given during configuration/in the CLI.

In backend.py

"""Generate a UUID based on the given parameters.
    The UUID will be the SHA1 of the concatenation of the values
    from the list. The separator bewteedn these values is ':'.
    Each value must be a non-empty string, otherwise, the function
    will raise an exception.
    :param *args: list of arguments used to generate the UUID
    :returns: a universal unique identifier
    :raises ValueError: when anyone of the values is not a string,
        is empty or `None`.
"""

6) The common methods of the perceval backends are:

- fetch_items(self, category, **kwargs)
- has_archiving(cls)
- has_resuming(cls)
- metadata_id(item)
- metadata_updated_on(item)
- metadata_category(item)

7) Some of the git commands used are

- git clone - Clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository (visible using git branch -r), and creates and checks out an initial branch that is forked from the cloned repository's currently active branch.

- git log - Shows the commit logs.
The command takes options applicable to the git rev-list command to control what is shown and how, and options applicable to the git diff-* commands to control how the changes each commit introduces are shown.

- git-fetch - Fetch branches and/or tags (collectively, "refs") from one or more other repositories, along with the objects necessary to complete their histories. Remote-tracking branches are updated (see the description of <refspec> below for ways to control this behavior).

- git-count-objects - Count unpacked number of objects and their disk consumption

- git remote - Manage set of tracked repositories



