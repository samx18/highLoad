# highLoad

A legacy python script to check the server load and post to Slack

## Usage

Call via cron

	*/5      *       *       *       *       /root/scripts/loadSlack.sh > /dev/null

Deploy via AWS Lambda

	t0-d0