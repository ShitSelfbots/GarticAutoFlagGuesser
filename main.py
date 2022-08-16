import discum, time, flagpy, random, json
import os

jsonData = json.load(open('config.json', 'r'))

class gartic:
      client = discum.Client(token = os.environ['TOKEN'] or jsonData['clientToken'], log = False)
      client

@gartic.client.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:
       print ('[GARTIC] | Client Online, Listening For Gartic Events')

@gartic.client.gateway.command
def on_message(resp):
    if resp.event.message:
       if True:
          message = resp.parsed.auto()

       try:
          if message['author']['username'] == 'GarticBOT':
             if 'g.restart' in message['content']:
                 if jsonData['automaticRestart'] == True:
                    gartic.client.sendMessage(message['channel_id'], 'g.restart')
                    gartic, print('[GARTIC] | Restarting Game')
               
             if 'embeds' in str(message):
                 if message['embeds'][0]['author']['name'] == 'INITIALIZING GARTIC ON DISCORD...':
                    print('[GARTIC] | Event Found')
                    print
                 else:
                     if 'LEVEL' in message['embeds'][0]['author']['name']:
                         print('[GARTIC] | Gartic Level Found')
                         try:
                           time.sleep(jsonData['guessDelay'])
                           gartic.client.sendMessage(message['channel_id'], flagpy.identify(message['embeds'][0]['image']['url']).replace('The', ''))
                           gartic, print('[GARTIC] | Sent Guess')
                         except:
                            print('[GARTIC] | Couldn\'t Get Guess')
                     else:
                        if '30 SECONDS LEFT TO GUESS' in message['embeds'][0]['author']['name'] and jsonData['guessAfterCountdown'] == True:
                            print('[GARTIC] | 30 Seconds Left, Resending Guess')
                            try:
                              time.sleep(jsonData['guessDelay'])
                              gartic.client.sendMessage(message['channel_id'], flagpy.identify(message['embeds'][0]['image']['url']).replace('The', ''))
                              gartic, print('[GARTIC] | Sent Guess')
                            except:
                              print('[GARTIC] | Couldn\'t Get Guess')
                        else:
                           if 'GAME OVER' in message['embeds'][0]['author']['name']:
                               gartic.client.sendMessage(message['channel_id'], random.choice(['Fuck', 'Rigged Game']))
                           else:
                              if 'TEAM RANKING' in message['embeds'][0]['author']['name']:
                                  try:
                                    print('[GARTIC] | Current Level | %s' % (message['embeds'][0]['fields'][0]['value'].replace('Level ', '')))
                                  except:
                                     pass
                              
       except:
          pass

gartic.client.gateway.run()
