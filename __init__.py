from mycroft import MycroftSkill, intent_file_handler


class MycloudMusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('music.mycloud.intent')
    def handle_music_mycloud(self, message):
        self.speak_dialog('music.mycloud')


def create_skill():
    return MycloudMusic()

