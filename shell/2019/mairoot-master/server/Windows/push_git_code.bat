@ echo off
@ title bat push gitlab server
g:
cd /g/8.测试/test
git config --global user.name "mai"
git remote add origin https://gitlab.mairoot.com/mai/test.git
git add .
git commit -m "everyday push file"
git push -u origin slave