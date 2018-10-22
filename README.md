# RestClient.py
* Rest api client for get, put delete, patch operations.

## Usage:
```
Usage: RestClient.py [ -r post ] -U resturl -j jsonfile

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -u USERNAME, --user=USERNAME
                        Username for restapi
  -U URL, --url=URL     Url of the rest api: https://'<fqdn>'/'<section>'
  -p PASSWORD, --password=PASSWORD
                        Password for restapi
  -r RESTCMD, --restcmd=RESTCMD
                        get, post, patch, or delete command
  -j JSONCFG, --jsoncfg=JSONCFG
                        jsoncfg as file
```

## POST
RestClient.py -r post -U https://reqres.in/api/login -j jsondata.json

_jsondata.json is a file with below content._

```
{
    "email": "peter@klaven",
    "password": "cityslicka"
}
```

RestClient.py -r post -U https://reqres.in/api/login -j jsondata.json

_response should be._

```
{
    "token": "QpwL5tke4Pnpja7X"
}
```

## GET
RestClient.py -r get -U https://reqres.in/api/users/2

_response should be._

```
{
    "data": {
        "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg", 
        "first_name": "Janet", 
        "id": 2, 
        "last_name": "Weaver"
    }
}
```

## DELETE
RestClient.py -r delete -U https://reqres.in/api/users/2

_response should be._


```
deleted https://reqres.in/api/users/2 with statuscode of 204
```

## PATCH
RestClient.py -r patch -U https://reqres.in/api/login -j jsondata.json

_jsondata.json is a file with below content._

```
{
    "name": "morpheus",
    "job": "zion resident"
}
```

_response should be something like (date/time will differ)._

```
{
    "job": "zion resident", 
    "name": "morpheus", 
    "updatedAt": "2018-10-17T12:12:24.878Z"
}
```

## Note:
To specify url and restcmd is minimum

## About:
Minimal rest api client

## License:
Copyright 2018 Nichlas Ekman

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


