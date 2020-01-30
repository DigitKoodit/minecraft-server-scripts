while true;
do
	java -Xms2G -Xmx3G -jar paper-71.jar
	echo "Server stopped, restarting in 10 seconds..."
	echo "If you want to exit server, use tmux kill-session asap"
	sleep 10
done
