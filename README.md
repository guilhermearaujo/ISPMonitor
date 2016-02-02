# ISP Monitor
_As seen on http://www.twitter.com/anethoje_

ISP Monitor monitors your Internet speeds and reports the results to your Twitter account.

# Dependencies
* [speedtest-cli](https://github.com/sivel/speedtest-cli)
* [tweepy](https://github.com/tweepy/tweepy)
* Requires a [Twitter Developer account](http://dev.twitter.com)

# Installing
1. Clone this repo: `$ git clone git@github.com:guilhermearaujo/ISPMonitor.git`
2. Add your Twitter Credentials and Internet speeds to `config.py` (hint: there's a `config.py.sample`!)
3. Schedule the script using `cron`:  
  `$ crontab -e`  
  Add the line:  
  `0 */1 * * * python /path/to/script/net.py`

# Using
Wait and check your Twitter account periodically.

# License

Action Button is released under the WFTPL license. See LICENSE for details.
