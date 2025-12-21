# Setting up WSL - Windows Subsystem for Linux

### Part 1: Install WSL if you haven't before
WSL is the Microsoft recommended way to run Linux on your Windows PC, as described here:  
https://learn.microsoft.com/en-us/windows/wsl/install

And, We will be using the default Ubuntu distribution of Linux, which seems to work fine.

1. Open a powershell
2. Run: `wsl --install`
3. Select to allow elevated permissions when/if it asks; then wait for Ubuntu to install
4. Then run `wsl` to start it and set your Linux username and password
5. Type `pwd` and `ls` to see what directory you're in, and list the contents. Then type `cd` to change to your home directory, and repeat.

It's important to appreciate the difference between your Windows home directory, and this new home directory in your Linux WSL..


### Part 2: Install uv and repo
1. From a powershell, run `ubuntu`. If not recognized, run `wsl -d Ubuntu`.
2. run `curl -LsSf https://astral.sh/uv/install.sh | sh` to install uv.
3. After that completes, you need to type `exit` to leave WSL and return to the Powershell and then type `ubuntu` to return to Linux, in order that changes to PATH are picked up.
4. Now type `pwd` to check you're in your Linux home directory. If in doubt, `cd ~` and `ls` to check.
5. Now create a projects directory with `mkdir projects` then `cd projects` to go into it.
6. And, from within your new projects directory, clone the repo with `git clone https://github.com/ubaidxai/setups-and-installations.git`


7. Now go into your new agents directory, your Project Root Directory, with `cd agents`
8. And now run the all-powerful `uv sync`

At this point, I experienced an unpleasant memory error. I believe it's related to my setup, and you shouldn't hit it. But if you do, please let me know - I have a fix!



---


### Part 3: Configure Cursor running in your PC environment

1. Open Cursor, the usual way, on your PC
2. Bring up the Extensions panel (View menu >> Extensions or Ctrl+Shift+X), search for WSL, see WSL by Anysphere (the makers of Cursor) and Install it
3. Now press Ctrl+Shift+P and search for Remote-WSL: New Window and select it to Open a new window configured for WSL
4. Select Open Project (then get a coffee), and navigate to your new "agents" project root directory in Linux, and then Open or Select Folder
5. Bring up the Extensions panel again (Ctrl+Shift+X) and install these Extensions in your WSL if not already installed: Python (ms-python), and Jupyter (microsoft), clicking the "Install in WSL-Ubuntu" button

### And you should be ready to roll!

You'll need to create a new ".env" file in the agents folder, and copy across your .env from your other project. And you'll need to click "Select Kernel" and "Choose python environment..".

Enjoy MCP!