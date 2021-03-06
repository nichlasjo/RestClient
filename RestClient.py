#!/usr/bin/env python

import requests
import json
import sys
import io
import os
from optparse import OptionParser
from requests.auth import HTTPBasicAuth


def main(opts):
    if not opts.url or not opts.restcmd:
        p.error("to specify url and restcmd is minimum")

    url = opts.url
    username = opts.username
    password = opts.password
    restcmd = getattr(requests, opts.restcmd)
    jheader = {'Content-Type': 'application/json'}

    try:
        if opts.jsoncfg:
            jsoncfg = json.load(
                io.open(opts.jsoncfg, mode="r", encoding="utf-8"))
            r = restcmd(url, auth=HTTPBasicAuth(
                username, password), json=jsoncfg, verify=opts.tls)
        else:
            r = restcmd(url, auth=HTTPBasicAuth(
                username, password), headers=jheader, verify=opts.tls)

        if restcmd == requests.delete:
            print("\n")
            print("deleted %s with statuscode of %s") % (url, r.status_code)
        elif r.ok:
            jdata = json.loads(r.content)
            print("\n")
            print(json.dumps(jdata, indent=4, sort_keys=True))
        else:
            r.raise_for_status()
    except Exception as e:
        print(e)
        print(r.text)
        sys.exit(1)
    except:
        print ("Connection error")
        sys.exit(1)


if __name__ == '__main__':
    p = OptionParser(usage="usage: %prog [ -r post ] -U resturl -j jsonfile",
                     version="%prog 0.9")
    p.add_option("-u", "--user", dest="username", help="Username for restapi")
    p.add_option("-U", "--url", dest="url",
                 help="Url of the rest api: https://<fqdn>/<section>")
    p.add_option("-p", "--password", dest="password",
                 help="Password for restapi")
    p.add_option("-r", "--restcmd", dest="restcmd",
                 help="get, post, patch, or delete command")
    p.add_option("-j", "--jsoncfg", dest="jsoncfg", help="jsoncfg as file")
    p.add_option("-t", "--tls-verify", dest="tls", action="store_false", help="tls verify")
    (opts, args) = p.parse_args()
    main(opts)

