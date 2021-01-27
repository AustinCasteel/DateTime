# -*- coding: utf-8 -*-
import datetime
import pytz
import time
from timezonefinder import TimezoneFinder
import calendar
import geocoder
import holidays
from naomi import app_utils
from naomi import plugin
from pytz import timezone


class DateTime(plugin.SpeechHandlerPlugin):
    def intents(self):
        CurrentYear = datetime.datetime.today().year
        return {
            'TimeIntent': {
                'locale': {
                    'en-US': {
                        'keywords': {
                            'LocationKeyword': [
                                'Hawaii',
                                'New Zealand',
                                'Los Angeles',
                                'New York',
                                'Paris',
                                'London'
                            ]
                        },
                        'templates': [
                            'WHAT TIME IS IT',
                            'WHAT TIME IS IT IN {LocationKeyword}'
                        ]
                    }
                },
                'action': self.handleTime
            },
            'DateIntent': {
                'locale': {
                    'en-US': {
                        'templates': [                
                            'WHAT IS THE DATE',
                            'TELL ME THE DAY OF THE WEEK',
                            'WHAT DAY IS IT'
                        ]
                    }
                },
                'action': self.handleDate
            },
            'HolidayIntent': {
                'locale': {
                    'en-US': {
                        'keywords': {
                            'HolidayKeyword': holidays.US(years=[CurrentYear]).values()
                        },
                        'templates': [
                            'WHAT DAY IS {HolidayKeyword}',
                            'WHEN IS {HolidayKeyword}'
                        ]
                    }
                },
                'action': self.handleHoliday
            }
        }

    def handleTime(self, intent, mic):
        print("handleTime")
        print(intent)
        if 'LocationKeyword' in intent['matches']:
            for location in intent['matches']['LocationKeyword']:
                geo = geocoder.osm(location)
                tzf = TimezoneFinder()
                tz = tzf.timezone_at(lng=geo.lng, lat=geo.lat)
                now = datetime.datetime.now(tz=timezone(tz))
                if now.minute == 0:
                    fmt = self.gettext("IT IS {t:%l} {t:%p} IN {l} RIGHT NOW.")
                else:
                    fmt = self.gettext("IT IS {t:%l}:{t:%M} {t:%p} IN {l} RIGHT NOW.")
                mic.say(fmt.format(l=location, t=now))
        else:
            now = datetime.datetime.now(tz=app_utils.get_timezone())
            if now.minute == 0:
                fmt = self.gettext("IT IS {t:%l} {t:%p}.")
            else:
                fmt = self.gettext("IT IS {t:%l}:{t:%M} {t:%p}.")
            mic.say(fmt.format(t=now))

        return True
    
    def handleDate(self, intent, mic):
        print("handleDate")
        print(intent)
        today = datetime.datetime.today()
        mic.say(self.gettext("TODAY IS {}").format(today.strftime("%A, %B %d, %Y")))
        return True
    
    def handleHoliday(self, intent, mic):
        print("handleHoliday")
        print(intent)
        CurrentYear = datetime.datetime.today().year
        if 'HolidayKeyword' in intent['matches']:
            for holiday in intent['matches']['HolidayKeyword']:
                dateslist = holidays.US(years=[CurrentYear]).get_named(holiday)
                if len(dateslist):
                    for date in dateslist:
                        if(date < datetime.date.today()):
                            mic.say(self.gettext("THIS YEAR, {} WILL BE ON {}").format(holiday, str(date)))
                        elif(date == datetime.date.today()):
                            mic.say(self.gettext("TODAY IS {}").format(holiday))
                        else:
                            mic.say(self.gettext("THIS YEAR, {} WILL BE ON {}").format(holiday, str(date)))
                else:
                    mic.say(self.gettext("ERROR FINDING HOLIDAY"))
        return True

    def handle(self):
        
        if "WHAT TIME IS IT IN" in transcript:
            location = transcript[19:]
            geo = geocoder.osm(location)
            tzf = TimezoneFinder()
            timezone = tzf.timezone_at(lng=geo.lng, lat=geo.lat)
            datetime = datetime.now(timezone)
            mic.say("THE TIME IN {} IS ".format(transcript[19:]) + datetime.strftime("%H %M"))
        elif "WHAT TIME IS IT" in transcript:
            t = time.localtime()
            current_time = time.strftime("%H %M", t)
            mic.say("IT IS {}".format(current_time))

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
