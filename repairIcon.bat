rem 关闭explorer.exe

taskkill /f /im explorer.exe

attrib -s -h -i %userprofile%AppDataLocalIconCache.db

del %userprofile%AppDataLocalIconCache.db /a

attrib +h +s %userprofile%AppDataLocalIconCache.db

rem 打开explorer

start explorer