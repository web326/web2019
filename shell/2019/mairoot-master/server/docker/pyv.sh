# 01. 构建pyv镜像
docker pull centos:6.8
if [[ $? -eq 0 ]] ; then
cat > dockerfile << EOF
FROM centos:6.8
RUN yum -y update
RUN LANG=en_US.UTF-8
RUN useradd mai;echo "2" |passwd --stdin mai
RUN yum install -y vim wget inetutils-ping net-tools sudo
RUN echo "mai ALL=(root) NOPASSWD:ALL" >>/etc/sudoers.d/mai
USER mai
RUN sudo yum install -y git gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel libcurl-devel expat-devel perl-ExtUtils-MakeMaker package gettext-devel nss
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
RUN echo export PATH=\"/home/mai/.pyenv/bin:\$PATH\" >> /home/mai/.bash_profile
RUN echo eval \"\$\(pyenv init -\)\" >> /home/mai/.bash_profile
RUN echo eval \"\$\(pyenv virtualenv-init -\)\" >> /home/mai/.bash_profile
RUN source /home/mai/.bash_profile
ENV LANG='en_US.UTF-8'
CMD ["/bin/bash"]
RUN cd /home/mai
RUN /home/mai/.pyenv/bin/pyenv install 3.5.3 -v
EOF
fi
docker build -t py:v1 .
Os_code=$?

# 02. 运行pyv镜像`
if [[ $Os_code -eq 0 ]] ; then
docker run -it --name pyv1 -d py:v1
docker exec -it pyv1 bash
fi
cd /home/mai
source .bash_profil
