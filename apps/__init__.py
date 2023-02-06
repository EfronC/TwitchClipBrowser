# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from flask import Flask
from importlib import import_module
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator, validate_token, refresh_access_token
from twitchAPI.types import AuthScope, TwitchAuthorizationException, InvalidTokenException

async def init_twitch(auth_step=False):
    token = os.getenv('TWITCH_TOKEN')
    refresh = os.getenv('TWITCH_REFRESH')
    app_id = os.getenv('TWITCH_APP_ID')
    secret = os.getenv('TWITCH_SECRET')
    
    twitch = await Twitch(app_id, secret)
    target_scope = [AuthScope.BITS_READ]

    if (token and refresh) and not auth_step:
        try:
            await twitch.set_user_authentication(token, target_scope, refresh)
        except (TwitchAuthorizationException, InvalidTokenException) as error:
            token, refresh = await refresh_access_token(refresh, app_id, secret)
            print("New Token: ", token)
            print("New Refresh: ", refresh)
            await twitch.set_user_authentication(token, target_scope, refresh)

        return twitch, None
    else:
        auth = UserAuthenticator(twitch, target_scope, force_verify=False, url="http://localhost:3333/api/oauth/success/")
        return twitch, auth

def register_blueprints(app):
    for module_name in ('home','browser'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    return app
