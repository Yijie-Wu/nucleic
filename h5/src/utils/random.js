  /**
         * 生成指定找度的随机字符串
         */
   export function randomString(length) {
    var str = '0123456789';
    var result = '';
    for (var i = length; i > 0; --i) 
        result += str[Math.floor(Math.random() * str.length)];
    return result;
}