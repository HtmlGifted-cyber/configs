# configs

Bash configuration files and a toolbox of small command-line scripts for Ubuntu / Xubuntu: shell options, a big set of time-saving aliases, and network and system helpers in `bin/`.

**Originally created by Gary DeLaney ([@gld1982ltd](https://github.com/gld1982ltd)).**
**Ubuntu branch extended and maintained by Jeremy A. Henry ([@HtmlGifted-cyber](https://github.com/HtmlGifted-cyber), formerly [@htmlgifted](https://github.com/htmlgifted)).**

I've used and grown these files since Ubuntu 14.04. They currently run daily on Xubuntu 20.04.

## Install

```bash
git clone https://github.com/HtmlGifted-cyber/configs.git && cd configs && ./INSTALL
```

`INSTALL` copies the dotfiles and `bin/` into your home folder. **It overwrites files with the same name**, so back up your own `~/.bashrc`, `~/.bash_aliases` and the rest first. It asks before copying (use `./INSTALL -f` to skip the question).

**Recommended: link instead of copy.** `./INSTALL --link` symlinks the files to your clone, so your machine and the repo are always the same files. Change something, run `pushconfigs "what changed"`, and the repo is updated (files are replaced, not duplicated). On another machine, `pullconfigs` brings the changes down.

**Your own settings stay private:**
- `~/.gitconfig.local`: your Git name and email (the shared `.gitconfig` includes it)
- `~/.bash_aliases.local`: aliases with personal paths, drives or accounts, and `CONFIGS_DIR` (where your clone lives)

```bash
printf '[user]\n    name = Your Name\n    email = you@example.com\n' > ~/.gitconfig.local
```

## What's inside

| File | What it does |
|---|---|
| `.bashrc` | Shell options, history settings, loads the other files |
| `.bash_profile` | Login shell setup |
| `.bash_aliases` | Aliases and functions: safety prompts (`cp -i`, `mv -i`, `rm -I`), `mkalias`, `extract`, `cl`, apt/pacman shortcuts, `reload`, `pushconfigs` / `pullconfigs` |
| `.exports` | Environment variables |
| `.gitconfig` | Git aliases (`git lg`, `git lt`, `git s`...) and colors, with no personal identity |

### bin/

| Script | Purpose |
|---|---|
| `geoip` | Geo-locate an IP address |
| `iptrace` | Trace and look up an IP |
| `whoison` | List devices on your local network (saved to `~/hackstack/nmpresults.txt`) |
| `openports` | List open ports on this machine |
| `scan` / `routerscan` | nmap scans of a host or your router |
| `mybey` | System summary: OS, uptime, disk, RAM, CPU, connected network and IPs (`MYBEY_HIDE_NETWORK=1 mybey` hides network details for screenshots) |
| `myips.sh`, `authhosts.sh` | Show and save local and public IP addresses |
| `traceroute`, `trcerte`, `reverse` | Route tracing and reverse DNS lookups |
| `analystics` | Find sites sharing an analytics ID (hackertarget API) |
| `blockip` | Block an IP with the firewall |
| `killport` | Kill whatever is listening on a port |
| `monitor` | Simple live system monitor |
| `top10`, `whodoinwhat` | Top processes, who's doing what |
| `findd` | Find duplicate files |
| `sshA` | SSH to a host (`SSH_USER` / `SSH_PORT` override the defaults) |
| `sshfsmount` | Mount a remote folder over SSHFS |
| `setup_vhost.sh` | Create an Apache virtual host |
| `seo.py` | Quick on-page SEO score for a URL |
| `person-search.py` | Public-web lookup for a name via Google Programmable Search (needs `GOOGLE_API_KEY` + `GOOGLE_CSE_ID`; use responsibly) |
| `configs-deps` | Checks that everything these scripts need is installed (`configs-deps --install` installs the missing pieces) |
| `tor`, `chrt`, `clsetor`, `exicute` | Misc helpers |
| `hackstack/external.sh` | Used by `mybey`: space on a mounted external drive |

## What the scripts need

Each script just needs its programs installed. Run `configs-deps` to see what's missing and the exact `apt install` line, or `configs-deps --install` to install them.

## Adding your own scripts

Put a new script in `~/bin`, then `addscript myscript` moves it into the repo and links it back. `pushconfigs "added myscript"` publishes it. The toolbox only grows: removing a link from `~/bin` never deletes a script from the repo.

Only scan networks and hosts you own or have permission to test.

## History

- 2013-2015: original configs by Gary DeLaney; Ubuntu branch started by Jeremy (htmlgifted).
- 2021: new `bin/` tools and alias updates for Xubuntu 18.04.
- 2026: moved to [@HtmlGifted-cyber](https://github.com/HtmlGifted-cyber). Brought up to date with the versions in daily use: new tools (`blockip`, `killport`, `monitor`, `routerscan`, `seo.py` and more), refreshed aliases, a `.gitconfig` that no longer carries anyone's identity, and no hard-coded user paths.

If these help you, a star is appreciated.
