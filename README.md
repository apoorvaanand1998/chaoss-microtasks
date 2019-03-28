## chaoss-microtasks
My solutions to the CHAOSS microtasks for GSoC Idea #3: Support of Source Code Related Metrics 

Check inside each directory for the solutions/explanations and how to run the scripts.


    Microtask 0:
    Download PyCharm and get familiar with it (for instance, you can follow this tutorial).

    Microtask 1:
    Set up Perceval to be executed from PyCharm.

    Microtask 2:
    Create a Python script to execute Perceval via its Python interface using the Git and GitHub backends. Feel free to select any target repository, for instance the GitHub repository hosting Perceval.

    Microtask 3:
    Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:
        What is the meaning of the JSON attribute 'timestamp'?
        What is the meaning of the JSON attribute 'updated_on'?
        What is the meaning of the JSON attribute 'origin'?
        What is the meaning of the JSON attribute 'category'?
        What is the meaning of the JSON attribute 'uuid'?
        Which are the common methods of the Perceval backends?
        List and explain at least 3 Git commands used by the Perceval backend (you can rely on the Git documentation)

    Microtask 4:
    Create a Python script to fetch data from SoftwareHeritage using its API.
    Given a target GitHub repository, the script should return a message if the repository is not available on SoftwareHeritage or the date of the last visit.
    The script should rely on the endpoints: origin and visits.
    Please use the Python library requests to issue requests to the SofwareHeritage API.

    Microtask 5:
    Set up Graal to be executed from PyCharm.

    Microtask 6:
    Create a Python script to execute Graal via its Python interface using the CoCom and CoLic backends. Feel free to select any target repository, for instance the GitHub repository hosting Toolkit.

    Microtask 7:
    Based on the JSON documents produced by Graal and its source code, try to answer the following questions:
        Which are the common methods of the Graal backends?
        List and explain at least 2 Git commands used by Graal (and not implemented in Perceval).

    Microtask 8:
    Create a Python script to execute flake8 for a given commit of any Git repository. Given a commit SHA and a Git repository, the script should clone the repository (if it doesn't exist locally), perform a checkout based on the commit SHA and execute flake8 on that checkout. The script should return a message that either lists the errors found or "OK" if flake8 successfully ended.

    Microtask 9:
    Submit at least a PR to one of the GrimoireLab repositories to fix an issue, improve the documentation, etc.

