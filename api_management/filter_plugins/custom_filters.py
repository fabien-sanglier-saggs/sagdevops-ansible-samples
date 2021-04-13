#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'wrap': self.wrap
        }

    def wrap(self, list):
        return [ "'" + x + "'" for x in list]