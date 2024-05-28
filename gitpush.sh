#Simple script to automate the process of git add, commit, push

set -x # To Enable Debug mode while the script execute

git add .

echo 'Enter the commit message:'
read commitMessage

git commit -m "$commitMessage"

echo 'Enter the name of the branch:'
read branch

git pull 

git push origin $branch

exit 0