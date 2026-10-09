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

After installing, set your own Git identity. The included `.gitconfig` deliberately has none:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Update later with the `reconfig` alias, or `cd ~/configs && ./INSTALL`.

## What's inside

| File | What it does |
|---|---|
| `.bashrc` | Shell options, history settings, loads the other files |
| `.bash_profile` | Login shell setup |
| `.bash_aliases` | Aliases and small functions: `mkalias`, `extract`, `cl` (cd + ls), apt/pacman shortcuts, `reload` |
| `.exports` | Environment variables |
| `.gitconfig` | Git aliases (`git lg`, `git lt`, `git s`...) and colors, with no personal identity |

### bin/

| Script | Purpose |
|---|---|
| `geoip` | Geo-locate an IP address |
| `iptrace` | Trace and look up an IP |
| `whoison` | See who's on the local network |
| `openports` | List open ports on this machine |
| `scan` / `routerscan` | nmap scans of a host or your router |
| `myips.sh`, `authhosts.sh`, `mybey` | Show and save local and public IP addresses |
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
| `seo.py` | Quick on-page SEO score for a URL (needs `requests`, `beautifulsoup4`, `lxml`) |
| `tor`, `chrt`, `clsetor`, `exicute` | Misc helpers |

## Suggested packages

```bash
sudo apt install nmap whois traceroute curl tor sshfs rsync
```

Only scan networks and hosts you own or have permission to test.

## History

- 2013-2015: original configs by Gary DeLaney; Ubuntu branch started by Jeremy (htmlgifted).
- 2021: new `bin/` tools and alias updates for Xubuntu 18.04.
- 2026: moved to [@HtmlGifted-cyber](https://github.com/HtmlGifted-cyber). Brought up to date with the versions in daily use: new tools (`blockip`, `killport`, `monitor`, `routerscan`, `seo.py` and more), refreshed aliases, a `.gitconfig` that no longer carries anyone's identity, and no hard-coded user paths.

If these help you, a star is appreciated.
