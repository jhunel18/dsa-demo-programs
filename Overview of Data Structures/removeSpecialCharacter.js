formatName:function formatName(s){
    var _s = s;
    _s = s.replace('\u00D1','N')
    _s = s.replace('\u00F1','n')
    return _s.replace(/[^a-zA-Z0-9 ]/g, '')
}

console.log(formatName("Jhunel2"));