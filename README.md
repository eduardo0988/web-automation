# Slash web-automation

This repo contains automated test scripts designed within Slash and Selenium Webdriver for python.

## Configuration

- check out this repo on your machine
- from the checkout directory, install all required (requirements.txt) in the **virtual environment**

## Running a test script

Using the **terminal**, ensure your virtual environment is activated and simply use the following command:

`slash run path_to_test/test_name.py` to execute a single file

`slash run -f path_to_test_suite.txt` to execute a test suite

## Logs

1.  Slash's logs will be generated automatically in an entire directory hierarchy.
2.  Logs from Slash will be stored into each folder based on the the session name and test ID.
3.  Test's logs will be stored at same level as slash's logs (debug.log).
