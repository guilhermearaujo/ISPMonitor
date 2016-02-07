# ISP Monitor
_As seen on http://www.twitter.com/anethoje_

ISP Monitor monitors your Internet speeds and reports the results to your Twitter account.

# Dependencies
* [speedtest-cli](https://github.com/sivel/speedtest-cli)
* [tweepy](https://github.com/tweepy/tweepy)
* [pyping](https://github.com/certator/pyping)
* Requires a [Twitter Developer account](http://dev.twitter.com)

# Installing
1. Clone this repo: `$ git clone git@github.com:guilhermearaujo/ISPMonitor.git`
2. Add your Twitter Credentials and Internet speeds to `config.py` (hint: there's a `config.py.sample`!)
3. Schedule the script using Cron:  
  `$ crontab -e`  
  Add the line:  
  `0 * * * * python /path/to/script/net.py`  
**Make sure your Cron's PATH includes the `speedtest-cli` path** ([see how](http://stackoverflow.com/a/2409369/1262783))

# Using
Wait and check your Twitter account periodically.

# License

ISPMonitor is released under the WFTPL license. See LICENSE for details.
