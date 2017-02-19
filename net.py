#encoding: UTF-8

from os import system
from re import search
from datetime import datetime

import tweepy
import pyping
import config

def main():
  try:
    uptime = get_uptime()
    run_test()

    results = parse_results()
    post_results(uptime, results)

    write('Finished')
  except Exception as e:
    write(e.message, True)

def get_uptime():
  if is_online():
    now = int(datetime.now().strftime('%s'))

    with open(config.base_path + 'uptime.log', 'a+') as file:
      file.write('%d\n' % now)
      file.seek(0)
      timestamp = file.readline()

    first_online_timestamp = - now if timestamp == '' else int(timestamp)

    uptime = (now - first_online_timestamp) / (60 * 60)

    return '%d %s' % (uptime, 'hora' if uptime == 1 else 'horas')
  else:
    with open(config.base_path + 'uptime.log', 'w') as file:
      file.write('')
    raise Exception('There is no Internet connectivity')

def is_online():
  write('Testing connectivity')
  for _ in range(10):
    if system('ping 8.8.8.8 -c 1 -W 5') == 0:
      return True
  return False

def run_test():
  write('Running SpeedTest')
  system('speedtest-cli --simple > ' + config.base_path + 'results.log')

def parse_results():
  write('Parsing Results')
  with open(config.base_path + 'results.log') as file:
    ping       = get_value(file.readline())
    down_speed = get_value(file.readline())
    up_speed   = get_value(file.readline())

  return [
    ping,
    down_speed,
    down_speed * 100 / config.down_speed,
    up_speed,
    up_speed * 100 / config.up_speed
  ]

def get_value(line):
  return float(search('(\d+\.\d+)', line).group(0))

def post_results(uptime, results):
  twitter = authenticate()
  write('Posting on Twitter')
  twitter.update_status(mount_status(uptime, results))

def authenticate():
  write('Authenticating')
  auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
  auth.set_access_token(config.access_key, config.access_secret)
  return tweepy.API(auth)

def mount_status(uptime, results):
  return config.twitter_message % (
    results[1], # Download speed
    # results[2], # Download percentage
    results[3], # Upload speed
    # results[4], # Upload percentage
    results[0], # Ping
    uptime,
    final_message(results[2], results[4])
  )

def final_message(down, up):
  if down > 105 or up > 110: return config.messages['awesome']
  elif down > 95 and up > 95: return config.messages['great']
  elif down > 90 and up > 90: return config.messages['fair']
  elif down > 85 and up > 85: return config.messages['mediocre']
  elif down > 70 and up > 70: return config.messages['bad']
  elif down > 60 and up > 60: return config.messages['terrible']
  else: return config.messages['shit']

def write(text, log = False):
  message = '%s - %s' % (timestamp(), text)
  print(message)

  if log:
    with open(config.base_path + 'error.log', 'a') as file:
      file.write('%s\n' % message)

def timestamp():
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

main()
