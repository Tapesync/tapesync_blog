jekyll build
rsync -cruP _site -e "ssh -p 2224" oivvio@collins.liberationtech.net:/home/oivvio/sites/tapesync_blog/
