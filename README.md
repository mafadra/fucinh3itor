## About Fucinh3itor:
Fucinh3itor is a Python tool made to enumate subdomains on a application. Currently (1.0 version) Fucinh3itor only uses crth.sh to get subdomains from target domain, except when it finds wildcard subdomains in a consult, then it will do brute force with a wordlist.

## Recommended Python Versions:
Fucinh3itor was build Python 3.9.8 version. It does not suport Python 2
- The recommend Python version for Python 3 is Python 3.9.x

## Dependencies:
To use Fucinh3itor, **termcolor**, **requests**, json, os, argparse, sys, datetime and time are required. The libs, json, os, argparse, sysm datetime and time are Python native libs, but **termcolor** and **requests** are not.
To install these libs, use requirements.txt file

- Installation on Linux: ```sudo pip install -r requirements.txt```

## Instalation:
```git clone https://github.com/mafadra/fucinh3itor```

## Usage:
| Short form | Long form | Description |
|:-------------------|:------------|:------------------|
| -d | --domain | Target domain to enumarate subdomains of|
| -s | --status-code | Status code filter |
| -sc | --subdomain-consult | Allow subdomain enumaration |
| -o | --output | Save consult in a output file (txt or json) |
| -h | --help | Show help message and exit |

### **Examples:**
- Specify target domain: ```python fucinh3itor.py -d/--domain targetdomain.tld```
- Only show subdomains with specific status code: ```python fucinh3itor.py -s 200 404```
- To activate subdomain consult: ```python fucinh3itor.py -sc/--subdomain-consult```
- Save consults in a output file (status code filter able if the user wants): ```python fucinh3itor.py -o/--output outputfile.txt or outputfile.json``` or ```python fucinh3itor.py -o/--output-file file.txt 200 404```
- Help message: ```python fucinh3itor.py -h/--help```

## Credits:
- [crt.sh](https://github.com/crtsh) - The crt.sh API allows querying public Certificate Transparency logs to obtain information about SSL/TLS certificates issued for domains and subdomains, as it captures certificates that include subdomains registered in their records

## Version:
**Current version is 1.0**
