class Handler:
    priority = -1;

    # Array for funny naughty words
    curses = ["homo", "dildo", "scrub", "penishole", "fag",
    "madman", "refugee", "immigrant", "nigger", "shitskin",
    "scrotum", "banaan", "equine vaginal cavity", "vagina",
    "punk", "bag", "furry", "error", "fig", "noob", "busta"]

    def __init__(self, brain):
        self.brain = brain; #brain is not used in this example, but it is usefull if you want i.e the name of the bot


    def canHandle(self, msg):
        msg.text = ''

        if(msg.command == 'PRIVMSG'):
            # Shut up if
            if(msg.contains('shut up') and msg.contains(self.brain.botnick)):
                msg.text = 'fuck off';
                return True;

            # Channel if
            if(msg.contains('http://') and msg.contains('youtu')):
                msg.text = 'only on my channel';
                return True;

            # Funny reply
            for curse in self.curses:
                if (msg.contains(curse) and msg.contains("you")):
                    if msg.contains("fuck"): # If it has fuck, add some fucking
                        msg.text = "yeah you fucking " + curse;
                        return True;
                    else:
                        msg.text = "yeah you " + curse;
                        return True;

        return False;


    def handle(self, msg, resp):
        resp.send(msg.text, msg.re());
