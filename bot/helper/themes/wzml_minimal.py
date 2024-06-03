#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '𝖴𝗉𝖽𝖺𝗍𝖾𝗌 🌛'
    ST_BN1_URL = 'https://t.me/dadaxcloud'
    ST_BN2_NAME = '𝖮𝗐𝗇𝖾𝗋 🛸'
    ST_BN2_URL = 'https://t.me/dadaxbhai'
    ST_MSG = '''<i>This bot can mirror all your links|files|torrents to telegram.</i>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<i>𝖭𝗈𝗐, 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖶𝗂𝗅𝗅 𝖲𝖾𝗇𝖽 𝖠𝗅𝗅 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾𝗌 𝖠𝗇𝖽 𝖫𝗂𝗇𝗄𝗌 𝖧𝖾𝗋𝖾. 𝖲𝗍𝖺𝗋𝗍 𝖴𝗌𝗂𝗇𝗀 ...</i>'''
    ST_UNAUTH = '''<i>𝖭𝗈𝗐, 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖶𝗂𝗅𝗅 𝖲𝖾𝗇𝖽 𝖠𝗅𝗅 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾𝗌 𝖠𝗇𝖽 𝖫𝗂𝗇𝗄𝗌 𝖧𝖾𝗋𝖾. 𝖲𝗍𝖺𝗋𝗍 𝖴𝗌𝗂𝗇𝗀 ...</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>🎉Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''⌬ <b><i>BOT STATISTICS :</i></b>
┖ <b>Bot Uptime :</b> {bot_uptime}

┎ <b><i>RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>DISK :</i></b>
┃ {disk_bar} {disk}%
┃ <b>Total Disk Read :</b> {disk_read}
┃ <b>Total Disk Write :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''⌬ <b><i>OS SYSTEM :</i></b>
┠ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b><i>NETWORK STATS :</i></b>
┠ <b>Upload Data:</b> {up_data}
┠ <b>Download Data:</b> {dl_data}
┠ <b>Pkts Sent:</b> {pkt_sent}k
┠ <b>Pkts Received:</b> {pkt_recv}k
┖ <b>Total I/O Data:</b> {tl_data}

┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>Total Core(s) :</b> {total_core}
┖ <b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''⌬ <b><i>REPO STATISTICS :</i></b>
┠ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {lat_version}
┖ <b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''⌬ <b><i>BOT LIMITATIONS :</i></b>
┠ <b>Direct Limit :</b> {DL} GB
┠ <b>Torrent Limit :</b> {TL} GB
┠ <b>GDrive Limit :</b> {GL} GB
┠ <b>YT-DLP Limit :</b> {YL} GB
┠ <b>Playlist Limit :</b> {PL}
┠ <b>Mega Limit :</b> {ML} GB
┠ <b>Clone Limit :</b> {CL} GB
┖ <b>Leech Limit :</b> {LL} GB

┎ <b>Token Validity :</b> {TV}
┠ <b>User Time Limit :</b> {UTI} / task
┠ <b>User Parallel Tasks :</b> {UT}
┖ <b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Task Started</i></b>
┠ <b>Mode:</b> {Mode}
┖ <b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b>Source:</b>
┖ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➲ <b><u>Task Started :</u></b>\n┃\n┖ <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b>User :</b> {mention} ( #ID{uid} )\n┖ <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '🗂️ 𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲 : <code>{Name}</code>\n\n'
    SIZE =                  '➢ <b>𝖲𝗂𝗓𝖾: </b><code>{Size}</code>\n\n'
    ELAPSE =                '➢ <b>𝖤𝗅𝖺𝗉𝗌𝖾𝖽: </b><code>{Time}</code>\n\n'
    MODE =                  '➢ <b>𝖬𝗈𝖽𝖾: </b><code>{Mode}</code>\n\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '➢ <b>𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌: </b><code>{Files}</code>\n\n'
    L_CORRUPTED_FILES =     ''
    L_CC =                  '➢ <b>𝖴𝗌𝖾𝗋: </b>{Tag}\n\n'
    PM_BOT_MSG =            '➲ <b><i>File(s) have been Sent above</i></b>'
    L_BOT_MSG =             '• <b>𝖥𝗂𝗅𝖾𝗌 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖲𝖾𝗇𝗍 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖣𝗆...</b>'
    L_LL_MSG =              ''
    
    # ----- MIRROR -------
    M_TYPE =                '➢ <b>Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '➢ <b>SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '➢ <b>Files: </b>{Files}\n'
    RCPATH =                '➢ <b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '➢ <b>By: </b>{Tag}\n\n'
    M_BOT_MSG =             '➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 𝖢𝗁𝖾𝖼𝗄 𝖡𝗈𝗍 𝖯𝖬'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b>▰▰▰▰<a href="https://t.me/dadaxcloud">⤹★ 𝗗𝗮𝗗𝗮 𝗫 𝗖𝗹𝗼𝘂𝗱 ★⤸</a> </b>▰▰▰▰\n\n➣ : </b><code>{Name}</code>\n'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n {Bar}'
    PROCESSED =         '\n <b>𝖯𝗋𝗈𝖼𝖾𝗌𝗌𝖾𝖽:</b> {Processed}'
    STATUS =            '\n <b>𝖲𝗍𝖺𝗍𝗎𝗌:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>𝖤𝖳𝖠:</b> {Eta}'
    SPEED =             '\n <b>𝖲𝗉𝖾𝖾𝖽:</b> {Speed}'
    ELAPSED =                                     ' | <b>𝖤𝗅𝖺𝗉𝗌𝖾𝖽:</b> {Elapsed}'
    ENGINE =            '\n <b>𝖤𝗇𝗀𝗂𝗇𝖾:</b> {Engine}'
    STA_MODE =          '\n <b>𝖬𝗈𝖽𝖾:</b> {Mode}'
    SEEDERS =           '\n <b>𝖲𝖾𝖾𝖽𝖾𝗋𝗌:</b> {Seeders} | '
    LEECHERS =                                           '<b>𝖫𝖾𝖾𝖼𝗁𝖾𝗋𝗌:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n <b>𝖲𝗂𝗓𝖾: </b>{Size}'
    SEED_SPEED =     '\n <b>𝖲𝗉𝖾𝖾𝖽: </b> {Speed} | '
    UPLOADED =                                     '<b>𝖴𝗉𝗅𝗈𝖺𝖽𝖾𝖽: </b> {Upload}'
    RATIO =          '\n <b>𝖱𝖺𝗍𝗂𝗈: </b> {Ratio} | '
    TIME =                                         '<b>𝖳𝗂𝗆𝖾: </b> {Time}'
    SEED_ENGINE =    '\n <b>𝖤𝗇𝗀𝗂𝗇𝖾:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n <b>𝖲𝗂𝗓𝖾: </b>{Size}'
    NON_ENGINE =     '\n <b>𝖤𝗇𝗀𝗂𝗇𝖾:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n <b>𝖴𝗌𝖾𝗋:</b> <code>{User}</code> | '
    ID =                                                        '<b>ID:</b> <code>{Id}</code>'
    BTSEL =          '\n <b>Select:</b> {Btsel}'
    CANCEL =         '\n <b>𝖲𝗍𝗈𝗉 🛑</b> :<b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⟲<b>𝖡𝗈𝗍 𝖲𝗍𝖺𝗍𝗌</b>\n'
    TASKS =  '<b>𝖳𝖺𝗌𝗄𝗌:</b> {Tasks}\n'
    BOT_TASKS = '<b>𝖳𝖺𝗌𝗄𝗌:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n'
    Cpu = '<b>CPU:</b> {cpu}% | '
    FREE =                      '<b>𝖥𝗋𝖾𝖾:</b> {free} [{free_p}%]'
    Ram = '\n<b>𝖱𝖠𝖬:</b> {ram}% | '
    uptime =                     '<b>𝖴𝖯𝖳𝖨𝖬𝖤:</b> {uptime}'
    DL = '\n<b>𝖣𝖫:</b> {DL}/s | '
    UL =                        '<b>𝖴𝗅:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⤺ '
    REFRESH = '𝖯𝖺𝗀𝖾 ⍟\n{Page}'
    NEXT = '⤻'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '<b>𝖲𝗂𝗓𝖾: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '<b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '<b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '<b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '<b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings :</u></b>
        
┎<b> Name :</b> {NAME} ( <code>{ID}</code> )
┠<b> Username :</b> {USERNAME}
┠<b> Telegram DC :</b> {DC}
┖<b> Language :</b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''㊂ <b><u>Universal Settings : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┠<b> Total User TD(s) :</b> <i>{USERTD}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''㊂ <b><u>Leech Settings for {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dumps :</b> <code>{LDUMP}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
