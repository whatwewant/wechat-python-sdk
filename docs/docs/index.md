# 欢迎使用 wechat-python-sdk 开发包

------

# 概述

wechat-python-sdk 希望能帮您解决微信公众平台开发中的种种不便，让您可以专注于业务逻辑本身，而不是浪费精力在与微信服务器复杂的交互中。

本开发包目前支持订阅号、服务号、企业号的官方接口，以及额外添加了扩展功能接口（扩展功能将会直接模拟登陆腾讯官方公众平台去进行相应操作），相信这将会极大的简化您的开发过程。

**请注意：本开发包并不打算提供一个独立的完整微信解决方案，我们更希望这个开发包可以非常融洽的在各个框架中进行集成并使用，对于HTTP请求及响应方面并不涉及，该开发包仅仅接受必要参数，提供各种微信操作的方法，并返回相应的可以响应微信服务器的数据(Response)或操作执行结果。**

# 文档目录

* [安装](install.md)
* [快速教程](quickstart.md)
* [订阅号/服务号文档](subscribe_service.md)
* [企业号文档](corp.md)
* [扩展功能文档](ext.md)
* [常见问题](faq.md)

# 许可协议

本项目采用 MIT 许可协议，可放心集成于商业产品中，但请包含本许可声明。

    Copyright (C) 2014-2015 Ace Kwok
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# 感谢

感谢 [WeRoBot](https://github.com/whtsky/WeRoBot) 项目，本项目中官方接口的许多代码均借鉴于此。