#Simple script to automate the process of git add, commit, push

git add .

echo 'Enter the commit message:'
read commitMessage

git commit -m "$commitMessage"

echo 'Enter the name of the branch:'
read branch

git pull 

git push origin $branch

read

exit 