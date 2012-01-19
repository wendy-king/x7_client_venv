# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011, X7 LLC.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import logging

from tank.notifier import strategy


class LoggingStrategy(strategy.Strategy):
    """A notifier that calls logging when called."""

    def __init__(self, conf):
        self.logger = logging.getLogger('tank.notifier.logging_notifier')

    def warn(self, msg):
        self.logger.warn(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)
