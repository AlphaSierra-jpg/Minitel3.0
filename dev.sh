ssh osboxes@localhost -p 2222 "sudo rm -rf *"

scp -r -P 2222 * osboxes@localhost:~/

