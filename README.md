

## 功能

数据行专列

假码

# uWSGI 安装

这是由于gcc版本不一致导致的，网上看到很多解决办法都是改变gcc版本，
但改变gcc版本会影响到其他的程序。如果python是用anaconda 安装，可以用conda的方式安装uwsgi，问题可以解决

https://blog.csdn.net/king_way/article/details/80821139

```shell
conda install -c conda-forge uwsgi
```

## 启动停止重启

uWSGI 通过 xxx.ini 启动后会在相同目录下生成一个 xxx.pid 的文件，里面只有一行内容是 uWSGI 的主进程的进程号。

#### 启动：

```uwsgi --ini xxx.ini```

#### 重启：

```uwsgi --reload xxx.pid```

#### 停止：

```uwsgi --stop xxx.pid```

原文链接：https://blog.csdn.net/duxin_csdn/article/details/83341922

## 其他参考

runoob上的安装配置 https://www.runoob.com/python3/python-uwsgi.html

ANACONDA上的uwsgi https://anaconda.org/conda-forge/uwsgi
