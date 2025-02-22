def longest_palindromic_subsequence(s, subStr = False):
    '''
    动态规划算法的优化
    时间复杂度o(n^2)，将空间复杂度降低为o(2n)
    用nlist存储j情况下所有的子串是否为回文子串的标志
    用olist存储j-1情况下所有的子串是否为回文子串的标志
    find the longest_palindromic_subsequence(lps) and the lenth of lps in s.
    it can return the logestSubStr as well.
    you can set subStr=True to do it.
    args:
        s -- a str
        subStr -- if reture longest_palindromic_subsequence as a str
    return:
        logestLen -- an int 
        logestSubStr -- a str, longest_palindromic_subsequence 
    '''

    k = len(s)
    olist = [0] * k    # 申请长度为n的列表，并初始化
    nList = [0] * k    # 同上
    logestSubStr = ""
    logestLen = 0

    for j in range(0, k):
        for i in range(0, j + 1):
            if j - i <= 1:
                if s[i] == s[j]:
                    nList[i] = 1                 # 当 j 时，第 i 个子串为回文子串
                    len_t = j - i + 1
                    if logestLen < len_t:        # 判断长度
                        logestSubStr = s[i:j + 1]
                        logestLen = len_t
            else:
                if s[i] == s[j] and olist[i+1]:   # 当j-i>1时，判断s[i]是否等于s[j]，并判断当j-1时，第i+1个子串是否为回文子串
                    nList[i] = 1                  # 当 j 时，第 i 个子串为回文子串
                    len_t = j - i + 1
                    if logestLen < len_t:
                        logestSubStr = s[i:j + 1]
                        logestLen = len_t
        olist = nList                            # 覆盖旧的列表
        nList = [0] * k                          # 新的列表清空
    
    if subStr:
        return logestLen, logestSubStr
    return logestLen
