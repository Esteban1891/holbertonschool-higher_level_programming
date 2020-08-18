# 0x10. Python - Network #0

## Overview
The goal of this project was to get us acquainted with how HTTP worked, what domains and subdomains were, what query strings were, what a URL is, what HTTP requests and responses look like, and how HTTP cookies work.

## Requirements
### Shell Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your scripts will be tested on Ubuntu 14.04 LTS
* All your scripts should be exactly three lines long (`wc -l` file should print 3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/bin/bash`
* All your files must be executable
* All `curl` commands must have the `-s` option

## Tasks
### Mandatory
**[0-body_size.sh](0-body_size.sh)** - the script takes in a URL, sends a request to it, and returns the size of the response body in bytes using `curl`
```
$ ./0-body_size.sh 0.0.0.0:5000
10
```

**[1-body.sh](1-body.sh)** - the script takes a URL, sends a `GET` request, and displays the body of `200` status code responses
```
$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
```

**[2-delete.sh](2-delete.sh)** - the script sends a `DELETE` request to a URL and displays the body of the response
```
$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
```

**[3-methods.sh](3-methods.sh)** - the script displays all HTTP methods that the server will accept
```
$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
```

**[4-header.sh](4-header.sh)** - script takes in a URL, sends a `GET` request with the header variable `X-DHKSchool-User-Id` sent with the value `98`
```
$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello DHK School!
```

**[5-post_params.sh](5-post_params.sh)** - script takes a URL, sends a `POST` request, and sends `email` variable with the value `hr@dhkschool.com` and `subject` with the value `I will always be here for PLD`.
```
$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: hr@dhkschool.com
    subject: I will always be here for PLD
```

**[6-peak.py](6-peak.py)** - Python script that finds a peak in a list of unordered integers
```
$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))

$ ./6-main.py
6
3
2
None
2
4
```

**[6-peak.txt](6-peak.txt)** - the time complexity of `6-peak.py`

### Advanced

**[100-status_code.sh](100-status_code.sh)** - script sends a request to a URL and displays only the status code of the response
```
$ ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200

$ ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
```

**[101-post_json.sh](101-post_json.sh)** - script sends a JSON `POST` request to a URL and displays the response
```
$ cat my_json_0
{
    "name": "John Doe",
    "age": 33
}

$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON

$ cat my_json_1
I'm a JSON! really!

$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON

$ cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}

$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
```

**[102-catch_me.sh](102-catch_me.sh)** - script sends a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message `You got me!`
```
$ ./102-catch_me.sh ; echo ""
You got me!
```



## Author :octocat:

[Esteban De La Hoz](https://www.linkedin.com/in/esteban-de-la-hoz-romero-b6270017b/) | [Twitter](https://twitter.com/Esteban18911) | [GitHub](https://github.com/Esteban18911)
