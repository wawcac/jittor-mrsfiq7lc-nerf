# Jittor 可微渲染新视角生成赛题 NeRF、Instant-NGP

![Car_r_6](README.assets\Car_r_6-16566595709211.png)

## 简介
本项目包含了第二届计图挑战赛计图 - 可微渲染新视角生成赛题的代码实现和参数设置。本项目的特点是：对两个Baseline（jrender、jnerf）的默认参数进行调节，达到了更高的PSNR。

## 安装

本项目可在单张 2080Ti 上运行，5个场景训练时间约30分钟到10小时不等。

#### 运行环境
- ubuntu 20.04 LTS
- python >= 3.7
- jittor ==1.3.4

#### 安装依赖

执行以下命令配置环境
```
cd jrender
pip install -r requirements.txt

sudo apt-get install tcl-dev tk-dev python3-tk
cd ../JNeRF
pip install -r requirements.txt
cd python
pip install -e .
```

## 数据下载

执行以下命令下载数：
```
cd jrender
bash download_competition_data.sh
```

## 训练及测试

可分别运行以下命令，对不同场景进行训练、测试：
```
python run.py Easyship
python run.py Car
python run.py Coffee
python run.py Scar
python run.py Scarf
```

测试集上的结果存储在logs文件夹中
