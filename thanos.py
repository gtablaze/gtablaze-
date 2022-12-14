o
    ??Rcn  ?                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dl
mZ d dlmZmZmZ d dl	mZmZmZmZ d dlmZ d dlmZmZmZmZmZmZmZ d dlmZmZm Z m!Z!m"Z"m#Z#m$Z$m%Z%m&Z& d dl'm(Z(m)Z) d d	l*m+Z+ d d
l,m-Z-m.Z. d dl/m0Z0m1Z1m2Z2 d dl3m4Z4 d dl5m6Z6m7Z7m8Z8m9Z9m:Z:m;Z;m<Z<m=Z= d dl>m?Z? dZ@dZAejBZCdZDdZEdZFdZdZGdZHdZIejJ?Kd?s?e?Ld? ejJ?Kd?s?eMdd? dd? ZNdd? ZOdd ? ZPd!d"? ZQd#d$? ZRd%d&? ZSd'd(? ZTd)d*? ZUeU?  dS )+?    N)?reader)?MINYEAR?datetime?	timedelta)?Fore?Back?Style?init)?TelegramClient)?	functions?typesr
   ?
connection?sync?utils?errors)	?InputPeerEmpty?UserStatusOffline?UserStatusRecently?UserStatusLastMonth?UserStatusLastWeek?PeerUser?PeerChannel?InputPeerChannel?InputPeerUser)?GetContactsRequest?DeleteContactsRequest)?DeletePhotosRequest)?GetDialogsRequest?ImportChatInviteRequest)?GetFullChannelRequest?JoinChannelRequest?InviteToChannelRequest)?SessionPasswordNeededError)?UsernameInvalidError?ChannelInvalidError?PhoneNumberBannedError?YouBlockedUserError?PeerFloodError?UserPrivacyRestrictedError?ChatWriteForbiddenError?UserAlreadyParticipantError)?StringSessionzhttps://t.me/THANOS_PROZthanosprosssi??? i(? Z d038e172eb99839b69c39c3c25cd98cfz[1;31mz[1;32mz[1;36mz[1,35mz
./sessions?	phone.csv?wc                  C   s?   t ?  tdd??L} dd? t?| ?D ?}d}|D ]3}t?|?}|d7 }ttjt	j
 d|? ? ? td|? ?tt?}|?|? |tt?? |??  t?  qd	}W d   ? n1 sWw   Y  t|rgtjt	j d
 nd? ttjt	j d ? t?  d S )Nr,   ?rc                 S   ?   g | ]}|d  ?qS ?r   ? ??.0?rowr1   r1   ?2/storage/emulated/0/freescripts/THANOSV2/thanos.py?
<listcomp>g   ?    zlogin.<locals>.<listcomp>r   ?   ?Login ?	sessions/TzAll Number added Done !zError!zPress enter to back)?banner?open?csvr   r   ?parse_phone?printr   ?BRIGHTr   ?GREENr
   ?API_ID?HashID?startr    ?	channelxd?
disconnect?RESET?YELLOW?input)?f?str_list?po?pphone?phone?client?doner1   r1   r5   ?loginb   s$   

?(
rQ   c               
   C   s~  t t?} tt?}g }d}tdd???}dd? t?|?D ?}d}|D ]T}|d7 }t?|?}t	d|? ?? t
d	|? ?| |?}	|	??  |	?? sqzt	d
? t|?}
t|?}|?|? W q  typ   t	d? t|?}
t|?}|?|? Y q w t	?  q d}t	d? t	|ddi? t	d? tdddd??}tj|ddd?}|?|? W d   ? n1 s?w   Y  W d   ? n1 s?w   Y  dd? }d S )NFr,   r.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6   ?   r7   zBanFilter.<locals>.<listcomp>r   r8   r9   r:   zThis Phone Has Been RevokedZBanTzList Of Banned Numbers?sep?
zSaved In BanNumers.csv?BanNumbers.csvr-   ?UTF-8??encoding?,?Z	delimiter?lineterminatorc               	   S   s^  g } g }g }g }g }t dd??}|D ]}| ?|? qW d   ? n1 s$w   Y  | D ]}t|??dd?}|?|? q+t d??+}t dd??}	|D ]}|	?|?dd?? qHW d   ? n1 s^w   Y  W d   ? n1 smw   Y  t dd??}	|	D ]}
|?|
? qzW d   ? n1 s?w   Y  |D ]}t|??dd?}|?|? q?t|?}t|?}|?|?}|D ]}||vr?|?|? q?t d	dd
d??}tj|dd?}|?	|? W d   ? n1 s?w   Y  t d	??0}t dd??}|D ]}t|??dd?}|?|? q?W d   ? n	1 ?s	w   Y  W d   ? n	1 ?sw   Y  t
?d? t
?d	d? td? d S )Nr,   r.   rS   ? rT   zoutfile.csvr-   rX   z	unban.csvrU   rV   )rZ   z(Done,All Banned Number Have Been Removed)r<   ?append?str?replace?write?set?intersectionr=   ?writer?	writerows?os?remove?renamer?   )Z
collectionZncZcollection1Znc1ZmaindZinfile?line?xZmod_xZoutfileZline1?iZmod_i?uniqueZunique1Zitd?	writeFilerb   Zlast?finalZline3r1   r1   r5   ?
autoremove$  sd   	????? ??

????? 
zBanFilter.<locals>.autoremove)?intrB   r]   rC   r<   r=   r   r   r>   r?   r
   ?connect?is_user_authorizedr\   r%   rb   rc   )Zapi_idZapi_hashZMadeByTHANOS_PROrP   rJ   rK   rL   Zunparsed_phonerN   rO   ?
THANOS_PROZNero_oprk   rb   rm   r1   r1   r5   ?	BanFilter?   sN   


????{rr   c                  C   s?  t ?? } | ?d? | d d ?? }|?d?}| d d ?? }tjtjd? tt	j
tj d|? ? ? ?ztd|? ?tt?}|??  |?? ?r5tt	j
tj d	 ? d
}t?? }|tdd? }|tdd? }tdddd?}	tj|	ddd?}
|
?g d?? z?|D ]?}z|t|?? W n ty? } zW Y d }~nd }~ww tt	j
tj d|? d? ? g }z	|j|dd?}W n ty? } zW Y d }~nd }~ww |D ]L}|jr?|j}nd}|jr?|j}nd}t |j!t"?r?|}nt |j!t#?r?|}t |j!t$?r?|}t |j!t%?r?|j!j&}|?'d?}|
?|||j(|||g? |d
 }q?q}W n t?y* } zW Y d }~nd }~ww |	?)?  td|? ntt	j
tj* d|? ? ? W n t?y` } ztt	j
tj* d ? W Y d }~nd }~ww t+? }dd? }d d!? }|?  |?  td"d#dd??U}t?,|?}tdddd??8}	tj|	ddd?}
|
?g d?? d$}|D ]}|d
7 }|
?||d
 |d% |d& |d' |d( f? ?q?W d   ? n	1 ?s?w   Y  W d   ? n	1 ?s?w   Y  t-?.d)? t-?.d"? tt	j
tj d* ? tt	j
tj d+ ? t/?  d S ),N?
config.inirq   Z	FromGrouprX   ?PhoneNumber??levelz
Logging For r:   z
login Doner8   i????)Zdaysi?????data.csvr-   rU   rV   rS   rY   ?zsr. no.?usernamezuser id?name?groupZStatuszScrabing Members from z group.....T?Z
aggressiver[   z%Y%m%dzCount : zlogin fail z
login failc                  S   ??   t ? } tdddd??%}t?|?}|D ]}| ?|? |D ]}|dkr&| ?|? qqW d   ? n1 s2w   Y  tdddd??}tj|dd	d
?}|?| ? W d   ? d S 1 sWw   Y  d S ?Nrw   r.   rU   rV   r[   ?1.csvr-   rX   rS   rY   ??listr<   r=   r   r\   re   rb   rc   ??linesZreadFiler   r4   Zfieldrk   rb   r1   r1   r5   ?main?  ?    


????$"?zScraper.<locals>.mainc                  S   r}   ?Nr   r.   rU   rV   ry   ?2.csvr-   rX   rS   rY   r?   r?   r1   r1   r5   ?main1?  ?    


????'"?zScraper.<locals>.main1r?   r.   r   ?   ?   ?   ?   r   zTask completedzEnter any key to exit)0?configparser?ConfigParser?read?strip?split?logging?basicConfig?WARNINGr?   r   r@   r   rG   r
   rB   rC   ro   rp   rA   r   Znowr   r<   r=   rb   ?writerowr    ?	ExceptionrH   ?iter_participantsry   Z
first_name?
isinstance?statusr   r   r   r   Z
was_online?strftime?id?close?REDr?   r   rd   re   rI   )?configZlink1ZlinksrN   rO   ?countZtodayZ	last_weekZ
last_monthrJ   rb   ?link?e?all_participants?userry   rz   Zdate_onlineZdate_online_strr?   r?   r?   ?source?rdrri   r4   r1   r1   r5   ?Scraper?  s?   


????	

??c??	? ??	<?
.????
!

r?   c               	      sn  t ?  tj?tj} tj?tj}tj?t?? }|?	d? |d d ?|d d ?|d d ?|d d ?|d d ? g }t
dd	??}t|?}t|?}|D ]}|?t|d
 ?? qKW d   ? n1 saw   Y  |?t| ? d?? d?? tt|??? ?? ?? ? ????????f	dd?}? ????????f	dd?}	tt|? d?? ???}
|
dkr?|	?  d S |
dkr?|?  d S d S )Nrs   rq   ?ToGroupZGroupIDZ	EnterStopZStartingAccountZ
EndAccountr,   r.   r   zTotal account: ? c            )         s?  t tjtj d ? tt? ?} d}t??}t??}t??d }t? ?}td?}td?d }t??}tdddd??}	t	j
|	d	d
d?}
|
?||| g? W d   ? n1 sTw   Y  d}d}?||? D ?]?}|d7 }t d|? ?? t?|?}t d|? ?? td|? ?tt?}|??  |?? s?t ?? d?? ?? |?|? |?|td?? |}g }t|dd??;}t	j|d	d
d?}t|d ? |D ]#}i }|d |d< |d |d< t|d ?|d< |d |d< |?|? q?W d   ? n1 s?w   Y  tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sw   Y  t|?}|| }tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sLw   Y  t|?}|| } tdddd??}!t	j
|!d	d
d?}
|
?|| g? W d   ? n	1 ?s{w   Y  |t|?? t?d? |?t|??}"|t|"d??}#t|#jj ?}$t d|$? ?? |$|k?r?t d|? d?? t?  t!?  d}%|D ]?}t|?t|d ?k?rZt|d ?t|?k?rZz2|%d7 }%|d dk?r?t ?? d?? ?? W ?q?|t"j#?$||d g?? t |%? d ?? t?| ? W ?q? t%?y& }& z|t|?? t?d? W Y d }&~&?q?d }&~&w t&j'?yG }' z|'j(j)}(t |%? d!|(? ?? W Y d }'~'?q?d }'~'w   t*?+?  t ?? d"?? ?? Y ?q??q?|d7 }qct,?-d? d S ?#Nz*Enter Delay Time Per Request 0 For None : rw   r8   ?2   z
memory.csvr-   rU   rV   rX   rS   rY   r   zIndex : r9   r:   zsome thing has changedzEnter the code: Zsrnory   r?   r?   r?   rz   r.   r?   )?channelz	Members: zThe Goal Of z Has Been Completedr[   zno username, moving to nextz - donez - zUnexpected Error).r?   r   r@   r   rA   rn   rI   r]   r<   r=   rb   r?   r   r>   r
   rB   rC   ro   rp   ?send_code_request?sign_inr   ?nextr\   r?   r    ?time?sleep?get_input_entityr   r   ?	full_chat?participants_count?quitr   ?channelsr!   r)   r   ?RPCError?	__class__?__name__?	traceback?	print_excrd   re   ?)ZTHANOS_PRO_devrq   Zrexlinkr?   ZFromZUptoZrexZhacks?stop?filerb   ?aZindexxZxdrN   rO   Z
input_file?usersrJ   Zrowsr4   r?   Zhash_obj?
csv_readerZlist_of_rowsZ
row_numberZ
col_numberZnumnextZ	startfromZ	nextstartZnumendZendtoZnextendZdfr?   ZchannelinfoZrexprodeltanoob?itZcwfer?   r?   ?	ZendacnoZgroupidZ	grouplink?nrM   r.   ZstacnoZstopnum?yer1   r5   ?autos?  s?   
?	


??$???

,	
? ??
zAdderForPhone.<locals>.autosc            )         s?  t tjtj d ? tt? ?} d}t??}t??}t??d }t? ?}td?}td?d }t??}tdddd??}	t	j
|	d	d
d?}
|
?||| g? W d   ? n1 sTw   Y  d}d}?||? D ?]}|d7 }t d|? ?? t?|?}t d|? ?? td|? ?tt?}|??  |?? s?t ?? d?? ?? |?|? |?|td?? |}g }t|dd??;}t	j|d	d
d?}t|d ? |D ]#}i }|d |d< |d |d< t|d ?|d< |d |d< |?|? q?W d   ? n1 s?w   Y  tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sw   Y  t|?}|| }tdd??}t|?}t|?}d}d}||d  |d  }W d   ? n	1 ?sLw   Y  t|?}|| } tdddd??}!t	j
|!d	d
d?}
|
?|| g? W d   ? n	1 ?s{w   Y  |t|?? t?d? |?t|??}"|t|"d??}#t|#jj ?}$t d|$? ?? |$|k?r?t d|? d?? t?  t!?  d}%|D ]?}t|?t|d ?k?rat|d ?t|?k?rat d|$? ?? z2|%d7 }%|d dk?r?t ?? d?? ?? W ?q?|t"j#?$||d g?? t |%? d ?? t?| ? W ?q? t%?y- }& z|t|?? t?d? W Y d }&~&?q?d }&~&w t&j'?yN }' z|'j(j)}(t |%? d!|(? ?? W Y d }'~'?q?d }'~'w   t*?+?  t ?? d"?? ?? Y ?q??q?|d7 }qct,?-d? d S r?   ).r?   r   r@   r   rA   rn   rI   r]   r<   r=   rb   r?   r   r>   r
   rB   rC   ro   rp   r?   r?   r   r?   r\   r?   r   r?   r?   r?   r   r   r?   r?   r?   r   r?   r!   r)   r   r?   r?   r?   r?   r?   rd   re   r?   r?   r1   r5   ?private  s?   
?	


??$???

,
? ??
zAdderForPhone.<locals>.privatez%Press Y if group is private else N : ?Y?N)r	   r   ZLIGHTRED_EXrA   rG   ZBLUErH   r?   r?   r?   r<   r   ?tupler\   rn   r?   r]   ?lenrI   )?grZblr?   rN   Z	delta_objr?   Zlist_of_phoneZphone_r?   r?   Z	rexchooser1   r?   r5   ?AdderForPhone=  sF   	
??(  m  m

?r?   c                  C   s?  t jt jd? t?? } | ?d? | d d ?? }| d d ?? }tdddd	??}t?	|?}d
d? |D ?}W d   ? n1 s>w   Y  tdddd	??}t?	|?}dd? |D ?}W d   ? n1 saw   Y  t
d|? ?tt?}|??  |?? s?td|? d?? n?g }d }	d}
g }d}|dk?rVz?|?|?}|jdk?rt|j?}|j|dd?}g }g }d}g }|D ]}zt|j?|v r?|?|?t|j??? W q?   td? Y q?|??  |??  |jdd? |D ]}||= q?tddddd??}t?|?}|?|? W d   ? n	1 ?sw   Y  d}n
ttjtj d ? d}W n7 t j!j"j#?y-   |t$|?? Y n% t%?yB   ttjtj& d ? d}Y n   ttjtj d ? d}Y |dks?t'? }dd? }d d!? }|?  |?  td"dd#d	??U}t?	|?}tddd#d	??8}tj|d$d%d&?}|?(g d'?? d}|D ]}|d(7 }|?(||d( |d) |d* |d+ |d, f? ?q?W d   ? n	1 ?s?w   Y  W d   ? n	1 ?s?w   Y  t)?*d-? t)?*d"? ttjtj+ d. ? ttjtj& d/ ? ttjtj, d0 ? t-?  d S )1Nru   rs   rq   r?   rt   rw   r.   zutf-8rV   c                 S   s   g | ]}|?qS r1   r1   ?r3   ri   r1   r1   r5   r6   ?  s    z(DeleteALreadyMembers.<locals>.<listcomp>c                 S   s   g | ]}t |d  ??qS )r?   )r]   r?   r1   r1   r5   r6   ?  s    r:   z
Login fail, for number z need Login first
??   r   ?????TFr|   zError get user)?reverser-   r[   )rW   ?newlinez
Invalid Group..
z
Only Public Group Allowed..
z
Invalid Group....
c                  S   r}   r~   r?   r?   r1   r1   r5   r?   V  r?   z"DeleteALreadyMembers.<locals>.mainc                  S   r}   r?   r?   r?   r1   r1   r5   r?   ?  r?   z#DeleteALreadyMembers.<locals>.main1r?   rU   rX   rS   rY   rx   r8   r?   r?   r?   r?   r   zAlready Member Deleted Done !zTask Completedzpress enter to exit).r?   r?   r?   r?   r?   r?   r?   r<   r=   r   r
   rB   rC   ro   rp   r?   Z
get_entityZ	megagroupr]   r?   r?   r\   ?indexr?   rF   ?sortrb   rc   r   r@   r   r?   ?telethonr   Zrpcerrorlistr)   r    ?
ValueErrorrA   r?   r?   rd   re   rG   rH   rI   )r?   r?   rN   rJ   Zusers1r?   ZuserlistrO   ZchatsZ	last_dateZ
chunk_size?groupsr?   r{   Zgroup_idr?   ?resultsZresults1r?   Zindex1r?   ri   r_   r?   r?   r?   r?   r?   rb   r4   r1   r1   r5   ?DeleteALreadyMembers~  s?   

?
?


?
?	?o	<?
.????
!
	
r?   c                  C   s?   t ?  tdd??I} dd? t?| ?D ?}d}|D ]1}t?|?}|d7 }ttd|? ? ? td|? ?t	t
?}|?|? |?t?}tt|d j?  ? qW d   ? d S 1 sTw   Y  d S )	Nr,   r.   c                 S   r/   r0   r1   r2   r1   r1   r5   r6     r7   zViewotp.<locals>.<listcomp>r   r8   zGetting Telegram message Otp r:   )r;   r<   r=   r   r   r>   r?   ?cyr
   rB   rC   rD   Zget_messages?chatopr?   ?text)rJ   rK   rL   rM   rN   rO   ?messagesr1   r1   r5   ?Viewotp  s   


?"?r?   c                   C   s   t ?d? ttd ? d S )N?clearu?    
    

████████╗██╗░░██╗░█████╗░███╗░░██╗░█████╗░░██████╗
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██╔══██╗██╔════╝
░░░██║░░░███████║███████║██╔██╗██║██║░░██║╚█████╗░
░░░██║░░░██╔══██║██╔══██║██║╚████║██║░░██║░╚═══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═════╝░
   )rd   ?systemr?   ?rer1   r1   r1   r5   r;     s   
r;   c                  C   s   t ?  ttd ? ttd ? ttd ? ttd ? ttd ? ttd ? ttd ? ttd ? ttd	 ? ttd
??} | dkrHt?  d S | dkrQt?  d S | dkrZt?  d S | dkrct	?  d S | dkrlt
?  d S | dkrut?  d S | dkr~t?  d S d S )NzSELECTE A OPTION:u4   ╭────⇌ᴅɢᴀᴅᴅᴇʀ⇋────u   ◈┈˃‌ <1> ʟᴏɢɪɴu&   ◈┈˃‌ <2> ʙᴀɴꜰɪʟᴛᴇʀu#   ◈┈˃‌ <3> ꜱᴄʀᴀᴘᴇʀuE   ◈┈˃‌ <4> ᴅᴇʟᴇᴛᴇ ᴀʟʀᴇᴀᴅʏ ᴍᴇᴍʙᴇʀu    ◈┈˃‌ <5> ᴀᴅᴅᴇʀ  u&   ◈┈˃‌ <6> ꜱʜᴜᴛᴅᴏᴡɴu4   ╰────⇌ᴅɢᴀᴅᴅᴇʀ⇋────z
Enter your choice: r8   r?   r?   r?   r?   ?   ?   )r;   r?   r?   r?   rn   rI   rQ   rr   r?   r?   r?   r?   r?   )r?   r1   r1   r5   ?	main_menu-  s4   $






?r?   )V?
subprocessZrequestsr?   rd   r?   r?   Zrandomr?   r?   Zcoloramar=   Zjsonr?   r   r   r   r   r   r   r   r	   Ztelethon.syncr
   r   r   r   r   r   r   Ztelethon.tl.typesr   r   r   r   r   r   r   r   r   Ztelethon.tl.functions.contactsr   r   Ztelethon.tl.functions.photosr   Ztelethon.tl.functions.messagesr   r   Ztelethon.tl.functions.channelsr   r    r!   Ztelethon.errorsr"   Ztelethon.errors.rpcerrorlistr#   r$   r%   r&   r'   r(   r)   r*   Ztelethon.sessionsr+   rE   ZgroupxdrH   r?   rB   r?   rC   r?   r?   Zwi?path?exists?mkdirr<   rQ   rr   r?   r?   r?   r?   r;   r?   r1   r1   r1   r5   ?<module>   sf   h $,(


2  &         G   
m