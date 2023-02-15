from datetime import datetime

from django.contrib.contenttypes.models import ContentType

from actstream.managers import ActionManager, stream

class myActionManager(ActionManager):
    
    @stream
    def mystream(self, obj, verb='added', time=None):
        if time is None:
            time = datetime.now()
        return obj.actor_actions.filter(verb = verb, timestamp__lte = time)
