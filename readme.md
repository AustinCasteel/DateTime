---
id: date-time
label: Date Time
title: Date Time - Speechhandler
type: speechhandlers
description: "Have Naomi tell you the date or time"
source: https://github.com/austincasteel/DateTime/blob/master/readme.md
meta:
  - property: og:title
    content: "Date Time - Speechhandler"
  - property: og:description
    content: "Have Naomi tell you the date or time"
---

# Date Time - Speechhandler

Naomi can tell you the Date, the local time as well as time somewhere else in the world, and when a holiday is.

Intents:

- What Time is it?
- What Time is it in "LOCATION"?
- What is the Date?
- Tell me the Day of the Week.
- What Day is "HOLIDAY"?
- When is "HOLIDAY"?

```
>> My name is Naomi.                                                           
>> How can I be of service?                                                    
<  <noise>                                                                     
<  ['NAOMI WHAT IS NAOMI WHAT IS']                                             
<< ['ONE WILL TIME IS IT NAOMI TIME IS ']                                      
TimeIntent 0.9357799927709994
handleTime
{'action': <bound method DateTime.handleTime of <Date Time_1_0.DateTime object at 0x7f5e3618c160>>, 'input': 'ONE WILL TIME IS IT NAOMI TIME IS ', 'matches': {}, 'score': 0.9357799927709994, 'intent': 'TimeIntent'}
>> IT IS  8:58 AM.                                                             
<  ['NAOMI WHAT KITTENS IT ON']                                                
<< ['NAOMI WHAT TIME IS IT IN LONDON']                                         
TimeIntent 0.9855546416454907
handleTime
{'action': <bound method DateTime.handleTime of <Date Time_1_0.DateTime object at 0x7f5e3618c160>>, 'input': 'NAOMI WHAT TIME IS IT IN LONDON', 'matches': {'LocationKeyword': ['LONDON']}, 'score': 0.9855546416454907, 'intent': 'TimeIntent'}
>> IT IS  1:59 PM IN LONDON RIGHT NOW.                                         
<  ['NAOMI WHAT IS']                                                           
<< ['NAOMI WHAT DAY IS IT']                                                    
DateIntent 0.5276958881263923
handleDate
{'action': <bound method DateTime.handleDate of <Date Time_1_0.DateTime object at 0x7f5e3618c160>>, 'input': 'NAOMI WHAT DAY IS IT', 'matches': {}, 'score': 0.5276958881263923, 'intent': 'DateIntent'}
>> TODAY IS Wednesday, January 27, 2021                                                   
<  ['NAOMI WHAT WHICH']                                                        
<< ['NAOMI ONE THANKSGIVING']                                                  
HolidayIntent 1.0
handleHoliday
{'action': <bound method DateTime.handleHoliday of <Date Time_1_0.DateTime object at 0x7f5e3618c160>>, 'input': 'NAOMI ONE THANKSGIVING', 'matches': {'HolidayKeyword': ['THANKSGIVING'], 'NumberKeyword': ['NAOMI ONE THANKSGIVING']}, 'score': 1.0, 'intent': 'HolidayIntent'}
>> THIS YEAR, THANKSGIVING WILL BE ON 2021-11-25                               
<  ['NAOMI OF']                                                                
<< ['NAOMI SHUTDOWN']                                                          
ShutdownIntent 1.0
>> I'm shutting down.
```

<EditPageLink/>
