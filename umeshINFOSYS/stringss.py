def countPrefixes(word,s):
    count = 0
    for i in word:
        j = len(i)
        k = len(s)
        if j <= k:
            if i == s[:j]:
                count += 1

    return count


word = ["feh","w","w","lwd","c","s","vk","zwlv","n","w","sw","qrd","w","w","mqe","w","w","w","gb","w","qy","xs","br","w","rypg","wh","g","w","w","fh","w","w","sccy"]
s = "w"


word = ["ycwj","hak","v","kjg","zw","vtes","vom","ii","as","v","vo","v","w","vomy","loa","fbm","j","v","vo","e","y","t","eh","yk","bt","x","vomy","vom","yab","v","sydi","wnb","z","v","iygp","vomy"]
s = "vomy"
print(countPrefixes(word,s))