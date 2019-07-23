# 01. pyenv虚拟环境
yum -y update
LANG=en_US.UTF-8
useradd mai;echo "2" |passwd --stdin mai
yum install -y vim wget inetutils-ping net-tools sudo
echo "mai ALL=(root) NOPASSWD:ALL" >>/etc/sudoers.d/mai
su - mai
pwd
sudo yum install -y git gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel libcurl-devel expat-devel perl-ExtUtils-MakeMaker package gettext-devel nss
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
if [[ $? -eq 0 ]] ; then
echo "pyenv install Successful!"
fi
cat > /home/mai/.bash_profile << EOF
export PATH="/home/mai/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOF
source /home/mai/.bash_profile
/home/mai/.pyenv/bin/pyenv install 3.5.3 -v
if [[ $? -eq 0 ]] ; then
echo "python3.5.3 install Successful!"
fi
