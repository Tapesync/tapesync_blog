if git status --porcelain | grep .; then
    echo "Repo is dirty, add, commit and push please." 
else
    echo "Repo is clean. I'll build and push to the server"
    jekyll build
    rsync -cruP _site -e "ssh -p 2224" oivvio@collins.liberationtech.net:/home/oivvio/sites/tapesync_blog/
fi


