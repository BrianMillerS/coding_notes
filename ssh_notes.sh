
# connect to WWU vpn (wwu wireless netweork)
https://securevpn.wwu.edu

# connect to pollard PC
# -X allows for forwarding of display screens
ssh -X pollardlab@140.160.89.249
ssh -X -p 922 mille453@linux.cs.wwu.edu

# open nautilus and remote access files
sftp://pollardlab@140.160.89.249

# vnc remote desktop
ssh -L 5901:127.0.0.1:5901 -N -f -l pollardlab 140.160.89.249

##start a tmux terminal session on the remote machine to run all the commands while you are logged off
# ssh into the remote computer and cd to the desired directory
tmux  # activates the session
press [Ctrl]+[b] and then [$] to rename the session  # optional
# start running desired commands
press [Ctrl]+[b] and then [d]  # detaches you from the session but lets it run while you are gone
#exit the ssh if you wish, then when you ssh back into that computer...
tmux list-sessions  # tells you which sessions are running
tmux attach  # attaches you back to the session

# copy a file using scp
scp /path/to/file username@a:/path/to/destination
scp /path/to/file brian@140.160.205.6:~/Desktop



mille453
1!Pickle

ssh://pollardlab@140.160.89.237
30Degrees!
