import peforth
import itchat
from itchat.content import * # TEXT PICTURE 等 constant 的定義
    # Failed in compyle command : import * only allowed at module level 
    # 因此本程式適合用 .py 直接執行
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def _(msg):
    peforth.ok('notGrupChat> ',loc=locals(),cmd=':> [0] inport cr')
    msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def _(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def _(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def _(msg):
    peforth.ok('isGrupChat> ',loc=locals(),cmd=':> [0] inport cr')
    # if msg.isAt:
    msg.user.send(u'@%s\u2005I received: %s' % (
        msg.actualNickName, msg.text))

itchat.auto_login(True)  # hotReload=True
itchat.run(True, blockThread=True) # debug=True 

peforth.ok('itChat> ',loc=locals(),cmd=':> [0] inport cr')


'''
[x] 用 PC client 視訊或語音時，itchat 端就會斷掉。
    itchat.run(True, blockThread=True) 經 blockThread=True 就可以避免
[x] isGroupChat> 與最後的 itChat> 交替出現, 一 exit 就整個結束
    經 blockThread=True --> 果然就好了！！！
[x] debug isGroupChat 時，發現 function name 都是 text_reply() 
    decorator 裡好像這個無所謂，其實是個 anonymous function。
[x] 不會 echo chatroom 的 message <== bug!
    RI: msg.isAt 是 False !! 所以沒反應。 --> FP: 不考慮 msg.isAt 即可。
    --> 比對普通 chat 與 GroupChat 的 msg ...... 
    isGroupChat> msg . cr
        {'MsgId': '1422233572015927974',
        'FromUserName': '@@26536008f1c1307c892640411bf7f60ffd2a3feb138ed6591e65e4fe7541708e',
        'ToUserName': '@9f15931b5d2a9ea59d4c5e220e079c5574b036939a4300c985ae83094d0b8250',
        'MsgType': 1,
        'Content': '22',
        'Status': 3,
        'ImgStatus': 1,
        'CreateTime': 1511086807,
        'VoiceLength': 0,
        'PlayLength': 0,
        'FileName': '',
        'FileSize': '',
        'MediaId': '',
        'Url': '',
        'AppMsgType': 0,
        'StatusNotifyCode': 0,
        'StatusNotifyUserName': '',
        'RecommendInfo': {'UserName': '',
            'NickName': '',
            'QQNum': 0,
            'Province': '',
            'City': '',
            'Content': '',
            'Signature': '',
            'Alias': '',
            'Scene': 0,
            'VerifyFlag': 0,
            'AttrStatus': 0,
            'Sex': 0,
            'Ticket': '',
            'OpCode': 0},
        'ForwardFlag': 0,
        'AppInfo': {'AppID': '',
            'Type': 0},
        'HasProductId': 0,
        'Ticket': '',
        'ImgHeight': 0,
        'ImgWidth': 0,
        'SubMsgType': 0,
        'NewMsgId': 1422233572015927974,
        'OriContent': '',
        'ActualNickName': 'hcchen5600',  <---- isGroupChat only 
        'IsAt': False,                   <----- isGroupChat only
        'ActualUserName':                <----- isGroupChat only
            '@102dffe8deaaa7160fae7db1214b0bf69285399c0e94bbb35bb5457cde76b001',
        'User': 
            <Chatroom:                   <----- isGroupChat only 
                {'MemberList': 
                    <ContactList: 
                        [
                            <ChatroomMember: {'MemberList': <ContactList: []>,
                                'Uin': 0,
                                'UserName': '@9f15931b5d2a9ea59d4c5e220e079c5574b036939a4300c985ae83094d0b8250',
                                'NickName': '網路分享小寶貝',
                                'AttrStatus': 33558565,
                                'PYInitial': '',
                                'PYQuanPin': '',
                                'RemarkPYInitial': '',
                                'RemarkPYQuanPin': '',
                                'MemberStatus': 0,
                                'DisplayName': '',
                                'KeyWord': ''}
                            >,
                            <ChatroomMember: {'MemberList': <ContactList: []>,
                                'Uin': 0,
                                'UserName': '@102dffe8deaaa7160fae7db1214b0bf69285399c0e94bbb35bb5457cde76b001',
                                'NickName': 'hcchen5600',
                                'AttrStatus': 33788007,
                                'PYInitial': '',
                                'PYQuanPin': '',
                                'RemarkPYInitial': '',
                                'RemarkPYQuanPin': '',
                                'MemberStatus': 0,
                                'DisplayName': '',
                                'KeyWord': ''}
                            >,
                            <ChatroomMember: {'MemberList': <ContactList: []>,
                                'Uin': 0,
                                'UserName': '@747c321e4170daada2e873aa731a3e6b0799b6ae98fceabfb69322aa3fe232bb',
                                'NickName': '陳厚成0922',
                                'AttrStatus': 266277,
                                'PYInitial': '',
                                'PYQuanPin': '',
                                'RemarkPYInitial': '',
                                'RemarkPYQuanPin': '',
                                'MemberStatus': 0,
                                'DisplayName': '',
                                'KeyWord': ''}
                            >
                        ]
                    >,
                    'Uin': 0,
                    'UserName': '@@26536008f1c1307c892640411bf7f60ffd2a3feb138ed6591e65e4fe7541708e',
                    'NickName': 'me and myself',
                    'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgetheadimg?seq=0&username=@@26536008f1c1307c892640411bf7f60ffd2a3feb138ed6591e65e4fe7541708e&skey=@crypt_24f3c9b8_8745523c9c4ecd2615222a8cf1a2e9e5',
                    'ContactFlag': 2,
                    'MemberCount': 3,
                    'RemarkName': '',
                    'HideInputBarFlag': 0,
                    'Sex': 0,
                    'Signature': '',
                    'VerifyFlag': 0,
                    'OwnerUin': 0,
                    'PYInitial': '',
                    'PYQuanPin': '',
                    'RemarkPYInitial': '',
                    'RemarkPYQuanPin': '',
                    'StarFriend': 0,
                    'AppAccountFlag': 0,
                    'Statues': 1,
                    'AttrStatus': 0,
                    'Province': '',
                    'City': '',
                    'Alias': '',
                    'SnsFlag': 0,
                    'UniFriend': 0,
                    'DisplayName': '',
                    'ChatRoomId': 0,
                    'KeyWord': '',
                    'EncryChatRoomId': '',
                    'IsOwner': 0,
                    'IsAdmin': None,
                    'Self': <ChatroomMember: {'MemberList': <ContactList: []>,
                    'Uin': 0,
                    'UserName': '@9f15931b5d2a9ea59d4c5e220e079c5574b036939a4300c985ae83094d0b8250',
                    'NickName': '網路分享小寶貝',
                    'AttrStatus': 33558565,
                    'PYInitial': '',
                    'PYQuanPin': '',
                    'RemarkPYInitial': '',
                    'RemarkPYQuanPin': '',
                    'MemberStatus': 0,
                    'DisplayName': '',
                    'KeyWord': ''}>,
                    'HeadImgUpdateFlag': 1,
                    'ContactType': 0,
                    'ChatRoomOwner': '@102dffe8deaaa7160fae7db1214b0bf69285399c0e94bbb35bb5457cde76b001'
                } # 'MemberList'
            >, # Chatroom:
        'Type': 'Text',
        'Text': '22'}
    isGrupChat>
    --> 怎解？與一般 message 比對看看。。。
    notGrupChat> msg . cr
        {'MsgId': '2003695809776296585',
        'FromUserName': '@3102312982f699ea667ea6f1da7274c41a0a04de0d39304b9c23cb53532eaf36',
        'ToUserName': '@b56266318a18a59dfde8de5c771d45b588e6804ad1a440201cc7155d601df7a5',
        'MsgType': 1,
        'Content': 'not groupchat',
        'Status': 3,
        'ImgStatus': 1,
        'CreateTime': 1511087391,
        'VoiceLength': 0,
        'PlayLength': 0,
        'FileName': '',
        'FileSize': '',
        'MediaId': '',
        'Url': '',
        'AppMsgType': 0,
        'StatusNotifyCode': 0,
        'StatusNotifyUserName': '',
        'RecommendInfo': {'UserName': '',
            'NickName': '',
            'QQNum': 0,
            'Province': '',
            'City': '',
            'Content': '',
            'Signature': '',
            'Alias': '',
            'Scene': 0,
            'VerifyFlag': 0,
            'AttrStatus': 0,
            'Sex': 0,
            'Ticket': '',
            'OpCode': 0},
        'ForwardFlag': 0,
        'AppInfo': {'AppID': '',
            'Type': 0},
        'HasProductId': 0,
        'Ticket': '',
        'ImgHeight': 0,
        'ImgWidth': 0,
        'SubMsgType': 0,
        'NewMsgId': 2003695809776296585,
        'OriContent': '',
        'User': <User: {'MemberList': <ContactList: []>,
            'Uin': 0,
            'UserName': '@3102312982f699ea667ea6f1da7274c41a0a04de0d39304b9c23cb53532eaf36',
            'NickName': 'hcchen5600',
            'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=647060216&username=@3102312982f699ea667ea6f1da7274c41a0a04de0d39304b9c23cb53532eaf36&skey=@crypt_24f3c9b8_0dc65510ad7649edb30b6fb91b87cd98',
            'ContactFlag': 3,
            'MemberCount': 0,
            'RemarkName': '',
            'HideInputBarFlag': 0,
            'Sex': 1,
            'Signature': 'hcchen5600',
            'VerifyFlag': 0,
            'OwnerUin': 0,
            'PYInitial': 'HCCHEN5600',
            'PYQuanPin': 'hcchen5600',
            'RemarkPYInitial': '',
            'RemarkPYQuanPin': '',
            'StarFriend': 0,
            'AppAccountFlag': 0,
            'Statues': 0,
            'AttrStatus': 33788007,
            'Province': 'New Taipei City',
            'City': '',
            'Alias': '',
            'SnsFlag': 1,
            'UniFriend': 0,
            'DisplayName': '',
            'ChatRoomId': 0,
            'KeyWord': '',
            'EncryChatRoomId': '',
            'IsOwner': 0}>,
        'Type': 'Text',
        'Text': 'not groupchat'}
    notGrupChat>

    # msg from Chatroom     
    chatroom> msg
    itChat> . cr
        {'MsgId': '7449149571480245218',
         'FromUserName': '@@7342ac412e48adb7025730088d9f2b296e02c40d8b2ae565f5052cbb28a99b46',
         'ToUserName': '@8f9b6e475295cfc7b0a3df608b70360883bbc0bfc136bffaddd2a8f5064cadc3',
         'MsgType': 1,
         'Content': '@陳厚成0922  1122',
         'Status': 3,
         'ImgStatus': 1,
         'CreateTime': 1511327340,
         'VoiceLength': 0,
         'PlayLength': 0,
         'FileName': '',
         'FileSize': '',
         'MediaId': '',
         'Url': '',
         'AppMsgType': 0,
         'StatusNotifyCode': 0,
         'StatusNotifyUserName': '',
         'RecommendInfo': {'UserName': '',
         'NickName': '',
         'QQNum': 0,
         'Province': '',
         'City': '',
         'Content': '',
         'Signature': '',
         'Alias': '',
         'Scene': 0,
         'VerifyFlag': 0,
         'AttrStatus': 0,
         'Sex': 0,
         'Ticket': '',
         'OpCode': 0},
         'ForwardFlag': 0,
         'AppInfo': {'AppID': '',
         'Type': 0},
         'HasProductId': 0,
         'Ticket': '',
         'ImgHeight': 0,
         'ImgWidth': 0,
         'SubMsgType': 0,
         'NewMsgId': 7449149571480245218,
         'OriContent': '',
         'ActualNickName': 'hcchen5600',
         'IsAt': True,
         'ActualUserName': '@0117966a4bdf06be236ba39e812db37d68084ddd748247f9341b00c344cb73c1',
         'User': <Chatroom: {'MemberList': <ContactList: [<ChatroomMember: {'MemberList': <ContactList: []>,
         'Uin': 0,
         'UserName': '@5ba50f986cf625ac05042d7a9935050ec67b7d97f4b40f08c75d53238aab3eec',
         'NickName': '網路分享小寶貝',
         'AttrStatus': 33558565,
         'PYInitial': '',
         'PYQuanPin': '',
         'RemarkPYInitial': '',
         'RemarkPYQuanPin': '',
         'MemberStatus': 0,
         'DisplayName': '',
         'KeyWord': ''}>,
         <ChatroomMember: {'MemberList': <ContactList: []>,
         'Uin': 0,
         'UserName': '@0117966a4bdf06be236ba39e812db37d68084ddd748247f9341b00c344cb73c1',
         'NickName': 'hcchen5600',
         'AttrStatus': 33788007,
         'PYInitial': '',
         'PYQuanPin': '',
         'RemarkPYInitial': '',
         'RemarkPYQuanPin': '',
         'MemberStatus': 0,
         'DisplayName': '',
         'KeyWord': ''}>,
         <ChatroomMember: {'MemberList': <ContactList: []>,
         'Uin': 0,
         'UserName': '@8f9b6e475295cfc7b0a3df608b70360883bbc0bfc136bffaddd2a8f5064cadc3',
         'NickName': '陳厚成0922',
         'AttrStatus': 266277,
         'PYInitial': '',
         'PYQuanPin': '',
         'RemarkPYInitial': '',
         'RemarkPYQuanPin': '',
         'MemberStatus': 0,
         'DisplayName': '',
         'KeyWord': ''}>]>,
         'Uin': 0,
         'UserName': '@@7342ac412e48adb7025730088d9f2b296e02c40d8b2ae565f5052cbb28a99b46',
         'NickName': 'me and myself',
         'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgetheadimg?seq=645051440&username=@@7342ac412e48adb7025730088d9f2b296e02c40d8b2ae565f5052cbb28a99b46&skey=',
         'ContactFlag': 2,
         'MemberCount': 3,
         'RemarkName': '',
         'HideInputBarFlag': 0,
         'Sex': 0,
         'Signature': '',
         'VerifyFlag': 0,
         'OwnerUin': 0,
         'PYInitial': 'MEANDMYSELF',
         'PYQuanPin': 'meandmyself',
         'RemarkPYInitial': '',
         'RemarkPYQuanPin': '',
         'StarFriend': 0,
         'AppAccountFlag': 0,
         'Statues': 1,
         'AttrStatus': 0,
         'Province': '',
         'City': '',
         'Alias': '',
         'SnsFlag': 0,
         'UniFriend': 0,
         'DisplayName': '',
         'ChatRoomId': 0,
         'KeyWord': '',
         'EncryChatRoomId': '@fda7300a2b81699fc64e6370385267d7',
         'IsOwner': 0,
         'IsAdmin': None,
         'Self': <ChatroomMember: {'MemberList': <ContactList: []>,
         'Uin': 0,
         'UserName': '@8f9b6e475295cfc7b0a3df608b70360883bbc0bfc136bffaddd2a8f5064cadc3',
         'NickName': '陳厚成0922',
         'AttrStatus': 266277,
         'PYInitial': '',
         'PYQuanPin': '',
         'RemarkPYInitial': '',
         'RemarkPYQuanPin': '',
         'MemberStatus': 0,
         'DisplayName': '',
         'KeyWord': ''}>}>,
         'Type': 'Text',
         'Text': '@陳厚成0922  1122'}
    chatroom>
    \ 同上，另一觀點
    itChat> msg keys . cr
    dict_keys(['MsgId',
         'FromUserName',
         'ToUserName',
         'MsgType',
         'Content',
         'Status',
         'ImgStatus',
         'CreateTime',
         'VoiceLength',
         'PlayLength',
         'FileName',
         'FileSize',
         'MediaId',
         'Url',
         'AppMsgType',
         'StatusNotifyCode',
         'StatusNotifyUserName',
         'RecommendInfo',
         'ForwardFlag',
         'AppInfo',
         'HasProductId',
         'Ticket',
         'ImgHeight',
         'ImgWidth',
         'SubMsgType',
         'NewMsgId',
         'OriContent',
         'ActualNickName',
         'IsAt',
         'ActualUserName',
         'User',
         'Type',
         'Text'])
    chatroom>
    
    
'''


