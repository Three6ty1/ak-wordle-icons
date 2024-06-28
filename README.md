# Instructions

## Expected results as of 28/06/2024
There 325 Icons, 15 missing entries database due to icons being from CN.

1 Icon is Guard Amiya.

There are total 310 operators in the database and the site says that there are 309 operators in global?

## Update Database
Download ***handbook_info_table.json*** and ***character_table.json*** from Aceship github
https://github.com/Aceship/AN-EN-Tags/tree/master/json/gamedata/en_US/gamedata/excel

Replace local files if applicable

Run build_db.py in root file (I hard coded the paths)

## Update Icons
(Optional) Use clean.py if copy and pasting images from the aceship icons directory
(Optional) Go through the most recent commit in Aceship icons and download every char manually and insert into avatars

Need to download cwebp and put /bin/.exe into the avatar directory https://developers.google.com/speed/webp/download 
Need to run in the same directory as avatars

convert.sh the files from png to webp and make into 180x180 to conserve space

Copy and paste the UL element from ace ship when searching all operators

Use sanity_check wiki.gg site https://arknights.wiki.gg/wiki/Operator/List

## Update site
Move updated operator db into correct directory

Seed database