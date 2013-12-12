Bitminter-Logger
================

This package is a simple python app for logging Bitminter and MtGox info to log files.  One can easily then feed the data into something like Splunk for further analysis/pretty charts.

Quick Setup
===========
Clone the repo
```
$ cd your_code_folder
$ git clone https://github.com/adewinter/bitminter-logger.git
$ pip install requests #this is required
$ nano bitminter.py  #Make sure to add your own API key and SECRET key, otherwise you'll get my stats :)
$ python bitminter.py
```
This will immediately start logging your mining performance on the Bitminter pool to a file named `bitminter.log`.

Similarly, you can pull MtGox ticker data:

```
$ python mtgoxticker.py
```
This will generate a file called `mtgoxticker.log` containing ticker information in JSON format.


Note
====
The log data is formatted for ease of use in [Splunk](http://www.splunk.com/).  What this essentially means is that everything is a key-value pair using the `=` char for pairing.  Pairs are space (' ') separated.  In both log files, that essentially amounts to one pair: `Request={JSON_BLOB}` with some timestamp information at the start of the line.

Recommendations
===============
Run these puppies in Screen so that they can continue to run in the background with minimal fuss.


Example Output
==============
After adding the data to Splunk, I was able to quickly generate the following dashboard:

![Example Splunk Dashboard](http://adewinter.github.io/bitminter-logger/images/mining_dash.png)
