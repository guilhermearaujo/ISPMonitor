# ISP Monitor
_As seen on http://www.twitter.com/avivohoje_ (formerly @anethoje)

ISP Monitor monitors your Internet speeds and reports the results to your Twitter account.

# Dependencies
* [speedtest-cli](https://github.com/sivel/speedtest-cli)
* [tweepy](https://github.com/tweepy/tweepy)
* Requires a [Twitter Developer account](http://developer.twitter.com)

# Installing
1. Clone this repo: `$ git clone git@github.com:guilhermearaujo/ISPMonitor.git`
2. Run `make dependencies` to install the dependencies. The official Ookla Speedtest CLI tool is also required. See how to [install it on your platform](https://www.speedtest.net/apps/cli).
3. Add your Twitter Credentials and Internet speeds to `config.py` (hint: there's a `config.sample.py`!)
4. Schedule the script using Cron:  
  `$ crontab -e`  
  Add the line:  
  `0 * * * * /path/to/script/main.py`  
**Make sure your Cron's PATH includes the `speedtest` path** ([see how](http://stackoverflow.com/a/2409369/1262783))

# Using
Wait and check your Twitter account periodically.

# License

ISPMonitor is released under the WFTPL license. See LICENSE for details.
