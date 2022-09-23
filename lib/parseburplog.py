import re
import requests



def parseburprequest(reqreslist: list):
    match = re.search(r"\A([A-Z]+) (.+) HTTP/[\d.]+\Z",reqreslist[0].strip('\n'))
    if match:
        mathod = match.group(1)
        url = match.group(2)
    else:
        print("数据包有误")
        return None
    header = {}
    data = None
    params = False
    for request in reqreslist:
        if len(request.strip()) == 0 and mathod == 'POST' and data is None:
            data = ""
            params = True
        elif data is not None and params:
            data += "%s" % request

        if re.search(r"\A\S+:", request):
            key, value = request.split(":", 1)
            if key == "Host":
                continue
            value = value.strip().replace("\r", "").replace("\n", "")
            header[key] = value

    return header, url, data, mathod


    # for match in reqreslist:
    #     request = re.sub(r"\A[^\w]+", "", match)
    #     schemePort = re.search(r"(http[\w]*)\:\/\/.*?\:([\d]+).+?={10,}", request, re.I | re.S)
    #
    #     if schemePort:
    #         scheme = schemePort.group(1)
    #         port = schemePort.group(2)
    #         request = re.sub(r"\n=+\Z", "", request.split(schemePort.group(0))[-1].lstrip())
    #     else:
    #         scheme, port = None, None
    #
    #     if "HTTP/" not in request:
    #         continue
    #
    #     if re.search(r"^[\n]*%s[^?]*?\.(%s)\sHTTP\/" % (HTTPMETHOD.GET, "|".join(CRAWL_EXCLUDE_EXTENSIONS)), request,
    #                  re.I | re.M):
    #         if not re.search(r"^[\n]*%s[^\n]*\*[^\n]*\sHTTP\/" % HTTPMETHOD.GET, request, re.I | re.M):
    #             continue
    #
    #     getPostReq = False
    #     url = None
    #     host = None
    #     method = None
    #     data = None
    #     cookie = None
    #     params = False
    #     newline = None
    #     lines = request.split('\n')
    #     headers = []
    #
    #     for index in range(len(lines)):
    #         line = lines[index]
    #
    #         if not line.strip() and index == len(lines) - 1:
    #             break
    #
    #         newline = "\r\n" if line.endswith('\r') else '\n'
    #         line = line.strip('\r')
    #         match = re.search(r"\A([A-Z]+) (.+) HTTP/[\d.]+\Z", line) if not method else None
    #
    #         if len(line.strip()) == 0 and method and method != HTTPMETHOD.GET and data is None:
    #             data = ""
    #             params = True
    #
    #         elif match:
    #             method = match.group(1)
    #             url = match.group(2)
    #
    #             if any(_ in line for _ in ('?', '=', kb.customInjectionMark)):
    #                 params = True
    #
    #             getPostReq = True
    #
    #         # POST parameters
    #         elif data is not None and params:
    #             data += "%s%s" % (line, newline)
    #
    #         # GET parameters
    #         elif "?" in line and "=" in line and ": " not in line:
    #             params = True
    #
    #         # Headers
    #         elif re.search(r"\A\S+:", line):
    #             key, value = line.split(":", 1)
    #             value = value.strip().replace("\r", "").replace("\n", "")
    #
    #             # Note: overriding values with --headers '...'
    #             match = re.search(r"(?i)\b(%s): ([^\n]*)" % re.escape(key), conf.headers or "")
    #             if match:
    #                 key, value = match.groups()
    #
    #             # Cookie and Host headers
    #             if key.upper() == HTTP_HEADER.COOKIE.upper():
    #                 cookie = value
    #             elif key.upper() == HTTP_HEADER.HOST.upper():
    #                 if '://' in value:
    #                     scheme, value = value.split('://')[:2]
    #                 splitValue = value.split(":")
    #                 host = splitValue[0]
    #
    #                 if len(splitValue) > 1:
    #                     port = filterStringValue(splitValue[1], "[0-9]")
    #
    #             # Avoid to add a static content length header to
    #             # headers and consider the following lines as
    #             # POSTed data
    #             if key.upper() == HTTP_HEADER.CONTENT_LENGTH.upper():
    #                 params = True
    #
    #             # Avoid proxy and connection type related headers
    #             elif key not in (HTTP_HEADER.PROXY_CONNECTION, HTTP_HEADER.CONNECTION, HTTP_HEADER.IF_MODIFIED_SINCE,
    #                              HTTP_HEADER.IF_NONE_MATCH):
    #                 headers.append((getUnicode(key), getUnicode(value)))
    #
    #             if kb.customInjectionMark in re.sub(PROBLEMATIC_CUSTOM_INJECTION_PATTERNS, "", value or ""):
    #                 params = True
    #
    #     data = data.rstrip("\r\n") if data else data
    #
    #     if getPostReq and (params or cookie or not checkParams):
    #         if not port and hasattr(scheme, "lower") and scheme.lower() == "https":
    #             port = "443"
    #         elif not scheme and port == "443":
    #             scheme = "https"
    #
    #         if conf.forceSSL:
    #             scheme = "https"
    #             port = port or "443"
    #
    #         if not host:
    #             errMsg = "invalid format of a request file"
    #             raise SqlmapSyntaxException(errMsg)
    #
    #         if not url.startswith("http"):
    #             url = "%s://%s:%s%s" % (scheme or "http", host, port or "80", url)
    #             scheme = None
    #             port = None
    #
    #         if not (conf.scope and not re.search(conf.scope, url, re.I)):
    #             yield (url, conf.method or method, data, cookie, tuple(headers))



