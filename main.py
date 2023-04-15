#!/usr/bin/env python3

import json, math, random
from typing import Tuple
from datetime import datetime
from os import system

import config
import tweepy

PING_SERVERS = [
    "1.1.1.1",
    "1.0.0.1",
    "8.8.8.8",
    "8.8.4.4",
]


def main():
    try:
        uptime = get_uptime()
        run_test()

        results = parse_results()
        post_results(uptime, results)

        write("Finished")
    except Exception as e:
        write(str(e), True)


def get_uptime() -> str:
    if is_online():
        now = int(datetime.now().strftime("%s"))

        with open(config.base_path + "uptime.log", "a+") as file:
            file.write("%d\n" % now)
            file.seek(0)
            timestamp = file.readline()

        first_online_timestamp = -now if timestamp == "" else int(timestamp)

        uptime = (now - first_online_timestamp) / (60 * 60)

        return "%d %s" % (uptime, "hora" if uptime == 1 else "horas")
    else:
        with open(config.base_path + "uptime.log", "w") as file:
            file.write("")
        raise Exception("There is no Internet connectivity")


def is_online() -> bool:
    write("Testing connectivity")
    for _ in range(10):
        ip = random.choice(PING_SERVERS)
        if system(f"ping {ip} -c 1 -W 5") == 0:
            return True
    return False


def run_test():
    write("Running SpeedTest")
    system(
        "speedtest --accept-license --accept-gdpr -f json > "
        + config.base_path
        + "results.log"
    )


def parse_results() -> Tuple[str, str, str, str, str, str]:
    write("Parsing Results")
    with open(config.base_path + "results.log") as file:
        data = json.loads(file.read())

    return (
        data["ping"]["latency"],
        data["download"]["bandwidth"] * 8e-6,
        data["download"]["bandwidth"] * 8e-6 / config.down_speed,
        data["upload"]["bandwidth"] * 8e-6,
        data["upload"]["bandwidth"] * 8e-6 / config.up_speed,
        data["result"]["url"],
    )


def post_results(uptime, results):
    twitter = authenticate()
    write("Posting on Twitter")
    twitter.create_tweet(text=mount_status(uptime, results))


def authenticate() -> tweepy.Client:
    write("Authenticating")
    return tweepy.Client(
        consumer_key=config.consumer_key,
        consumer_secret=config.consumer_secret,
        access_token=config.access_key,
        access_token_secret=config.access_secret,
    )


def mount_status(uptime, results) -> str:
    ping, down, down_ratio, up, up_ratio, url = results
    worst_ratio = min(down_ratio, up_ratio)
    return config.twitter_message.format(
        provider=config.provider,
        down=down,
        up=up,
        ping=ping,
        ratio=worst_ratio * 100,
        uptime=uptime,
        reaction=get_reaction(down_ratio, up_ratio, ping),
        url=url,
    )


def get_reaction(down_ratio, up_ratio, ping) -> str:
    if (
        ping > config.anatel["ping"]
        or down_ratio <= config.anatel["down_ratio"]
        or up_ratio <= config.anatel["up_ratio"]
    ):
        return config.messages["illegal"]

    messages = [
        config.messages["terrible"],
        config.messages["bad"],
        config.messages["mediocre"],
        config.messages["fair"],
        config.messages["great"],
        config.messages["awesome"],
    ]
    max_idx = len(messages) - 1

    # convert the worst_ratio within the range [worst_legal - 1.0] to [0 - number_of_messages]
    worst_ratio = min(down_ratio, up_ratio)

    worst_legal = min(config.anatel["down_ratio"], config.anatel["up_ratio"])
    best_legal = 1.0

    coefficient = (0 - max_idx) / (worst_legal - best_legal)
    idx = coefficient * (worst_ratio - worst_legal)

    message_idx = min(int(math.ceil(idx)), max_idx)

    return messages[message_idx]


def write(text, log=False):
    message = "%s - %s" % (timestamp(), text)
    print(message)

    if log:
        with open(config.base_path + "error.log", "a") as file:
            file.write("%s\n" % message)


def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


main()
