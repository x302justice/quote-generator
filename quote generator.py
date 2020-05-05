#file setup and importing modules
file = open("output.txt","w+")
import random
#lists
quotes = ["god is dead and we have killed him","i'm getting a turBONER","shut the fuck up, giorno","god has been dead for a long time","i'm going to be the guy who burns your house down using explosive lemons","i don't eat because i like eating, i eat because i like eating but still i like eating less than i like doing drunk car surfing at 2 am in the night","Who was the mf who ate a raw bat?","That's more cursed than black polnareff","give me your tonsils","holy shit i just realised at the end of this i'll have a list of quotes longer than the ammount of google search traffic that happens every year, is my hard drive even big enough to support that? jesus fucking christ.","“derek how was the loli party?”"]
quoted = ["michael reeves","michael reeves in dingding poster form","giorno","abbachio","penguinz0","x302justice","someone on discord","x302justice in his mind","cave motherfucking jonson","someone in the class of someone on discord","my friends neighbours dogs cousins owners bosses bosses local pharmacy owner"]
#writing to a file
file.write(random.choice(quotes)),"\n-"
file.write(random.choice(quoted))