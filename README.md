# configs

Bash configuration files and a growing toolbox of command-line scripts for Ubuntu / Xubuntu: shell options, a big set of time-saving aliases, and network, system and web helpers in `bin/`.

**Originally created by Gary DeLaney ([@gld1982ltd](https://github.com/gld1982ltd)).**
**Ubuntu branch extended and maintained by Jeremy A. Henry ([@HtmlGifted-cyber](https://github.com/HtmlGifted-cyber), formerly [@htmlgifted](https://github.com/htmlgifted)).**

I've used and grown these files since Ubuntu 14.04. They run every day on Xubuntu 20.04.

---

## Quick start

```bash
git clone https://github.com/HtmlGifted-cyber/configs.git ~/configs
cd ~/configs && ./INSTALL --link
printf '[user]\n    name = Your Name\n    email = you@example.com\n' > ~/.gitconfig.local
configs-deps            # see which programs the scripts still need
```

Open a new terminal and you're set.

### Install options

| Command | What it does |
|---|---|
| `./INSTALL --link` | **Recommended.** Links your home-folder files to this repo instead of copying them, so your machine and the repo are always the *same* files. Any existing files are backed up first to `~/.configs-backup-<date>`. |
| `./INSTALL` | Copies the files into your home folder (asks first; overwrites files with the same name). |
| `./INSTALL -f` | Same copy, without asking. |

---

## What's new in the 2026 update

- **Linked install and one-command sync.** With `./INSTALL --link`, editing `~/.bash_aliases` or a script in `~/bin` edits the repo copy. `pushconfigs "what changed"` commits and pushes it (files are replaced, never duplicated). `pullconfigs` brings changes down on another computer and reloads your shell.
- **Private settings stay private.** Anything personal lives in two local files that are never pushed:
  - `~/.gitconfig.local`: your Git name and email. The shared `.gitconfig` includes it, so the repo carries no one's identity. (Older versions copied the author's identity onto everyone who installed them.)
  - `~/.bash_aliases.local`: aliases with personal paths, drives, servers or accounts. It's loaded automatically at the end of `.bash_aliases`.
- **`addscript`: the toolbox only grows.** Drop a new script in `~/bin` and run `addscript myscript`. It moves the script into the repo, makes it executable, and links it back. It refuses to overwrite a script with the same name, so you never get duplicates, and removing a link from `~/bin` never deletes a script from the repo.
- **`configs-deps`: know what each script needs.** It checks every program and Python library the scripts use, says which scripts need anything that's missing, and prints the exact `apt install` line. `configs-deps --install` installs them for you.
- **New tools:** `netwatch`, `blockip`, `killport`, `monitor`, `routerscan`, `reverse`, `analystics`, `findd`, `top10`, `whodoinwhat`, `myips.sh`, `authhosts.sh`, `trcerte`, `setup_vhost.sh`, `sshA`, `seo.py`, `person-search.py`, `configs-deps`, and `hackstack/external.sh`.
- **Updated tools:**
  - `mybey` v0.03 shows only the network you're connected to (it used to list every Wi-Fi network in range). `MYBEY_HIDE_NETWORK=1 mybey` hides network name and IPs for screenshots. Works without `ifconfig`, and the saved public-IP file no longer gets blanked.
  - `whoison` runs one scan instead of two and really saves the results.
  - `geoip`, `iptrace`, `openports` and `scan` are refreshed to their current versions.
- **Fixes:**
  - `traceroute` used to call itself forever (it shares the system command's name, and `~/bin` comes first in your PATH). It now runs the real traceroute and asks for an address if you don't give one.
  - `analystics` never received your input (a `read` typo). It now also takes the ID or domain as an argument.
  - `sshfsmount` no longer has a server login built in. Pass the remote folder, or set `SSHFS_REMOTE` / `SSHFS_MOUNT` in `~/.bash_aliases.local`.
  - `person-search.py` couldn't run (Python errors). It's rebuilt and reads its API keys from environment variables.
  - Every script in `bin/` is executable, and none has hard-coded user paths.
  - Removed a global `[branch "master"]` Git setting that gave every repo two upstreams and broke plain `git push`.

---

## What's inside

### Dotfiles

| File | What it does |
|---|---|
| `.bashrc` | Shell options (typo correction for `cd`, appended history, case-insensitive globbing), 10,000-line history, loads the other files |
| `.bash_profile` | Login-shell setup: adds `~/bin` to your PATH and loads `.bashrc` |
| `.bash_aliases` | Aliases and functions (see below) |
| `.exports` | Environment variables |
| `.gitconfig` | Git shortcuts (`git lg` pretty log, `git lt` graph, `git s` short status, `git go`, `git cm`...), colors, whitespace checks, and an include for your private `~/.gitconfig.local` |

### Aliases and functions highlights

| Name | What it does |
|---|---|
| `cp`, `mv`, `rm`, `ln` | Safety prompts before overwriting or deleting (`rm -I` asks once for big deletes) |
| `chown`, `chmod`, `chgrp` | `--preserve-root`, so you can't accidentally change all of `/` |
| `ll`, `la`, `lt`, `lz`, `lx` | Long listings: all files, by date, by size, by extension |
| `update`, `upgrade`, `install`, `remove`, `autoclean`, `clean`, `fix`, `config` | Short apt commands |
| `extract <file>` | Unpacks zip, tar, tar.gz, tgz, tar.bz2, tbz2, bz2, gz, rar and 7z archives |
| `mkalias name "command"` | Creates a new alias and saves it permanently |
| `cl <folder>` | `cd` and `ls` in one step |
| `reload` | Clears the screen and reloads your shell settings |
| `getlocal`, `getpub`, `getzen` | Show your saved local / public IP, or a GitHub zen quote |
| `pushconfigs`, `pullconfigs`, `addscript` | Sync and grow this repo (see "What's new") |
| `cls`, `:q`, `cd..` | Real screen clear, and forgiving typos for exit and `cd ..` |

### bin/ scripts

Run any script by name. Most ask for what they need (an IP, a folder, a port) if you don't pass it.

**Network and security**

| Script | What it does |
|---|---|
| `whoison` | Lists every device answering on your local network; saved to `~/hackstack/nmpresults.txt` |
| `routerscan` | Scans your router's network range for unexpected devices |
| `openports` | Port scan of a remote host with nmap |
| `scan` | Shows this computer's active connections and listening ports |
| `chrt` | Shows your network route table |
| `monitor` | Watches for new network interfaces appearing (USB tethering, VPN, new adapters) every 5 seconds |
| `netwatch` | Security watch for cron: alerts (desktop + log) when a new device joins your network or a new port opens. `netwatch status`, `netwatch trust` |
| `blockip` | Blocks an IP address in the ufw firewall |
| `killport` | Stops whatever program is using a port |
| `myips.sh` | Saves this computer's local IP to a file and shows it |
| `authhosts.sh` | Saves this computer's local IP to a file (quiet version, for other scripts) |
| `geoip` | Country / location of an IP address (geoiplookup); saved to `~/hackstack` |
| `iptrace` | Traces the route to an IP address; saved to `~/hackstack` |
| `traceroute` | Runs the real traceroute; asks for an address if you don't give one |
| `trcerte` | Asks for an address, traces it, and saves the result to `~/hackstack` |
| `reverse` | Reverse IP lookup: other domains hosted on the same IP (HackerTarget API) |
| `tor` / `clsetor` | Route your terminal through Tor and show your Tor IP / turn it off and show your normal IP |

**System**

| Script | What it does |
|---|---|
| `mybey` | One-screen system summary: OS, kernel, uptime, disk (home and external), RAM, CPU, packages, connected network, IPs and your tools |
| `whodoinwhat` | Who is logged in and what they're running |
| `findd` | Finds duplicate files in a folder (rdfind) |
| `exicute <file>` | Makes a file executable |
| `configs-deps` | Checks (and with `--install`, installs) everything these scripts need |
| `hackstack/external.sh` | Used by `mybey`: space used on a mounted external drive |

**Remote and web**

| Script | What it does |
|---|---|
| `sshA` | SSH to a host you type in (`SSH_USER` / `SSH_PORT` change the defaults) |
| `sshfsmount` | Mounts a folder from another computer over SSH |
| `setup_vhost.sh` | Creates a new Apache website (virtual host): folders, config, enables it and restarts Apache |
| `seo.py` | Asks for a URL and gives a quick on-page SEO score with a list of issues |
| `analystics <ID or domain>` | Finds other sites sharing a Google Analytics / AdSense ID |
| `person-search.py "Name"` | Public-web lookup for a name via Google Programmable Search; saves a JSON report. Needs `GOOGLE_API_KEY` and `GOOGLE_CSE_ID`. Use responsibly. |
| `top10` | Searches Google for today's top 10 best-selling books (googler) |

Results that scripts save go in `~/hackstack/`.

---

## What the scripts need

Each script only needs its programs installed. Run `configs-deps` to see what's missing:

```text
nmap, traceroute, curl, wget, tor, torsocks, sshfs, openssh-client, ufw, net-tools,
psmisc, network-manager, bind9-host, geoip-bin, rdfind, googler, apache2 (for setup_vhost.sh),
python3-requests, python3-bs4, python3-lxml
```

Only scan networks and hosts you own or have permission to test.

---

## Everyday workflow

```bash
nano ~/bin/newtool && addscript newtool    # add a new script to the toolbox
pushconfigs "added newtool"                # publish your changes
pullconfigs                                # on another computer: get the latest
```

---

## History

- **2013-2015:** original configs by Gary DeLaney; Ubuntu branch started by Jeremy (htmlgifted).
- **2021:** new `bin/` tools and alias updates for Xubuntu 18.04.
- **2026:** moved to [@HtmlGifted-cyber](https://github.com/HtmlGifted-cyber). Brought up to the versions in daily use, plus the linked install, private local settings, `addscript`, `configs-deps`, and the fixes listed above.

If these help you, a star is appreciated.
