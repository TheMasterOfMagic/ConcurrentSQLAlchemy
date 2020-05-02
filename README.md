# 通过SQLAlchemy并发地访问MySQL数据库

最近做项目时遇到了「多进程多线程地使用SQLAlchemy访问MySQL数据库」的需求。  
在此之前我已经写好了一个「单进程单线程」版本的脚本。  
按理说Python是很容易实现多进程多线程的。MySQL肯定也是支持多进程多线程访问的。  
然而当我简单地拿上述脚本去套「多进程多线程」时发现出错了，既不支持单个进程里有多线程，也不支持主进程下有多个子进程。  
于是做了个实验，研究了一下。  
最后算是把问题解决了吧。  

简要总结解决方案：
- `engine`不能跨进程（每个进程一份）
- `Session`不能跨线程（每个线程一份）
  - 线程内部可以借助`scoped_session`来使线程内部每次执行`Session()`时获得同一个会话

本实验在以下环境中运行通过：
- Ubuntu 18.04 及 Mac OS X 10.15.4
- Python 3.6.9
  - SQLAlchemy==1.3.12
  - mysqlclient==1.4.4
- Docker 19.03.6
  - mysql:8.0.18 

注：
- 在Ubuntu 18.04上，安装`mysqlclient`库之前需要先执行`apt install libmysqlclient-dev`以提供底层支持（若是在Mac OS X 10.15.4上则需要执行`brew install mysql`）
- `MySQL`服务通过Docker提供，在本实验中镜像启动命令为`docker run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -p 3306:3306 mysql:8.0.18`

实验过程大概分这么几个步骤：
1. [添加与数据库无关的初始并发脚本](https://github.com/TheMasterOfMagic/ConcurrentSQLAlchemy/tree/62078ea)
2. [修改为涉及数据库的单进程单线程脚本](https://github.com/TheMasterOfMagic/ConcurrentSQLAlchemy/tree/cd51102)
3. [升级为粗暴支持单进程多线程的脚本](https://github.com/TheMasterOfMagic/ConcurrentSQLAlchemy/tree/2cb73bf)
4. [升级为优雅支持单进程多线程的脚本](https://github.com/TheMasterOfMagic/ConcurrentSQLAlchemy/tree/7f090ce)
5. [升级为支持多进程多线程的脚本](https://github.com/TheMasterOfMagic/ConcurrentSQLAlchemy/tree/e1bfbc4)
