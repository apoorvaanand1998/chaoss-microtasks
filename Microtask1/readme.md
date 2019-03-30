> Set up Perceval to be executed from PyCharm.

### Method 1
Perceval can be set up to be executed by pycharm as shown [here.](https://stackoverflow.com/questions/26069254/importerror-no-module-named-bottle-pycharm)

Here's a screenshot from me:

![AA's setup](/Microtask1/Images/perceval_setup.png)

### Method 2
Perceval can also be set up by installing perceval using pip in the virtual environment of our project. 
- Activate the virtual environment (`source path/to/venv/bin/activate`)
- `$ pip3 install perceval`

Running perceval through python 

![Perceval Python](/Microtask1/Images/perceval_config.png)

Running perceval through the terminal

![Perceval Terminal](/Microtask1/Images/perceval_terminal.png)

Additionally, the [grimoirelab-toolkit](https://github.com/chaoss/grimoirelab-toolkit) can be used for debugging and using functions for datetime, introspection and URIs. It can be imported as follows:
- Activate the virtual environment (`source path/to/venv/bin/activate`)
- cd to the project
- `git clone https://github.com/chaoss/grimoirelab-toolkit.git`
- cd to grimoirelab-toolkit
- Build using instructions [here](https://github.com/chaoss/grimoirelab-toolkit#installation)

The project structure looks like this after doing everything above:

![GrimoireLab Toolkit](Images/grimoirelab_toolkit.png)


For running [the script](
        chaoss-microtasks/Microtask1/microtask1.py
      ) in this microtask yourself, clone this repo and run the script with a Github repo and token as arguments in the command line.


