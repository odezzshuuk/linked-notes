# Tomcat Install On Linux

[article I](https://www.atlantic.net/dedicated-server-hosting/how-to-install-apache-tomcat-10-on-rocky-linux-8/)
[article II](https://kifarunix.com/install-apache-tomcat-on-rocky-linux-8/)

- [tar]
- [chmod]
- [chown]
- [alternatives]
- [etc/profile](../linux/linux-system-environment.md)

## rocky linux

download a `tar.gz`package to a temporary directory, like `/tmp`

```bash
cd /tmp
curl -O https://dlcdn.apache.org/tomcat/tomcat-10/v10.0.27/bin/apache-tomcat-10.0.27.tar.gz
```

uncompress to `/opt/tomcat`

```bash
cd /opt/tomcat
sudo tar xzvf path/to/apache-tomcat-10.0.27.tar.gz
```

## Set Environment Variables

use [`alternatives`](linux-alternatives.md) to check the path of java command, to set `JAVA_HOME

```bash
alternatives --list | grep java
```

If the output is as follows:

```
/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.352.b08-2.el9_1.x86_64/bin/java
```

`JAVA_HOME` is `/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.352.b08-2.el9_1.x86_64`

[Environment variables](linux-system-environment.md) `JAVA_HOME`, `CATALINA_HOME`, are set in the `/etc/profile.d/tomcat.sh` file

```bash
vim /etc/profile.d/tomcat.sh
```

Add the following content

```
export CATALINA_HOME="/opt/tomcat"
export JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.352.b08-2.el9_1.x86_64"
```

## Create User

**web server usually does not run as a privileged user**

create user: `tomcat`

```bash
useradd -r -d /opt/tomcat/ -s /bin/false -c "Apach Tomcat User" tomcat
```

set access permission

```bash
chown -R tomcat: /opt/tomcat
```

## Set Web Management Accounts

This account is used to manage Tomcat and can be accessed via `http://localhost:8080/manager/html`

```bash
vim /opt/tomcat/conf/tomcat-users.xml
```
When accessing `http://localhost:8080/manager/html`, you need to enter a username and password for authentication

```xml
<tomcat-users>
  ...
  <role rolename="admin-gui"/>
  <role rolename="manager-gui"/>
  <user username="admin" password="mystrongpassword" roles="admin-gui,manager-gui"/>
</tomcat-users>
```

- Set the username and password to `admin` and `mystrongpassword` respectively

## Configure Remote Host

> By default, Tomcat only allows local access; you need to modify the configuration file

```bash
vim /opt/tomcat/webapps/manager/META-INF/context.xml
```

Delete this line

```xml
<Valve className="org.apache.catalina.valves.remoteAddrValve" allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1">
```

## allow external access

```sh
firewall-cmd --permanent --add-port=8080/tcp
firewall-cmd --reload
```

## Run As Service

```sh
vim /etc/systemd/system/tomcat.service
```

```
[Unit]
Description=Apache Tomcat Server
After=syslog.target network.target

[Service]
Type=forking
User=tomcat
Group=tomcat

Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat

ExecStart=/opt/tomcat/bin/catalina.sh start
ExecStop=/opt/tomcat/bin/catalina.sh stop

RestartSec=10
Restart=always
[Install]
WantedBy=multi-user.target
```

[start and enable](/sorted/linux/linux-system-command.md#systemctl)

```bash
systemctl enable --now tomcat
```

check

```bash
system status tomcat
```

output like:

```
● tomcat.service - Apache Tomcat Web Application Container
     Loaded: loaded (/etc/systemd/system/tomcat.service; enabled; vendor preset: disabled)
     Active: active (running) since Fri 2022-12-02 15:36:57 CST; 3 days ago
   Main PID: 42026 (java)
      Tasks: 27 (limit: 10768)
     Memory: 145.4M
        CPU: 16min 19.334s
     CGroup: /system.slice/tomcat.service
             └─42026 /usr/lib/jvm/jre/bin/java -Djava.util.logging.config.file=/opt/tomcat/conf/logging.properties -Djava.util.logging.manager=org.apac>

Dec 02 15:36:57 localhost.localdomain systemd[1]: Starting Apache Tomcat Web Application Container...
Dec 02 15:36:57 localhost.localdomain startup.sh[42019]: Tomcat started.
Dec 02 15:36:57 localhost.localdomain systemd[1]: Started Apache Tomcat Web Application Container.
```
