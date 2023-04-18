# AWD-WebKiller
适用AWD中WEB和PWN的各种场景下的攻击框架。
可快速修改exp进行批量攻击。

注：如果攻击目标为不同端口时，在target.txt中使用，ip:port格式，通常只用放ip地址即可

## 项目结构

.

├── README.md

├── conf.yaml

├── core

│   ├── common.py

│   └── data.py

├── lib

│   ├── admin.py

│   ├── parseburplog.py

│   ├── pwn_exp.py

│   ├── scan.py

│   ├── ssh.py

│   ├── submit_flag.py

│   └── web_flag.py

├── main.py

├── requirements.txt

└── web_targets.txt