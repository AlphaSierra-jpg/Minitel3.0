ssh alpha@172.16.24.228 -p 2222 "sudo rm -rf *"

scp -r -P 2222 * alpha@172.16.24.228:~/
