#encoding: UTF-8

import os
import re
import tweepy
import config
from random import randint
from IPython import embed # call embed() anywhere to debug code


def main():
  run_test()
  results = parse_results()
  post_results_in_twitter(results)


def post_results_in_twitter(results):
  status_message = mount_status(results)

  try:
    twitter = authenticate()
    twitter.update_status(status_message)
  except:
    print 'Error posting message in Twitter timeline (see config.py)'
  finally:
    print "Message: %s" % (status_message)

def run_test():
  os.system('speedtest-cli --simple > net.log')

def parse_results():
  log        = open('net.log')

  ping       = get_value(log.readline())
  down_speed = get_value(log.readline())
  up_speed   = get_value(log.readline())

  return [
    ping,
    down_speed,
    (down_speed * 100 / config.down_speed),
    up_speed,
    (up_speed * 100 / config.up_speed)
  ]

def get_value(line):
  return float(re.search('(\d+\.\d+)', line).group(0))

def authenticate():
  auth = tweepy.OAuthHandler(config.twitter_consumer_key, config.twitter_consumer_secret)
  auth.set_access_token(config.twitter_access_key, config.twitter_access_secret)
  return tweepy.API(auth)

def mount_status(results):
  return config.twitter_message % (
    results[1], # download speed
    results[2], # download (%)
    results[3], # upload speed
    results[4], # upload (%s)
    results[0], # ping
    final_message(results[2], results[4]) # random final message
  )

def satisfy(down, up, connection_status):
  check_valid_connection_status(connection_status)

  speeds = config.speeds[connection_status]
  up_speed, down_speed = speeds

  return (down > down_speed and up > up_speed)

def get_message(connection_status):
  check_valid_connection_status(connection_status)

  messages = config.messages[connection_status]
  message = messages[randint(0, (len(messages) -1))]

  return message

def check_valid_connection_status(connection_status):
  if not config.speeds.has_key(connection_status):
    raise ValueError("invalid connection_status: %s" % (connection_status))

  return True

def final_message(current_down, current_up):
  for connection_status in config.speeds.keys():
    if satisfy(current_down, current_up, connection_status):
      return get_message(connection_status)
    else:
      return get_message('shit')

main()
