# JavaScript JS 脚本语言学习

## JSON 数据格式
```js
(function() {
    /* https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON */
    if (!window.JSON) {
        window.JSON = {
            parse: function(sJSON) {
                return eval('(' + sJSON + ')');
            },
            stringify: (function() {
                var toString = Object.prototype.toString;
                var isArray = Array.isArray || function(a) {
                    return toString.call(a) === '[object Array]';
                };
                var escMap = { '"': '\\"', '\\': '\\\\', '\b': '\\b', '\f': '\\f', '\n': '\\n', '\r': '\\r', '\t': '\\t' };
                var escFunc = function(m) {
                    return escMap[m] || '\\u' + (m.charCodeAt(0) + 0x10000).toString(16).substr(1);
                };
                var escRE = /[\\"\u0000-\u001F\u2028\u2029]/g;
                return function stringify(value) {
                    if (value == null) {
                        return 'null';
                    } else if (typeof value === 'number') {
                        return isFinite(value) ? value.toString() : 'null';
                    } else if (typeof value === 'boolean') {
                        return value.toString();
                    } else if (typeof value === 'object') {
                        if (typeof value.toJSON === 'function') {
                            return stringify(value.toJSON());
                        } else if (isArray(value)) {
                            var res = '[';
                            for (var i = 0; i < value.length; i++) res += (i ? ', ': '') + stringify(value[i]);
                            return res + ']';
                        } else if (toString.call(value) === '[object Object]') {
                            var tmp = [];
                            for (var k in value) {
                                if (value.hasOwnProperty(k)) tmp.push(stringify(k) + ': ' + stringify(value[k]));
                            }
                            return '{' + tmp.join(', ') + '}';
                        }
                    }
                    return '"' + value.toString().replace(escRE, escFunc) + '"';
                };
            })()
        };
    }
})();
```

## Date 时间
```js
(function() {
    Date.prototype.FormatAsString = function(format) {
        if (arguments.length <= 0) {
            format = 'yyyy-MM-dd HH:mm:ss';
        }

        var o = {
            "M+" : this.getMonth()+1, //month
            "d+" : this.getDate(), //day
            "[hH]+" : this.getHours(), //hour
            "m+" : this.getMinutes(), //minute
            "s+" : this.getSeconds(), //second
            "q+" : Math.floor((this.getMonth()+3)/3), //quarter
            "S" : this.getMilliseconds() //millisecond
        }
        if(/(y+)/.test(format)) {
            format=format.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
        }
        for(var k in o) {
            if (new RegExp("(" + k + ")").test(format)) {
                format = format.replace(RegExp.$1, RegExp.$1.length==1 ? o[k] : ("00"+ o[k]).substr((""+ o[k]).length));
            }
        }
        return format;
    }
    Date.prototype.GetNormalValue = function() {
        return {
            Year: this.getFullYear(),
            Month: this.getMonth() + 1, // especially!
            Day: this.getDate(), // // especially!
            Hour: this.getHours(),
            Minute: this.getMinutes(),
            Second: this.getSeconds(),
            Millisecond: this.getMilliseconds(),
        };
    }
    Date.prototype.AppendValueClone = function(matchFmt, diffValue) {
        matchFmt = matchFmt || 'TTT';
        var v = this.GetNormalValue();
        diffValue = (!diffValue || isNaN(diffValue)) ? 0 : parseInt(diffValue);
        switch(matchFmt) {
            case 'yyyy': v.Year += diffValue; break;
            case 'MM': v.Month += diffValue; break;
            case 'dd': v.Day += diffValue; break;
            case 'HH':
            case 'hh': v.Hour += diffValue; break;
            case 'mm': v.Minute += diffValue; break;
            case 'ss': v.Second += diffValue; break;
        }
        return window.CommonData.CreateDateTime(v.Year, v.Month, v.Day, v.Hour, v.Minute, v.Second, v.Millisecond);
    }
    Date.prototype.AppendValue = function(matchFmt, diffValue) {
        if (isNaN(diffValue))
            return this;
        switch(matchFmt) {
            case 'yyyy': this.setFullYear(this.getFullYear() + Number(diffValue)); break;
            case 'MM': this.setMonth(this.getMonth() + Number(diffValue)); break;
            case 'dd': this.setDate(this.getDate() + Number(diffValue)); break;
            case 'HH':
            case 'hh': this.setHours(this.getHours() + Number(diffValue)); break;
            case 'mm': this.setMinutes(this.getMinutes() + Number(diffValue)); break;
            case 'ss': this.setSeconds(this.getSeconds() + Number(diffValue)); break;
        }
        return this;
    }
})();
```

## Array 数组
```js
(function() {
    Array.prototype.del = function(n) {
        return n < 0 ? this : this.slice(0, n).concat(this.slice(n + 1, this.length));
    }
})();
```

## JQuery Ajax
```js
function jsonpsuccessbackfunction(a,b,c,d,e,f) {}
(function() {
    window.AjaxRequest = {
        Queue: [null,],
        QueueIndex: 0,
        QueueEnable: false,
        QueueAppend: function(ajax_data) {
            var self = this;
            var index = self.QueueGetFirstMeetCriteriaIndex(0, function(item_data) {
                return item_data === null;
            });
            if (index < 0) {
                self.Queue.push(ajax_data);
            } else {
                self.Queue[index] = ajax_data;
            }
        },
        QueueGetFirstMeetCriteriaIndex: function(init_index, fun_judgmentItemData) {
            var self = this;
            for (var i = init_index; i < self.Queue.length + init_index; i++) {
                var index = i;
                if (index >= self.Queue.length) {
                    index = index - self.Queue.length;
                }
                if (fun_judgmentItemData(self.Queue[index])) {
                    return index;
                }
            }
            return -1;
        },
        QueueExecute: function() {
            var self = this;
            if (self.QueueEnable) {
                return;
            }
            var ajax_data = self.Queue[self.QueueIndex];
            if (ajax_data === null) {
                self.QueueNext();
            } else {
                self.QueueEnable = true;
                $.ajax(ajax_data);
            }
        },
        QueueNext: function() {
            var self = this;
            self.Queue[self.QueueIndex] = null;
            self.QueueEnable = false;
            var index = self.QueueGetFirstMeetCriteriaIndex(self.QueueIndex + 1, function(item_data) {
                return item_data != null;
            });
            if (index < 0) {
                return;
            }
            self.QueueIndex = index;
            self.QueueExecute();
        },
        CrossDomainGet: function(argument_config) {
            var self = this;
            var config = self.MergeConfig(argument_config);
            if (window.CheckData.IsStringNull(config.url)) {
                return;
            }
            var data = {
                url: config.url,
                type: "GET",
                data: config.data,
                dataType: "jsonp",
                async: true,
                jsonp: "callback",
                jsonpCallback: "jsonpsuccessbackfunction",
                success: function(json) {
                    config.EventSuccess(json);
                },
                error: function(XMLHttpRequest_obj, textStatus_obj, errorThrown_obj) {
                    self.ErrorResponseProcessing(XMLHttpRequest_obj, textStatus_obj, errorThrown_obj, config.EventSuccess);
                },
                complete: function(XMLHttpRequest_obj, TypeStatus) {
                    config.EventComplete(XMLHttpRequest_obj, TypeStatus, this);
                    self.QueueNext();
                },
            };
            self.QueueAppend(data);
            self.QueueExecute();
        },
        LocalPost: function(argument_config) {
            var self = this;
            var config = self.MergeConfig(argument_config);
            if (window.CheckData.IsStringNull(config.url)) {
                return;
            }
            var data = {
                url: config.url,
                type: "POST",
                data: config.data,
                dataType: "json",
                async: config.async,
                success: function(json) {
                    config.EventSuccess(json);
                },
                error: function(XMLHttpRequest_obj, textStatus_obj, errorThrown_obj) {
                    self.ErrorResponseProcessing(XMLHttpRequest_obj, textStatus_obj, errorThrown_obj, config.EventSuccess);
                },
                complete: function(XMLHttpRequest_obj, TypeStatus) {
                    config.EventComplete(XMLHttpRequest_obj, TypeStatus, this);
                    if (this.async) {
                        self.QueueNext();
                    }
                },
            };
            if (config.async) {
                self.QueueAppend(data);
                self.QueueExecute();
            } else {
                $.ajax(data);
            }
        },
        MergeConfig: function(argument_config) {
            var self = this;
            var def_conf = {
                url: '',
                data: {},
                async: true,
                EventSuccess: function(json) {},
                EventComplete: function(XMLHttpRequest_obj, TypeStatus, complete_this) {
                    console.log('Ajax Request Complete: ', complete_this.url);
                },
            };
            var config = $.extend(def_conf, argument_config);
            return config;
        },
        ErrorResponseProcessing: function(XMLHttpRequest_obj, textStatus_obj, errorThrown_obj, SuccessEXEMethod) {
            var self = this;
            if (window.CheckData.IsObjectNull(SuccessEXEMethod) || !self.IsSuccessRequest(XMLHttpRequest_obj)) {
                self.PrintErrorInfoObject(XMLHttpRequest_obj, textStatus_obj, errorThrown_obj);
                return;
            }
            var sjson = XMLHttpRequest_obj.responseText;
            if (window.CheckData.IsStringNull(sjson)) {
                self.PrintErrorInfoObject(XMLHttpRequest_obj, textStatus_obj, errorThrown_obj);
            } else {
                self.ParseSJSONExeSuccessMethod(sjson, SuccessEXEMethod);
            }
        },
        ParseSJSONExeSuccessMethod: function(sjson, successMethod) {
            var self = this;
            var json = {};
            try {
                json = window.JSON.parse(sjson);
            } catch(ex) {
                console.log('parse json Error:', json, '\tex:', ex);
                json = {
                    'Status': 0,
                    'Msg': '错误内容!',
                    'Url': '',
                    'Result': {},
                };
            }
            successMethod(json);
        },
        IsSuccessRequest: function(XMLHttpRequest_obj) {
            /* XMLHttpRequest 对象属性值参照地址: http://www.w3school.com.cn/xmldom/dom_http.asp */
            return XMLHttpRequest_obj.status == 200 || XMLHttpRequest_obj.readyState == 4;
        },
        PrintErrorInfoObject: function(XMLHttpRequest_obj, textStatus_obj, errorThrown_obj) {
            console.log('class.AjaxRequest (Error Request Response Result):');
            console.log('XMLHttpRequest:', XMLHttpRequest_obj, 'textStatus:', textStatus_obj, 'errorThrown:', errorThrown_obj);
        }
    };
})();
```


## 参考学习链接:
```shell
# js 删除数组几种方法
# (大神解决方案)
http://www.cnblogs.com/qiantuwuliang/archive/2010/09/01/1814706.html

# JQuery 插件库
http://www.jq22.com/

# jquery JSON的解析方式
https://www.cnblogs.com/leejersey/p/3594473.html
```
