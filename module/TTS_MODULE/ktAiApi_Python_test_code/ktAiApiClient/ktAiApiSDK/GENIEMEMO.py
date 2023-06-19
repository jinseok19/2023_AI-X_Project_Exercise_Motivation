from __future__ import absolute_import

import json
import base64
import os
import sys

try:
    # Python 3.x
    from configparser import ConfigParser
except ImportError:
    # Python 2.x
    from ConfigParser import SafeConfigParser as ConfigParser
config = ConfigParser()
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'server.config'))
config.read(config_path)

import HttpUtils
HttpUtils = HttpUtils.HttpUtils()

# Decorator
def constant(func):
    def func_set(self, value):
        raise TypeError

    def func_get(self):
        return func()
    return property(func_get, func_set)

class GENIEMEMO:
    @constant
    def VERSION_MAJOR():
        return 1

    @constant
    def VERSION_MINOR():
        return 0

    @constant
    def VERSION_BUILD():
        return 0

    @constant
    def URL_GENIEMEMO():
        return "/v2/genieMemo"
    
    @constant
    def URL_GENIEMEMOASYNC():
        return "/v2/genieMemoAsync"

    @constant
    def URL_GENIEMEMOQUERY():
        return "/v2/genieMemoQuery"

    def CODE_NAME(self):
        return "GENIEMEMO" + str(self.VERSION_MAJOR) + "." + str(self.VERSION_MINOR) + "." + str(self.VERSION_BUILD)

    def TAG(self):
        return self.CODE_NAME()

    def __init__(self):
        self.service_url = ""
        self.client_key = ""
        self.timestamp = ""
        self.signature = ""
        strUrl = "https://" + config.get('server', 'host') + ":" + config.get('server', 'http_port')
        self.setServiceURL(strUrl)

    def setServiceURL(self, entrypoint):
        self.service_url = entrypoint

    def setAuth(self, clientKey, clientId, clientSecret):

        if not clientKey or not clientId or not clientSecret:
            return

        self.client_key = clientKey
        self.timestamp = HttpUtils.getTimestamp()
        self.signature = HttpUtils.makeSignature(self.timestamp, clientId, clientSecret)

    def requestGENIEMEMO(self, audioData, callKey, lastYn, callIndex):
        result_json = {}

        try:
            metdata_json_object = {}
            metdata_json_object["callKey"] = callKey
            metdata_json_object["callIndex"] = callIndex
            metdata_json_object["lastYn"] = lastYn
            strUrl = self.service_url + self.URL_GENIEMEMO

            json_object = {}
            json_object[HttpUtils.REQUEST_PARAMETER_X_CLIENT_KEY] = self.client_key
            json_object[HttpUtils.REQUEST_PARAMETER_X_AUTH_TIMESTAMP] = self.timestamp
            json_object[HttpUtils.REQUEST_PARAMETER_X_CLIENT_SIGNATURE] = self.signature

            response = HttpUtils.requestMultipart(strUrl, json_object, metdata_json_object, audioData)

            if response[HttpUtils.RESPONSE_STATUS_CODE] == 301:
                entrypoint = HttpUtils.setHttpEntrypoint(json.loads(response[HttpUtils.RESPONSE_RESULT]))
                self.setServiceURL('https://' + entrypoint)
                strUrl = self.service_url + self.URL_GENIEMEMO
                return HttpUtils.requestMultipart(strUrl, json_object, metdata_json_object, audioData)
            else:
                return response

        except Exception as e:
            return

    def requestGENIEMEMOASYNC(self, audioData, callKey):
        result_json = {}

        try:
            metdata_json_object = {}
            metdata_json_object["callKey"] = callKey
            strUrl = self.service_url + self.URL_GENIEMEMOASYNC

            json_object = {}
            json_object[HttpUtils.REQUEST_PARAMETER_X_CLIENT_KEY] = self.client_key
            json_object[HttpUtils.REQUEST_PARAMETER_X_AUTH_TIMESTAMP] = self.timestamp
            json_object[HttpUtils.REQUEST_PARAMETER_X_CLIENT_SIGNATURE] = self.signature

            response = HttpUtils.requestMultipart(strUrl, json_object, metdata_json_object, audioData)

            if response[HttpUtils.RESPONSE_STATUS_CODE] == 301:
                entrypoint = HttpUtils.setHttpEntrypoint(json.loads(response[HttpUtils.RESPONSE_RESULT]))
                self.setServiceURL('https://' + entrypoint)
                strUrl = self.service_url + self.URL_GENIEMEMOASYNC
                return HttpUtils.requestMultipart(strUrl, json_object, metdata_json_object, audioData)
            else:
                return response

        except Exception as e:
            return
            
    def queryGENIEMEMOASYNC(self, callKey, callIndex):

        try:
            metdata_json_object = {}
            metdata_json_object["callKey"] = callKey
            metdata_json_object["callIndex"] = callIndex

            strUrl = self.service_url + self.URL_GENIEMEMOQUERY

            json_object = {}
            json_object[HttpUtils.REQUEST_PARAMETER_X_CLIENT_KEY] = self.client_key
            json_object[HttpUtils.REQUEST_PARAMETER_X_AUTH_TIMESTAMP] = self.timestamp
            json_object[HttpUtils.REQUEST_PARAMETER_X_CLIENT_SIGNATURE] = self.signature

            return HttpUtils.requestPost(strUrl, json_object, metdata_json_object)

        except Exception as e:
            return    