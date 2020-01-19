# Overview
##Test Description
Search for products on Brooks Running website using search box , then Add a product to cart.

##Test environment
- Selenium webdriver using Python 3
- Test is running on Chrome using Chrome Webdriver.
- Testing desktop version of the website 1440x1080 size

# Usage
## Installation
Uses virtualenv for python dependencies. Activate and install by running
1. Install chrome webdriver to `%USERPROFILE%\SeleniumWebDrivers\chromedriver.exe`
1. Install dependencies via pip
```
> cd BrooksRunningTesting\
> venv\Scripts\activate
> pip install -r requirements.txt
```

## Running Tests
Execute via nose2 test framework
```

(venv) (base) BrooksRunningTesting>nose2

DevTools listening on ws://127.0.0.1:51240/devtools/browser/d979ec96-3f26-479e-ad19-53992d8d74b5
.
----------------------------------------------------------------------
Ran 1 test in 23.346s

OK
```
