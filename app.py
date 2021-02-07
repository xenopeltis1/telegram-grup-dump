from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'



api_id =  #api id
api_hash = 'api_hash'
phone = 'numara

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))


chats = []
last_date = None
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             hash = 0,
             limit = 9999
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

print(bcolors.WARNING+"Hangi grubun data'sını çekmek istiyorsunuz?")
i=0
for g in groups:
    print(f"[ {str(i)} ] " + g.title)
    i+=1

g_index = input("Grubun numarasını girin: ")
target_group = groups[int(g_index)]

print('Fotoğraflar çekiliyor...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)


messages = client.get_messages(target_group, None, filter=InputMessagesFilterPhotos)

count = 0

for i in messages:
    dosya = i.download_media()
    count += 1
    print(bcolors.OKBLUE + f"[ {count} ] "+dosya+" indirildi." )

print(f"[ {count} ]"+ f" ADET RESİM DOSYASI {groups[int(g_index)].title} GRUBUNDAN BAŞARIYLA İNDİRİLDİ")
