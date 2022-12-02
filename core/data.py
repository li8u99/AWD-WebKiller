from collections import OrderedDict

banner = r'''
 __                                                   .___
_/  |_  _______________________       _____ __  _  ____| _/
\   __\/ __ \_  __ \_  __ \__  \      \__  \\ \/ \/ / __ | 
 |  | \  ___/|  | \/|  | \// __ \_     / __ \\     / /_/ | 
 |__|  \___  >__|   |__|  (____  /____(____  /\/\_/\____ | 
           \/                  \/_____/    \/           \/ 
      @TERRASEC                 v1.0  d1mang｜黔灵山Xo.
                                       

1. 存活探测  2、SSH攻击  3.WEB攻击          
           '''

IP_REGEX = r"(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]" \
           r"\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\."

FLAG_REGEX = r"flag{.*}"

conf = OrderedDict()

cookies = OrderedDict()
