#
# ~/.bash_profile
#

# Set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

[[ -f ~/.bashrc ]] && . ~/.bashrc


# Added by Antigravity CLI installer
export PATH="/home/wwm/.local/bin:$PATH"
