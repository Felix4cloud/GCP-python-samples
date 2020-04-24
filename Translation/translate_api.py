from google.cloud import translate_v2 as translate
import os,sys
import time



# Instantiates a client for V2 client
translate_client = translate.Client()

# The target language
source = 'en'
target = 'zh'

fp = open(u"hello_world.txt", 'r')
# Translates some text into Russian
for line in fp.readlines():
  pretime = time.time()
  text = line.strip()
  translation = translate_client.translate(
    text,
    source_language=source,
    target_language=target)
  print(u'{}\t{}\t{}'.format(text, translation['translatedText'], time.time() - pretime))
