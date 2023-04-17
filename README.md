# AWD-WebKiller
适用AWD-WEB-PWN的各种场景下的攻击框架。


如果攻击目标为不同端口时，在target.txt中使用，ip:port格式

## 项目结构
├── README.md
├── conf.yaml
├── core
│   ├── __init__.py
│   ├── common.py
│   └── data.py
├── lib
│   ├── __init__.py
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
