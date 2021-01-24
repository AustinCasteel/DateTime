# -*- coding: utf-8 -*-
import datetime
import pytz
import time
from timezonefinder import TimezoneFinder
import calendar
import geocoder
import holidays
from naomi import plugin


class DateTime(plugin.SpeechHandlerPlugin):
    def intents(self):
        return {
            'DateTimeIntent': {
                'locale': {
                    'en-US': {
                        'templates': [
                            'WHAT TIME IS IT',
                            'WHAT TIME IS IT IN {}',
                            'WHAT IS THE DATE',
                            'TELL ME THE DAY OF THE WEEK',
                            'WHAT DAY IS {}',
                            'WHEN IS {}'
                        ]
                    }
                },
                'action': self.handle
            }
        }

    def handle(self, intent, mic):
        transcript = intent['input']

        if "WHAT TIME IS IT" in transcript not "WHAT TIME IS IT IN" in transcript:
            t = time.localtime()
            current_time = time.strftime("%H %M", t)
            mic.say("IT IS {}".format(current_time))
        
        if "WHAT TIME IS IT IN" in transcript:
            location = transcript[19:]
            geo = geocoder.osm(location)
            tzf = TimezoneFinder()
            timezone = tzf.timezone_at(lng=geo.lng, lat=geo.lat)
            datetime = datetime.now(timezone)
            mic.say("THE TIME IN {} IS ".format(transcript[19:]) + datetime.strftime("%H %M"))

        if "WHAT IS THE DATE" in transcript:
            today = date.today()
            date = today.strftime("%B %d, %Y")
            mic.say("TODAY IS {}".format(date))

        if "TELL ME THE DAY OF THE WEEK" in transcript:
            today = date.today()
            mic.say("TODAY IS {}".format(calendar.day_name[today.weekday()]))

        if "WHAT DAY IS" in transcript:
            holiday = transcript[12:]
            year = day.year
            for date in sorted(holidays.US(years=year).get_named(holiday).items()):
                mic.say(str(date[0]))
                break
            else:
                mic.say("ERROR FINDING HOLIDAY")
        
        if "WHEN IS" in transcript:
            holiday = transcript[8:]
            year = day.year
            for date in sorted(holidays.US(years=year).get_named(holiday).items()):
                mic.say(str(date[0]))
                break
            else:
                mic.say("ERROR FINDING HOLIDAY")