#Dockerfile
FROM ubuntu:14.04
MAINTAINER he.wenxin

RUN echo 'root:123' | chpasswd

# change timezone to shanghai
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#update apt repository
RUN rm -f /etc/apt/sources.list
ADD sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install --no-install-recommends -y \
    git curl ant make maven \
    cmake gcc g++ \
    protobuf-compiler libprotoc-dev \
    protobuf-c-compiler libprotobuf-dev \
    build-essential libtool \
    zlib1g-dev pkg-config libssl-dev \
    snappy libsnappy-dev \
    bzip2 libbz2-dev \
    libjansson-dev \
    fuse libfuse-dev \
    libcurl4-openssl-dev \
    python python2.7 pylint \
    doxygen \
    mysql-server vim tree

# install jdk
RUN apt-get install -y openjdk-7-jdk

RUN mkdir -p /usr/java
RUN ln -s /usr/lib/jvm/java-1.7.0-openjdk-amd64 /usr/java/jdk

# install python
RUN apt-get install -y python-dev python-pip libffi-dev

RUN mkdir -p /root/.pip
RUN echo '[global] \nindex-url=http://10.31.48.30/pypi/simple' > /root/.pip/pip.conf

# install robotframework
RUN pip install cffi
RUN pip install robotframework robotframework-selenium2library robotframework-httplibrary \
                robotframework-sshlibrary requests robotframework-requests

# install openssh server
RUN apt-get install -y openssh-server openssh-client

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
#RUN sed -i -e 's~^\(.*\)/usr/libexec/openssh/sftp-server$~\1internal-sftp~g' /etc/ssh/sshd_config

RUN mkdir /var/run/sshd

EXPOSE 22
CMD /usr/sbin/sshd -D
#End
