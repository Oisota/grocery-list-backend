#!/bin/bash

#
# This is a git post-receive hook that deploys the application.
#

APP="grocery-list-api"
GIT_DIR="/home/derek/$APP.git"
APP_DIR="/opt/apps/$APP"

UWSGI_CONFIG="/opt/apps/$APP/config/uwsgi.ini"
UWSGI_APPS_AVAILABLE="/etc/uwsgi/apps-available"
UWSGI_APPS_ENABLED="/etc/uwsgi/apps-enabled"

while read oldrev newrev ref
do
	# only checking out the master (or whatever branch you would like to deploy)
	if [[ $ref =~ .*/master$ ]]; then
		echo "Master ref received.  Deploying master branch to production..."
		git --work-tree="$APP_DIR" --git-dir="$GIT_DIR" checkout -f

		# link uwsgi config
		echo "Updating uWSGI config..."
		cp $UWSGI_CONFIG "$UWSGI_APPS_AVAILABLE/$APP.ini"
		ln -sf "$UWSGI_APPS_AVAILABLE/$APP.ini" "$UWSGI_APPS_ENABLED/$APP.ini"
	else
		echo "Ref $ref successfully received. Doing nothing: only the master branch may be deployed on this server."
	fi
done
