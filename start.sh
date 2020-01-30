tmux new -s minecraft-server

tmux split-window -v

tmux send-keys -t 1 "./launch.sh" Enter
