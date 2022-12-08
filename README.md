<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-exchangerate

_✨ 简单汇率换算 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/A-kirami/nonebot-plugin-exchangerate.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-exchangerate">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-exchangerate.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>


## 📖 介绍

支持汇率换算与汇率查询

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-exchangerate

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-exchangerate
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-exchangerate
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-exchangerate
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-exchangerate
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot_plugin_exchangerate')

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| EXCHANGE_APP_KEY | 是 | 无 | 聚合数据的汇率APP_KEY，[点击此处](https://www.juhe.cn/docs/api/id/80)获取 |
| EXCHANGE_DECIMALS | 否 | 2 | 汇率换算保留小数位 |

## 🎉 使用
### 指令表
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| 数字+货币名称 | 否 | 私聊/群聊 | 将该数量的货币换算为对应的人民币，如：200日元 |
| 货币名称+汇率 | 否 | 私聊/群聊 | 展示该货币的汇率详情 |
| 汇率列表/货币列表 | 否 | 私聊/群聊 | 查看支持的货币清单 |
