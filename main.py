from bot import Bot

Bot().run()

SCRIPTNAME="script"

SCRIPT="script.sh"

echo "running $SCRIPTNAME nohup" "$@"

tmux new-window -d -t "nohup-${SCRIPTNAME}": "$SCRIPT" "$@" || tmux new -d -s "nohup-${SCRIPTNAME}" "$SCRIPT" "$@"
