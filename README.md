# 奖学金seeker

 寻找下哪个学院又偷偷发奖学金了

 目前实现了北京理工大学院的“奖助学金”自动爬取，通过github action自动爬取数据，通过邮件的方式发送到指定邮箱。

# 代码使用方式：

## 需要的环境

    基础的爬虫环境：只要能运行requests和beautifulsoup库的环境即可。

    pyinstaller  ：将代码转换为.exe文件，后直接让Github Action运行这个.exe文件。（个人认为这样速度快一些）这个.exe会生成一个output.txt文件，存放爬取到的数据。

    一个支持smtp的邮箱，用于发送邮件。（QQ邮箱就可以）

## 代码修改（如何化为己用）

    1. 爬取网页的修改：
        网页信息存放于website.json文件中，包含网页的url，名称和flag。flag是一个标志位，用于标志网页中的奖学金列表中是否包含日期（有些网页中没有日期，只有标题）。如果网页中有日期，则为true，没有则为false。

    2. Github action配置
        需要使用secret存放邮箱的账号和密码（需要查看邮箱网站的smtp端口号和授权码）。对于触发时间的确定，直接在cron触发方式中修改（注意使用UTC时间）。

    3. 使用pyinstaller将master.py转换为.exe文件
        在master.py文件所在目录下，运行命令：
        ```
        pyinstaller --onefile master.py
        ```
        这样会在dist文件夹下生成一个master.exe文件，同时将配置好的website.json文件也放到dist文件下，代码就可以完美运行了。

## 注意事项

    1. 由于代码中使用了smtp发送邮件，所以需要开启邮箱的smtp服务，并且获取授权码。

    2. 由于代码中使用了github action，所以需要开启action功能。且Github action对于私人仓库有运行总时间的限制。如果网络环境正常，代码运行约为40s，最长也就3min。

    3. 不要对学校网站进行频率过高的爬取，这很不道德

    4. 代码中使用了一些简单的异常处理，但是仍然可能会出现一些问题，需要自己进行调试。Github自身网络也不稳定，有可能出现爬取失败的情况（大概1/10的概率），可以通过手动触发来重新爬取。

    5. 该项目旨在帮助大家更快获得相关信息（换个关键词就可以检索留学，志愿等信息），减少由于信息壁垒造成的不公平。

    6. 时间紧，纯娱乐，代码粗糙，请见谅。
