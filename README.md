# SadTopic

Silly script to set the topic of a Hipchat room to the most recent tweet from a specific user.

The [@SadServer](https://twitter.com/sadserver) account inspired the name, and was the account which prompted me to write this.

## Configuration

You need to create a file `vars.sh` with some environment variables inside, an example is below:

```
export CONSUMER_KEY='.....'
export CONSUMER_SECRET='....'
export ACCESS_TOKEN='....'
export ACCESS_TOKEN_SECRET='....'
export HC_ROOM_ID=....
export HC_SERVER="...."
export HC_TOKEN='....'
export TWITTER_USER="sadserver"
```

Some explanation:

* `CONSUMER_KEY` you need to register this app with [Twitter](http://developer.twitter.com/), once you have done so put the consumer key here.
* `CONSUMER_SECRET` same as above.
* `ACCESS_TOKEN` Register an instance of this app against your twitter account and put the token here.
* `ACCESS_TOKEN_SECRET` same as above.
* `HC_ROOM_ID` Numerical ID of the Hipchat Room to set the topic of
* `HC_SERVER` Server URL for your Hipchat server
* `HC_TOKEN` Your Hipchat API token
* `TWITTER_USER` Twitter username to check

## Running

After creating `vars.sh` run with the `run.sh`, possibly from cron:

```
% bash run.sh
Latest tweet=How high were you when you green lit this deployment?
Current topic=foo
Topic doesn't match, setting to: How high were you when you green lit this deployment?
```

Or if the topic doesn't need setting because it is already set to the current tweet:
```
% bash run.sh
Latest tweet=How high were you when you green lit this deployment?
Current topic=How high were you when you green lit this deployment?
Topic is already set to latest tweet, ignoring
```

## Requirements

Uses the following Python libs (and their deps.):

* [HypChat](https://github.com/RidersDiscountCom/HypChat/)
* [python-twitter](https://github.com/bear/python-twitter)
