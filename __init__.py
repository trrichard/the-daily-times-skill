from mycroft import MycroftSkill, intent_file_handler


class TheDailyTimes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('times.daily.the.intent')
    def handle_times_daily_the(self, message):
        self.speak_dialog('times.daily.the')


def create_skill():
    return TheDailyTimes()

