# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.


# TODO: Change "Template" to a unique name for your skill
class LogSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(LogSkill, self).__init__(name="LogSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0

        
        
    def text2int(textnum, numwords={}):
        if not numwords:
          units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
          ]

          tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

          scales = ["hundred", "thousand", "million", "billion", "trillion"]

          numwords["and"] = (1, 0)
          for idx, word in enumerate(units):    numwords[word] = (1, idx)
          for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
          for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

        current = result = 0
        for word in textnum.split():
            if word not in numwords:
              raise Exception("Illegal word: " + word)

            scale, increment = numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0

        return result + current        
        
        
        
        
        
        
    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("").require("Hello").require("World"))
    def handle_log_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog
        self.speak_dialog("hello.world")

        # write to log
        f = open("/home/matthew/Desktop/mycroft.log", "w+")
        z = self.text2int(message)
        f.write(str(z))
        f.close()


    @intent_handler(IntentBuilder("").require("Count").require("Dir"))
    def handle_count_intent(self, message):
        if message.data["Dir"] == "up":
            self.count += 1
        else:  # assume "down"
            self.count -= 1
        self.speak_dialog("count.is.now", data={"count": self.count})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False
    

    
    

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return LogSkill()
