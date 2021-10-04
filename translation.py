from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I am Fastest Renamer Bot which help you to rename and convert files in less time. Use /help command to see features.

Just send a File or Media to get started

By @Tellybots_4u
    """
RENAME_403_ERR = "What Are You Doing? Bruh!!"
    BANNED_USER_TEXT = "Sorry!! Sir you are banned to use me. That means you are not able to use me! \n \n Contact our support group : @Tellybots_support For more Details.. "
    ABS_TEXT = "What Are You Trying To Do, Mate?"
    UPGRADE_TEXT = "Contact : @Tellybots_support"
    DOWNLOAD_START = "<b> 📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ⌉ \n│\n</b>"
    UPLOAD_START = "<b> 📤 ᴜᴘʟᴏᴀᴅɪɴɢ ⌉ \n│\n</b>"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry Do You Think! I'll Upload It?"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>Thank you for Using Me SHARE > </b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds"
    NOT_AUTH_USER_TEXT = "CONTACT : <a href='https://telegram.me/tellybots_support'> Tellybots_support</a>"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Contact our support group if got this msg @tellybots_support
    SAVED_CUSTOM_THUMB_NAIL = "<b>Thumbnail Saved ✅ This Is Permanent Until</b> ❌ /delthumb ❌"
    DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail Cleared Succesfully"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Media Cleared Succesfully."
    SAVED_RECVD_DOC_FILE = "<b>File Downloaded Successfully </b>"
    REPLY_TO_DOC_FOR_RENAME_FILE = "<b>Please Reply To An File With /rename file name extension To rename a file</b>"
    REPLY_TO_FILE_FOR_CONVERT = "<b> Please Reply To An File With /c2v To Convert It Into Streamable Video File</b>"
    REPLY_TO_DOC_FOR_C2A = "<b> Please Reply To An File/video With /c2a To Convert It Into Audio File</b>"
    Custom_caption_ul_file = " "
    No_thumb_found = "No Thumbnail found "
    User_added_to_db = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    File_name = """File name is so long this cannot be supported...Decrease the no of letters to get started 🔻🔻"""
    About_me = """<b><u>About Me:</u></b>
    
<b>An advance multi purpose bot Which Can :-</b>
 Rename telegram files 
 Set custom thumbnail
 Convert Files to Video 

 Any problem contact our support group 🖊️ <a href="https://telegram.dog/tellybots_supporr"><b>Tellybots_4u</b></a>
    """
    help_user = """Use Below command to see how to use me

<b>Made with 💕 : @Tellybots_4u</b>
"""
    
    rename_help = """
<b><u>Rename Commands</u></b>
 Send me any Telegram File or Media.
 Upload any correct file or media.
 Reply to that message to '/rename' new name.extension for renaming.
    """
    c2v_help  = """
<b><u>Convert File Commands</u></b>
 Reply with file With '/c2v' To convert file to video.
"""
    THUMBNAIL_HELP = """
<b><u>Thumbnail Commands</u></b>
 Send a photo to make it as Custom Thumbnail.

 Send '/delthumb' to Deleting Thumbnail.
 Send '/showthumb' for view Current Thumbnail.
"""
CAPTION_HELP = """Here Are The Available Commands In Custom Caption \n\n\n <code>/scaption</code> Use This Command To Save Your Custom Caption \n<b>Usage:</b> <code>/scaption your caption text</code> \n\n<b>[You Can Use</b> <code>{filename}</code> <b>For showing new file name in the caption]</b> """

