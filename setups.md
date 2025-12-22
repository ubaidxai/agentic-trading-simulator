# WSL - Windows Subsystem for Linux

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
6. And, from within your new projects directory, clone the repo with `git clone https://github.com/ubaidxai/agentic-trading-simulator.git`
7. Now go into your Project Root Directory, with `cd agentic-trading-simulator`
8. And now run the all-powerful `uv sync`


### Part 3: Configure IDE running in your PC environment
1. Open IDE, the usual way, on your PC
2. Download the Extension: `WSL`
3. Now press Ctrl+Shift+P and search for WSL: New Window.
4. In the new WSL IDE window, Select the project folder to Open it.
5. In the WSL IDE window, download the Extenions: `Python (ms-python)`, `Jupyter (microsoft)`, and all the necessary extensions by clicking the "Install in WSL-Ubuntu" button.

### And you should be ready to roll!
You'll need to create a new ".env" file in the agents folder, and copy across your .env from your other project. And you'll need to click "Select Kernel" and "Choose python environment..".

# Node
For Windows (WSL), we'll use linux instructions:
1. Head towards the wsl linux terminal.
2. Run `curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`
3. Restart terminal, Run: `source ~/.bashrc`
3. Then, `nvm install 24.12.0`
4. Verify `node -v`

# PlayWright
1. First install the python package: `uv add playwright`.
2. Then, `uv run playwright install --with-deps chromium`.  